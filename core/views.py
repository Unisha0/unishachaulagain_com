from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from .models import BlogPost, Project, Certificate, Achievement, Education, Skill, ContactMessage, PostLike, PostComment, SiteSettings


def home(request):
    featured_projects = Project.objects.filter(featured=True)[:4]
    recent_posts = BlogPost.objects.filter(published=True)[:3]
    achievements = Achievement.objects.all()[:6]
    skills = Skill.objects.all()
    education = Education.objects.all()
    certificates = Certificate.objects.all()
    skill_categories = {}
    for skill in skills:
        cat = skill.get_category_display()
        skill_categories.setdefault(cat, []).append(skill)
    site = SiteSettings.load()
    context = {
        'featured_projects': featured_projects,
        'recent_posts': recent_posts,
        'achievements': achievements,
        'skill_categories': skill_categories,
        'education': education,
        'certificates': certificates,
        'cv_url': site.cv_file.url if site.cv_file else None,
    }
    return render(request, 'core/home.html', context)


def blog_list(request):
    tag = request.GET.get('tag', '')
    posts = BlogPost.objects.filter(published=True)
    if tag:
        posts = [p for p in posts if tag in p.get_tags_list()]
    all_tags = set()
    for post in BlogPost.objects.filter(published=True):
        all_tags.update(post.get_tags_list())
    return render(request, 'core/blog_list.html', {
        'posts': posts, 'all_tags': sorted(all_tags), 'active_tag': tag,
    })


def blog_detail(request, slug):
    post     = get_object_or_404(BlogPost, slug=slug, published=True)
    related  = BlogPost.objects.filter(published=True).exclude(id=post.id)[:3]
    comments = post.comments.filter(approved=True)

    if not request.session.session_key:
        request.session.create()
    user_liked = post.likes.filter(session_key=request.session.session_key).exists()

    return render(request, 'core/blog_detail.html', {
        'post':       post,
        'related':    related,
        'comments':   comments,
        'like_count': post.likes.count(),
        'user_liked': user_liked,
    })


def like_post(request, slug):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST required'}, status=405)
    post = get_object_or_404(BlogPost, slug=slug, published=True)
    if not request.session.session_key:
        request.session.create()
    key = request.session.session_key
    like, created = PostLike.objects.get_or_create(post=post, session_key=key)
    if not created:
        like.delete()
        liked = False
    else:
        liked = True
    return JsonResponse({'liked': liked, 'count': post.likes.count()})


def add_comment(request, slug):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST required'}, status=405)
    post  = get_object_or_404(BlogPost, slug=slug, published=True)
    name  = request.POST.get('name', '').strip()
    email = request.POST.get('email', '').strip()
    body  = request.POST.get('body', '').strip()
    if not name or not body:
        return JsonResponse({'error': 'Name and message are required.'}, status=400)
    PostComment.objects.create(post=post, name=name, email=email, body=body)
    return JsonResponse({'status': 'ok'})


def projects(request):
    all_projects = Project.objects.all()
    categories = Project.CATEGORY_CHOICES
    return render(request, 'core/projects.html', {
        'projects': all_projects,
        'categories': categories,
    })


def contact(request):
    if request.method == 'POST':
        name    = request.POST.get('name', '').strip()
        email   = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()

        ContactMessage.objects.create(
            name=name, email=email, subject=subject, message=message
        )

        # Email notification to Unisha's inbox
        try:
            send_mail(
                subject=f'[Portfolio] {subject} — from {name}',
                message=(
                    f'New contact message from your portfolio:\n\n'
                    f'Name:    {name}\n'
                    f'Email:   {email}\n'
                    f'Subject: {subject}\n\n'
                    f'Message:\n{message}\n\n'
                    f'---\nReply directly to this email to respond.'
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_RECIPIENT_EMAIL],
                reply_to=[email],
                fail_silently=True,
            )
        except Exception:
            pass  # message already saved to DB; email failure is non-fatal

        return JsonResponse({'status': 'ok'})
    return render(request, 'core/contact.html')
