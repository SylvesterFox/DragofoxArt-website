from django.contrib import admin

from artlog.models import Artwork

@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    list_display = ("title", "created", "is_published")
    list_filter = ("is_published", )
    search_fields = ("title", )