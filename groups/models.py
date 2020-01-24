from django.db import models
from users.models import User
import uuid

class Group(models.Model):
    id = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4,)
    group_name = models.CharField(blank=False, max_length=100, default=None)
    group_members = models.ManyToManyField(User, blank=True)
    date_formed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.group_name

    class Meta(object):
        ordering = ["date_formed"]
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'


class GroupPost(models.Model):
    id = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4,)
    group = models.OneToOneField(Group, blank=False, on_delete=models.CASCADE)
    post = models.ImageField(blank=False)
    author = models.OneToOneField(User, blank=False, on_delete=models.CASCADE)
    publication_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.id

    class Meta(object):
        ordering = ["publication_date"]
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        
    