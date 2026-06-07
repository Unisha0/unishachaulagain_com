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

## 🌐 Deployment (Production-ready for unishachaulagain.com.np)

This project is configured for `unishachaulagain.com.np` and `www.unishachaulagain.com.np`.
The Django settings now use environment variables for security and deploy static files using `whitenoise`.

### Required environment variables
Create a local `.env` file or export the values before running the app:
```bash
export DJANGO_SECRET_KEY='your-strong-secret-key'
export DJANGO_DEBUG=False
export DJANGO_ALLOWED_HOSTS='unishachaulagain.com.np,www.unishachaulagain.com.np'
export DJANGO_CSRF_TRUSTED_ORIGINS='https://unishachaulagain.com.np,https://www.unishachaulagain.com.np'
export EMAIL_HOST='smtp.gmail.com'
export EMAIL_PORT=587
export EMAIL_USE_TLS=True
export EMAIL_HOST_USER='your-email@example.com'
export EMAIL_HOST_PASSWORD='your-email-app-password'
export DEFAULT_FROM_EMAIL='Unisha Portfolio <your-email@example.com>'
export CONTACT_RECIPIENT_EMAIL='your-email@example.com'
```

### Deploy steps
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set the environment variables above.
3. Run migrations:
   ```bash
   python manage.py migrate
   ```
4. Load initial data:
   ```bash
   python manage.py loaddata core/fixtures/initial_data.json
   ```
5. Collect static files:
   ```bash
   python manage.py collectstatic
   ```
6. Start the app with Gunicorn:
   ```bash
   gunicorn portfolio.wsgi:application --bind 0.0.0.0:8000
   ```

For production, run behind a reverse proxy such as nginx and serve HTTPS for `unishachaulagain.com.np`.

### Notes
- `DEBUG` must be `False` in production.
- `DJANGO_SECRET_KEY` must be a strong unique secret.
- Do not commit `.env` or any credentials to GitHub.

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
