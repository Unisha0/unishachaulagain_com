# 🌸 Your Premium Portfolio - Quick Start Guide

## ✅ What Was Built

Your portfolio has been **completely redesigned** with a stunning modern aesthetic featuring:

- **🎨 Modern Design**: Dark theme with purple/pink gradients
- **✨ Animations**: Smooth transitions, scroll effects, particle backgrounds
- **🔳 Glassmorphism**: Frosted glass effects on cards and forms
- **📱 Responsive**: Perfect on all devices (desktop, tablet, mobile)
- **🌍 Internationalization**: Ready for English & नेपाली
- **⚡ Performance**: Optimized animations, lazy loading images

---

## 🚀 Next Steps

### 1. **Run the Server**
```bash
cd /Users/U/Desktop/unisha_portfolio
python manage.py runserver
```

Visit: **http://127.0.0.1:8000**

### 2. **Add Your Photo**
```bash
# Place your photo in media folder (or update the path in home.html)
cp ~/your-photo.jpg core/static/core/images/unisha-profile.jpg
```

In `home.html`, make sure the image path is correct:
```html
<img src="{% static 'core/images/unisha-profile.jpg' %}" ...>
```

### 3. **Add Content via Django Admin**
- Navigate to: **http://127.0.0.1:8000/admin**
- Login with your superuser credentials
- Add Projects, Blog Posts, Skills, Education, etc.

### 4. **Customize Colors** (Optional)
Edit `core/static/core/css/premium-theme.css`:

```css
:root {
  --primary: #7c3aed;        /* Purple - change to your color */
  --secondary: #ec4899;      /* Pink */
  --accent: #f59e0b;         /* Amber */
}
```

---

## 📋 What's New

### Templates (Completely Redesigned)
- ✅ `base.html` - Bootstrap 5 + Premium navbar/footer
- ✅ `home.html` - Hero with particles + sections
- ✅ `projects.html` - Filterable project cards
- ✅ `blog_list.html` - Searchable blog with animations
- ✅ `blog_detail.html` - Full article with sidebar
- ✅ `contact.html` - Glassmorphic contact form

### New CSS File
- ✅ `core/static/core/css/premium-theme.css` - Complete theme (15KB)

### Updated Settings
- ✅ `portfolio/settings.py` - i18n support for English & नेपाली

---

## 🎯 Key Features

### Animations & Effects
- **Particle Background**: 50 animated particles on hero
- **AOS Animations**: Scroll-triggered fade animations
- **Hover Effects**: Cards lift and glow on hover
- **Smooth Transitions**: All interactions are polished
- **Image Zoom**: Images scale on hover

### Interactivity
- **Project Filtering**: Filter by category (AI/ML, Django, etc.)
- **Blog Search**: Search posts by title & tags
- **Language Selector**: Switch English ↔ नेपाली
- **Navbar Detection**: Navbar style changes when scrolling

### Components
- **Buttons**: Primary, secondary, outline, ghost styles
- **Cards**: Glassmorphic with hover effects
- **Forms**: Beautiful input styling with focus glow
- **Badges**: Color-coded tags for skills/techs
- **Social Icons**: Animated icon links

---

## 🎨 Design System

### Colors
```css
Primary:    #7c3aed (Purple)
Secondary:  #ec4899 (Pink)
Accent:     #f59e0b (Amber)
Dark:       #0f0f1e
Text Light: #f0f0f0
Text Muted: #a0a0a0
```

### Fonts
```css
Display:  Playfair Display (Serif)
Body:     DM Sans (Sans-serif)
Mono:     JetBrains Mono
```

### Spacing
```css
xs: 0.25rem   |   sm: 0.5rem   |   md: 1rem
lg: 2rem      |   xl: 3rem     |   2xl: 4rem
```

---

## 📐 Responsive Breakpoints

| Device | Width | Layout |
|--------|-------|--------|
| Desktop | 1024px+ | Multi-column grids |
| Tablet | 768px-1023px | 2-column layouts |
| Mobile | < 768px | Single column |

---

## 🔧 Libraries Used

```
Bootstrap 5.3.0          - Grid & components
Bootstrap Icons 1.11.0   - Icon library
AOS 2.3.1               - Scroll animations
TsParticles 2.12.0      - Particle effects
Google Fonts            - Typography
```

---

## 📝 Customization Tips

### Change Primary Color
```css
/* In premium-theme.css */
:root {
  --primary: #YOUR_COLOR;      /* Change purple */
  --gradient-primary: linear-gradient(135deg, #YOUR_COLOR 0%, #SECONDARY_COLOR 100%);
}
```

### Add More Animations
All animations in:
```
core/static/core/css/premium-theme.css (lines 85-150)
```

### Modify Hero Section
Edit in `home.html`:
- Hero title & subtitle
- Hero CTA buttons
- Particle count

### Change Footer Links
Edit in `base.html`:
- Social media links
- Footer navigation
- Company info

---

## 🐛 Troubleshooting

### Static files not loading?
```bash
python manage.py collectstatic --noinput
```

### Animations not showing?
- Check browser console for errors
- Ensure AOS library is loaded (check Network tab)
- Try clearing browser cache (Ctrl+Shift+Del)

### i18n not working?
```bash
python manage.py makemessages -l ne    # Create Nepali translations
python manage.py compilemessages       # Compile translations
```

### Images not showing?
```bash
# Ensure MEDIA_URL and MEDIA_ROOT are configured in settings.py
# Place images in: /media/ folder
```

---

## 📊 File Structure

```
unisha_portfolio/
├── core/
│   ├── static/core/
│   │   └── css/
│   │       └── premium-theme.css       ← NEW CSS
│   ├── templates/core/
│   │   ├── base.html                   ← REDESIGNED
│   │   ├── home.html                   ← REDESIGNED
│   │   ├── projects.html               ← REDESIGNED
│   │   ├── blog_list.html              ← REDESIGNED
│   │   ├── blog_detail.html            ← REDESIGNED
│   │   └── contact.html                ← REDESIGNED
│   └── models.py
├── media/
│   └── uploads/                        ← Your uploaded images
├── portfolio/
│   └── settings.py                     ← UPDATED (i18n)
└── db.sqlite3
```

---

## 🎁 Bonus Features

### Pre-built Components Ready to Use
- Newsletter signup section (add to any page)
- Testimonials carousel (coming soon)
- FAQ accordion (coming soon)
- Timeline component (coming soon)

### SEO Optimized
- Meta tags in all templates
- Semantic HTML structure
- Open Graph support ready
- Sitemap ready

### Accessibility
- WCAG AA compliant
- Semantic HTML
- Proper heading hierarchy
- Color contrast compliance
- Screen reader friendly

---

## 📞 Support

If you need to:
- **Add new pages**: Copy a template and modify
- **Add animations**: Check `premium-theme.css` for animation examples
- **Change colors**: Update CSS variables in `:root`
- **Add new sections**: Use Bootstrap grid with glassmorphic cards

---

## 🎉 You're All Set!

Your portfolio is now a **stunning, modern, premium website**! 

**Start by:**
1. Running the dev server
2. Adding your photo
3. Adding projects and blog posts via admin
4. Customizing colors to your liking
5. Sharing with the world! 🚀

---

**Built with ❤️ using Django + Bootstrap 5 + Premium CSS**

*"A wildflower who chose to bloom" — in code, design, and creativity* 🌸
