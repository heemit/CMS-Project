from django.contrib                 import admin
from django.utils.safestring        import mark_safe
from unfold.admin                   import ModelAdmin
from grape_js.widgets               import GrapeJSWidget
from grape_js.models                import GrapeJsHTMLField

# Import models
from .models                        import Page

@admin.register(Page)
class PageAdmin(ModelAdmin):
    list_display    = ("url", "show_header", "show_footer", "preview_link", "updated_at")
    search_fields   = ("url",)
    list_filter     = ("show_header", "show_footer", "updated_at")
    readonly_fields = ("created_at", "updated_at")

    def preview_link(self, obj):
        return mark_safe(f'<a href="/{obj.url}" target="_blank">🔗 Preview</a>')

    preview_link.short_description = "Preview"
