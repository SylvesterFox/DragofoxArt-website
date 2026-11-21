from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from artlog.models import Artwork, SocialLink, CommissonsStatus

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

@admin.register(CommissonsStatus)
class CommissonStatusAdmin(admin.ModelAdmin):
    list_display = ("commissons_status", "edit_link")

    def edit_link(self, obj):
        url = reverse(
            "admin:%s_%s_change" % (
                obj._meta.app_label,
                obj._meta.model_name
            ),
            args=[obj.pk]
        )
        return format_html('<a href="{}">Изменить</a>', url)

    edit_link.short_description = ""

    def has_add_permission(self, request):
        return not CommissonsStatus.objects.exists()

    def has_delete_permission(self, request, obj = None):
        return False