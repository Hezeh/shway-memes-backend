from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'verified', 'is_trending')
    list_display_links = ('id', 'user',)
    list_editable = ('verified', 'is_trending')
    search_fields = ('user',)
    list_per_page = 10