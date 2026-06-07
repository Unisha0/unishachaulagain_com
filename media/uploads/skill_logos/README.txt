SKILL LOGOS — SVG Icons for Unisha's Portfolio
================================================

All icons are official SVGs from Devicons (https://devicons.dev)

FILES:
  python.svg       — Python (blue)
  pytorch.svg      — PyTorch (red)
  tensorflow.svg   — TensorFlow (orange)
  django.svg       — Django (dark green)
  react.svg        — React (cyan)
  postgresql.svg   — PostgreSQL (blue)
  docker.svg       — Docker (blue)
  javascript.svg   — JavaScript (yellow)
  git.svg          — Git (red-orange)
  aws.svg          — Amazon Web Services (orange)
  sql.svg          — SQL / MySQL (blue)

HOW TO USE IN YOUR DJANGO TEMPLATE:
=====================================

1. Copy all SVG files into:
   core/static/core/images/skills/

2. In your settings.py, make sure you have:
   STATIC_URL = '/static/'

3. In your template (e.g. home.html), replace emoji icons with:

   {% load static %}

   <img src="{% static 'core/images/skills/python.svg' %}"
        alt="Python" width="48" height="48">

EXAMPLE — Skills Section:
--------------------------

{% load static %}

<div class="skills-grid">
  <div class="skill-card">
    <img src="{% static 'core/images/skills/python.svg' %}" alt="Python" width="48" height="48">
    <span>Python</span>
  </div>
  <div class="skill-card">
    <img src="{% static 'core/images/skills/pytorch.svg' %}" alt="PyTorch" width="48" height="48">
    <span>PyTorch</span>
  </div>
  <!-- ... repeat for each skill -->
</div>

STYLING TIP:
------------
For a professional look, set a consistent size and use object-fit:

  .skill-card img {
    width: 48px;
    height: 48px;
    object-fit: contain;
  }

