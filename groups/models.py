from django.db import models
from users.models import User
import uuid
from uploads.models import Image

class Group(models.Model):
    id = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4,)
    group_name = models.CharField(blank=False, max_length=100, default=None)
    group_members = models.ManyToManyField(User, blank=True)
    date_formed = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)
    is_trending = models.BooleanField(default=False)


    def __str__(self):
        return self.group_name

    # def get_member_list(self):
    #     "Returns a list with members, without admin information"
    #     return [i.user for i in self.membership_set.all()]
    
    # def get_admins_list(self):
    #     "Returns a list with admins, without admin information"
    #     return [i.user for i in self.membership_set.filter(admin=True)]


    class Meta(object):
        ordering = ["date_formed"]
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'


# class Membership(models.Model):
#     "Intermediate table for many-to-many relationship between users and groups"

#     group = models.ForeignKey(Group, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     is_admin = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.group
    

    # class Meta:
    #     'Only one entry per user and group'
    #     unique_together = ('group', 'user')
    #     'Admin first, then sort by username'
    #     ordering = ['-admin', 'user__username']


class GroupPost(models.Model):
    id = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4,)
    group = models.ForeignKey(Group, blank=False, on_delete=models.CASCADE)
    post = models.ImageField(blank=False)
    author = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    publication_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.group

    class Meta(object):
        # ordering = ["publication_date"]
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        
    