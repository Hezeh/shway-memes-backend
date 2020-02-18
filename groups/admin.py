from django.contrib import admin
from .models import Group, GroupPost

admin.site.register(GroupPost)
# admin.site.register(Membership)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'group_name', 
                   'date_formed', 'is_public',
                   'is_trending',)
    search_fields = ('publication_date', 'group_name', 'group_members')
    list_per_page = 10
    filter_horizontal = ('group_members',)
    list_editable = ('is_public', 'is_trending',)
