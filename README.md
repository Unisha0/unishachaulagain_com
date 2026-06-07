# Unisha Chaulagain — Personal Portfolio & Blog

A professional Django portfolio website for Unisha Chaulagain, Computer Engineer, AI/ML builder, and free writer.

## 🌸 Features

- **Home page** — Hero, About, Featured Projects, Skills, Education, Achievements, Goals, Hobbies, Blog preview
- **Projects page** — Filterable by category (AI/ML, Deep Learning, Django, Data Science)
- **Blog** — Write daily posts with tags, cover images, rich HTML content
- **Contact page** — Contact form that saves to database, all social links
- **Django Admin** — Full CMS for all content: posts, projects, certificates, achievements, skills, education
- **Responsive** — Works on all screen sizes

## 🚀 Quick Start

```bash
# 1. Install dependencies
pip install django pillow

# 2. Run migrations
python manage.py migrate

# 3. Load initial data (education, skills, projects, achievements)
python manage.py loaddata core/fixtures/initial_data.json

# 4. Create superuser (for admin panel)
python manage.py createsuperuser

# 5. Start development server
python manage.py runserver
```

Visit: http://127.0.0.1:8000
Admin: http://127.0.0.1:8000/admin (username: admin, password: admin123)

## 📝 How to Write Blog Posts

1. Go to http://yourdomain.com/admin
2. Click **Blog Posts → Add Blog Post**
3. Fill in: Title, Excerpt (short preview), Content (HTML supported), Tags (comma-separated)
4. Check **Published** to make it live
5. Check **Featured** to show it on homepage
6. Save!

## 🖼️ Adding Your Photo

In `core/templates/core/home.html`, find the `photo-placeholder` div and replace with:
```html
<img src="/media/your-photo.jpg" alt="Unisha Chaulagain">
```
Upload your photo via the media folder.

## 🌐 Deployment (on your domain unishachaulagain.com.np)

1. Set `DEBUG = False` in settings.py
2. Set `SECRET_KEY` to a strong random key
3. Run `python manage.py collectstatic`
4. Use gunicorn + nginx (recommended)
5. Point domain DNS to your server

## 📁 Project Structure

```
unisha_portfolio/
├── portfolio/          # Django project settings & urls
├── core/               # Main app
│   ├── models.py       # BlogPost, Project, Certificate, Achievement, Education, Skill, ContactMessage
│   ├── views.py        # home, blog_list, blog_detail, projects, contact
│   ├── urls.py         # URL routing
│   ├── admin.py        # Admin panel config
│   ├── templates/      # All HTML templates
│   │   └── core/
│   │       ├── base.html       # Navigation + Footer + Social links
│   │       ├── home.html       # Full homepage
│   │       ├── blog_list.html  # Blog listing with tag filter
│   │       ├── blog_detail.html# Individual post
│   │       ├── projects.html   # All projects with category filter
│   │       └── contact.html    # Contact form
│   └── fixtures/
│       └── initial_data.json   # Pre-filled data (skills, education, projects, achievements)
└── media/              # Uploaded images (blog covers, project images, certificates)
```

## 🎨 Customization

- **Colors**: Edit CSS variables in `base.html` (`:root` block) — `--rust`, `--earth`, `--moss` etc.
- **Font**: Currently Playfair Display (headings) + DM Sans (body). Change in base.html `<link>` tag.
- **Social links**: Update in `base.html` footer and `contact.html`
- **Email**: Update `unishachaulagain@gmail.com` in `contact.html`

---

Built with ❤️ and Django · *"a wildflower who chose to bloom"*
