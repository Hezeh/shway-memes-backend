from django.db import models
import uuid
from users.models import User
from django.dispatch import receiver
from groups.models import Group


class Profile(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to='profiles', default=None, blank=True)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False, blank=True)
    favorites = models.ManyToManyField('uploads.Image', related_name='favorited_by', blank=True)
    reposts = models.ManyToManyField('uploads.Image', related_name='reposted_by', blank=True)
    is_trending = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    groups = models.ManyToManyField(Group, default=None, related_name='joined_by', blank=True)

    def __str__(self):
        return self.user.username


    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    @property
    def user_indexing(self):
        """Publisher for indexing.
        Used in Elasticsearch indexing.
        """
        if self.user is not None:
            return self.user.username

    @property
    def null_field_indexing(self):
        """null_field for indexing.
        Used in Elasticsearch indexing/tests of `isnull` functional filter.
        """
        return None

    def join(self, group):
        "Join group if we haven't joined group; False otherwise"
        self.groups.add(group)

    def disjoin(self, group):
        "Disjoin group if we're already members; False otherwise"
        self.groups.remove(group)

    # def is_admin(self, group):
    #     self.groups.filter(pk=group.pk).exists()

    def has_joined(self, group):
        "Returns True if we have joined group; else False"
        return self.groups.filter(pk=group.pk).exists()

    def follow(self, profile):
        " Follow profile if we aren't already  following profile."
        self.follows.add(profile)
    
    def unfollow(self, profile):
        "Unfollow profile if we're already following profile"
        self.follows.remove(profile)

    def is_following(self, profile):
        "Returns True if we're following profile; False otherwise"
        return self.follows.filter(pk=profile.pk).exists()

    def is_followed_by(self, profile):
        """Returns True if `profile` is following us; False otherwise."""
        return self.followed_by.filter(pk=profile.pk).exists()

    def favorite(self, photo):
        "Favorite photo if we haven't"
        self.favorites.add(photo)

    def unfavorite(self, photo):
        "Unfavorite photo if we've already favorited it."
        self.favorites.remove(photo)

    def has_favorited(self, photo):
        "Returns True if we have favorited photo; else False"
        return self.favorites.filter(pk=photo.pk).exists()

    def repost(self, photo):
        self.reposts.add(photo)

    def unrepost(self, photo):
        self.reposts.remove(photo)

    def has_reposted(self, photo):
        return self.reposts.filter(pk=photo.pk).exists()