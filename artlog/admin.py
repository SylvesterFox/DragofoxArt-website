from django.contrib import admin
from django.utils.html import format_html

from artlog.models import Artwork, SocialLink

@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    list_display = ("title", "created", "is_published")
    list_filter = ("is_published", )
    search_fields = ("title", )

@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ("title", "icon_preview", "url", "order", "is_active")
    list_editable = ("order", "is_active")
    list_filter = ("is_active",)
    search_fields = ("title", "url")

    @admin.display(description="Иконка")
    def icon_preview(self, obj):
        if not obj.icon:
            return "—"
        return format_html(
            '<img src="{}" alt="" style="height:28px;padding:3px;border-radius:6px;background:#b1684f">',
            obj.icon.url,
        )