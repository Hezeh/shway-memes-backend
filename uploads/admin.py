from django.contrib import admin
from .models import Image, Tag


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    """Image admin"""

    list_display = ('id', 'publication_date')
    search_fields = ('publication_date',)
    filter_horizontal = ('tags',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Tag admin."""

    list_display = ('title',)
    search_fields = ('title',)