import os
import io
import re

from django.contrib import admin
from django.contrib import messages
from django.utils.html import format_html, mark_safe
from django_summernote.admin import SummernoteModelAdmin

from .models import BlogPost, Project, Certificate, Achievement, Education, Skill, ContactMessage, PostComment, PostLike, SiteSettings


def _extract_docx(file_obj):
    """Convert .docx to clean HTML using mammoth."""
    import mammoth
    result = mammoth.convert_to_html(file_obj)
    return result.value


def _extract_pdf(file_obj):
    """Extract text from PDF and wrap in basic HTML paragraphs."""
    from pdfminer.high_level import extract_text_to_fp
    from pdfminer.layout import LAParams
    out = io.StringIO()
    extract_text_to_fp(file_obj, out, laparams=LAParams(), output_type='text', codec='utf-8')
    raw = out.getvalue()
    paras = [p.strip() for p in re.split(r'\n{2,}', raw) if p.strip()]
    return ''.join(f'<p>{p}</p>' for p in paras)


def _auto_excerpt(html_content, word_limit=40):
    """Strip HTML tags and return first N words as plain-text excerpt."""
    plain = re.sub(r'<[^>]+>', ' ', html_content)
    plain = re.sub(r'\s+', ' ', plain).strip()
    words = plain.split()
    snippet = ' '.join(words[:word_limit])
    return snippet + ('…' if len(words) > word_limit else '')


def _estimate_read_time(html_content):
    """~200 words per minute reading speed."""
    plain = re.sub(r'<[^>]+>', ' ', html_content)
    words = len(plain.split())
    return max(1, round(words / 200))


# ── Blog Post Admin ──────────────────────────────────────────────────────────

@admin.register(BlogPost)
class BlogPostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

    list_display = ['title', 'type_badge', 'published', 'featured', 'read_time_display', 'created_at']
    list_filter  = ['post_type', 'published', 'featured', 'created_at']
    list_editable = ['published', 'featured']
    search_fields = ['title', 'excerpt', 'content', 'tags']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-created_at']
    date_hierarchy = 'created_at'

    fieldsets = (
        ('📝 Content', {
            'fields': ('post_type', 'title', 'slug', 'excerpt', 'content'),
            'description': 'Write your post below. Use the toolbar for formatting, images, colors, and font sizes.',
        }),
        ('📄 Import from Document', {
            'fields': ('source_document',),
            'classes': ('collapse',),
            'description': (
                '<strong style="color:#c05a2c">Upload a .docx or .pdf file and save</strong> — '
                'the content will be extracted automatically and placed in the editor above. '
                'Supports Word documents and PDFs. The file upload is cleared after extraction.'
            ),
        }),
        ('🖼 Media', {
            'fields': ('cover_image',),
        }),
        ('🏷 Meta', {
            'fields': ('tags', 'read_time'),
            'description': 'Tags are comma-separated. Leave read_time as 0 to auto-calculate.',
        }),
        ('⚙ Publish', {
            'fields': ('published', 'featured', 'created_at'),
        }),
    )

    readonly_fields = []

    def save_model(self, request, obj, form, change):
        doc = obj.source_document
        if doc:
            name = doc.name.lower()
            try:
                doc.seek(0)
                if name.endswith('.docx'):
                    obj.content = _extract_docx(doc)
                    messages.success(request, '✅ Word document extracted into editor successfully.')
                elif name.endswith('.pdf'):
                    obj.content = _extract_pdf(doc)
                    messages.success(request, '✅ PDF extracted into editor successfully.')
                else:
                    messages.warning(request, '⚠ Unsupported file type. Only .docx and .pdf are supported.')
            except Exception as e:
                messages.error(request, f'❌ Could not extract document: {e}')
            # Clear the document field after extraction — no need to keep it
            obj.source_document = None

        # Auto-fill excerpt if empty
        if not obj.excerpt and obj.content:
            obj.excerpt = _auto_excerpt(obj.content)

        # Auto-calculate read time
        if obj.read_time == 0 and obj.content:
            obj.read_time = _estimate_read_time(obj.content)

        super().save_model(request, obj, form, change)

    # ── List display helpers ──

    def type_badge(self, obj):
        colours = {
            'blog':     ('#c05a2c', '#fff3ee', '✍ Blog'),
            'research': ('#5a6cc0', '#eef0ff', '🔬 Research'),
            'tutorial': ('#22a06b', '#edfdf5', '📖 Tutorial'),
            'note':     ('#888',    '#f5f5f5', '📌 Note'),
        }
        color, bg, label = colours.get(obj.post_type, ('#888', '#f5f5f5', obj.post_type))
        return format_html(
            '<span style="background:{};color:{};padding:2px 9px;border-radius:12px;'
            'font-size:11px;font-weight:600;">{}</span>',
            bg, color, label
        )
    type_badge.short_description = 'Type'

    def read_time_display(self, obj):
        if obj.read_time:
            return f'{obj.read_time} min read'
        return '—'
    read_time_display.short_description = 'Read time'


# ── Project Admin ────────────────────────────────────────────────────────────

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display  = ['thumbnail', 'title', 'category', 'priority_badge', 'featured', 'order', 'github_link']
    list_filter   = ['category', 'priority', 'featured']
    list_editable = ['featured', 'order']
    search_fields = ['title', 'description', 'tech_stack']
    ordering      = ['order']

    fieldsets = (
        ('Project Info', {
            'fields': ('title', 'description', 'category', 'priority', 'tech_stack'),
        }),
        ('Links', {
            'fields': ('github_url', 'live_url'),
        }),
        ('Image', {
            'fields': ('image', 'image_preview'),
            'description': 'Upload a project screenshot or cover image. Recommended: 800×500 px.',
        }),
        ('Display', {
            'fields': ('featured', 'order'),
        }),
    )

    readonly_fields = ['image_preview']

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-width:480px;max-height:280px;'
                'border-radius:8px;border:1px solid #e0e0e0;margin-top:6px;" />',
                obj.image.url
            )
        return format_html('<span style="color:#aaa;">No image uploaded yet.</span>')
    image_preview.short_description = 'Current image'

    def thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width:56px;height:36px;object-fit:cover;'
                'border-radius:4px;border:1px solid #ddd;" />',
                obj.image.url
            )
        return mark_safe('<span style="color:#ccc;font-size:11px;">—</span>')
    thumbnail.short_description = ''

    def priority_badge(self, obj):
        if obj.priority == 'major':
            return mark_safe(
                '<span style="background:#fef9c3;color:#b45309;padding:2px 8px;'
                'border-radius:10px;font-size:11px;font-weight:700;">⭐ Major</span>'
            )
        elif obj.priority == 'minor':
            return mark_safe(
                '<span style="background:#ede9fe;color:#6d28d9;padding:2px 8px;'
                'border-radius:10px;font-size:11px;font-weight:700;">· Minor</span>'
            )
        return mark_safe('<span style="color:#aaa;font-size:11px;">Standard</span>')
    priority_badge.short_description = 'Priority'

    def github_link(self, obj):
        if obj.github_url:
            return format_html('<a href="{}" target="_blank" style="color:#c05a2c">GitHub ↗</a>', obj.github_url)
        return '—'
    github_link.short_description = 'GitHub'


# ── Other Admins ─────────────────────────────────────────────────────────────

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display  = ['title', 'issuer', 'issue_date', 'order']
    list_editable = ['order']


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display  = ['title', 'year', 'icon', 'order']
    list_editable = ['order']


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display  = ['institution', 'degree', 'start_year', 'end_year', 'order']
    list_editable = ['order']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display  = ['name', 'category', 'order']
    list_filter   = ['category']
    list_editable = ['order']


@admin.register(PostComment)
class PostCommentAdmin(admin.ModelAdmin):
    list_display  = ['name', 'post', 'short_body', 'approved', 'approved_badge', 'created_at']
    list_filter   = ['approved', 'created_at']
    list_editable = ['approved']
    search_fields = ['name', 'body', 'post__title']
    ordering      = ['-created_at']
    readonly_fields = ['post', 'name', 'email', 'body', 'created_at']
    actions       = ['approve_comments', 'reject_comments']

    def short_body(self, obj):
        return obj.body[:60] + ('…' if len(obj.body) > 60 else '')
    short_body.short_description = 'Message'

    def approved_badge(self, obj):
        if obj.approved:
            return format_html('<span style="color:#22a06b;font-weight:700;">✓ Approved</span>')
        return format_html('<span style="color:#c05a2c;font-weight:700;">⏳ Pending</span>')
    approved_badge.short_description = 'Status'

    @admin.action(description='✅ Approve selected comments')
    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
        self.message_user(request, f'{queryset.count()} comment(s) approved.')

    @admin.action(description='🗑 Reject & delete selected comments')
    def reject_comments(self, request, queryset):
        count = queryset.count()
        queryset.delete()
        self.message_user(request, f'{count} comment(s) deleted.')


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('📄 CV / Resume', {
            'fields': ('cv_file',),
            'description': (
                'Upload your latest CV as a PDF. '
                'Once saved, the <strong>Download CV</strong> button on the homepage will serve this file. '
                'Uploading a new file replaces the old one automatically.'
            ),
        }),
    )

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        # Redirect straight to the single settings object instead of a list
        obj, _ = SiteSettings.objects.get_or_create(pk=1)
        from django.http import HttpResponseRedirect
        from django.urls import reverse
        return HttpResponseRedirect(
            reverse('admin:core_sitesettings_change', args=[obj.pk])
        )


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display    = ['name', 'email', 'subject', 'received_at', 'read', 'read_badge']
    list_filter     = ['read']
    list_editable   = ['read']
    readonly_fields = ['name', 'email', 'subject', 'message', 'received_at']
    ordering        = ['-received_at']

    def read_badge(self, obj):
        if obj.read:
            return format_html('<span style="color:#22a06b;font-weight:600;">✓ Read</span>')
        return format_html('<span style="color:#c05a2c;font-weight:600;">● New</span>')
    read_badge.short_description = 'Status'
