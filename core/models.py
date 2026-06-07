from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class BlogPost(models.Model):
    POST_TYPE_CHOICES = [
        ('blog', 'Blog Post'),
        ('research', 'Research / Paper'),
        ('tutorial', 'Tutorial'),
        ('note', 'Quick Note'),
    ]
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    post_type = models.CharField(max_length=20, choices=POST_TYPE_CHOICES, default='blog')
    excerpt = models.TextField(max_length=500, blank=True)
    content = models.TextField()
    cover_image = models.ImageField(upload_to='blog/', blank=True, null=True)
    source_document = models.FileField(
        upload_to='blog/documents/',
        blank=True, null=True,
        help_text='Upload a .docx or .pdf — content will be extracted automatically.'
    )
    tags = models.CharField(max_length=200, blank=True, help_text='Comma-separated tags')
    read_time = models.PositiveIntegerField(default=0, help_text='Estimated read time in minutes (0 = auto)')
    published = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_tags_list(self):
        if self.tags:
            return [t.strip() for t in self.tags.split(',')]
        return []


class Project(models.Model):
    CATEGORY_CHOICES = [
        ('ai_ml', 'AI / Machine Learning'),
        ('deep_learning', 'Deep Learning'),
        ('django', 'Django / Web'),
        ('data', 'Data Science'),
        ('other', 'Other'),
    ]
    PRIORITY_CHOICES = [
        ('major', 'Major'),
        ('minor', 'Minor'),
        ('', 'Standard'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, blank=True, default='')
    tech_stack = models.CharField(max_length=300)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

    def get_tech_list(self):
        return [t.strip() for t in self.tech_stack.split(',')]


class Certificate(models.Model):
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=100)
    issue_date = models.DateField()
    credential_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='certificates/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', '-issue_date']

    def __str__(self):
        return f"{self.title} — {self.issuer}"


class Achievement(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    year = models.CharField(max_length=10)
    icon = models.CharField(max_length=50, default='⭐')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', '-year']

    def __str__(self):
        return self.title


class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field = models.CharField(max_length=200, blank=True)
    start_year = models.CharField(max_length=10)
    end_year = models.CharField(max_length=10, blank=True)
    description = models.TextField(blank=True)
    institution_url = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.degree} — {self.institution}"


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('languages', 'Languages'),
        ('frameworks', 'Frameworks'),
        ('ai_ml', 'AI / ML'),
        ('tools', 'Tools & Platforms'),
        ('databases', 'Databases'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    emoji = models.CharField(max_length=10, default='🔧')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['category', 'order']

    def __str__(self):
        return self.name


class PostLike(models.Model):
    post        = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='likes')
    session_key = models.CharField(max_length=40)
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['post', 'session_key']

    def __str__(self):
        return f'Like on "{self.post.title}"'


class PostComment(models.Model):
    post       = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    name       = models.CharField(max_length=100)
    email      = models.EmailField(blank=True)
    body       = models.TextField()
    approved   = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f'{self.name} on "{self.post.title}"'


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    received_at = models.DateTimeField(default=timezone.now)
    read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-received_at']

    def __str__(self):
        return f"{self.name} — {self.subject}"


class SiteSettings(models.Model):
    cv_file = models.FileField(
        upload_to='cv/',
        blank=True,
        null=True,
        help_text='Upload your CV/resume as a PDF. Used for the "Download CV" button on the homepage.',
    )

    class Meta:
        verbose_name = 'Site Settings'
        verbose_name_plural = 'Site Settings'

    def __str__(self):
        return 'Site Settings'

    def save(self, *args, **kwargs):
        self.pk = 1  # singleton
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj
