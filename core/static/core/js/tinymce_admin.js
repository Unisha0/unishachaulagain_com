document.addEventListener('DOMContentLoaded', function () {
    if (typeof tinymce === 'undefined') return;

    tinymce.init({
        selector: '#id_content',
        plugins: 'lists link image media table code blockquote fullscreen wordcount',
        toolbar: [
            'undo redo | bold italic underline strikethrough | forecolor backcolor',
            'h1 h2 h3 | bullist numlist | blockquote | link image media | table | code fullscreen'
        ],
        toolbar_mode: 'sliding',
        menubar: 'edit insert format table',
        height: 550,
        resize: true,
        skin: 'oxide',
        content_css: 'default',
        body_class: 'blog-content-preview',
        content_style: `
            body { font-family: Georgia, serif; font-size: 16px; line-height: 1.8; color: #2C2018; padding: 1.5rem; max-width: 800px; margin: 0 auto; }
            h1 { font-size: 2rem; font-weight: 700; margin: 2rem 0 1rem; }
            h2 { font-size: 1.6rem; font-weight: 700; margin: 1.75rem 0 0.75rem; }
            h3 { font-size: 1.25rem; font-weight: 700; margin: 1.5rem 0 0.6rem; }
            p { margin-bottom: 1.25rem; }
            blockquote { border-left: 3px solid #C05A2C; padding-left: 1.5rem; margin: 1.5rem 0; font-style: italic; color: #7A6450; }
            code { background: #F3EFE8; padding: 0.2em 0.4em; border-radius: 3px; font-family: monospace; font-size: 0.9em; }
            pre { background: #F3EFE8; padding: 1.25rem; border-radius: 6px; overflow-x: auto; }
            img { max-width: 100%; height: auto; border-radius: 6px; }
        `,
        image_uploadtab: false,
        link_default_target: '_blank',
        link_assume_external_targets: true,
        setup: function(editor) {
            editor.on('change', function() {
                editor.save();
            });
        }
    });
});
