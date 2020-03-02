from django.contrib import admin
from .models import Group, GroupPost

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created', 'is_public', 'is_trending',)
    search_fields = ('created', 'name', 'group_members')
    list_per_page = 10
    filter_horizontal = ('members',)
    list_editable = ('is_public', 'is_trending',)

@admin.register(GroupPost)
class GroupPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'group', 'author', 'created',)
    search_fields = ('created', 'group', 'author', )
    list_per_page = 10