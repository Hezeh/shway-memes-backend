from django.contrib import admin
from .models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    """Image admin"""

    list_display = ('id', 'publication_date', 'publisher')
    search_fields = ('publication_date', 'publisher',)
    # filter_horizontal = ('tags',)
    list_per_page = 25


# @admin.register(Tag)
# class TagAdmin(admin.ModelAdmin):
#     """Tag admin."""

#     list_display = ('id', 'title', 'occurrences', 'trending',)
#     search_fields = ('title',)
#     list_editable = ('trending',)
#     list_per_page = 25