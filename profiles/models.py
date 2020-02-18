from django.db import models
import uuid
from users.models import User
from versatileimagefield.fields import VersatileImageField, PPOIField
from django.dispatch import receiver
from versatileimagefield.image_warmer import VersatileImageFieldWarmer


class Profile(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to='profiles', default=None, blank=True)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False, blank=True)
    favorites = models.ManyToManyField(
        'uploads.Image',
        related_name='favorited_by',
        blank=True
    )
    verified = models.BooleanField(default=False)
    is_trending = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def follow(self, profile):
        " Follow profile if we aren't already  following profile."
        self.follows.add(profile)
    
    def unfollow(self, profile):
        "Unfollow profile if we're already following profile"

    def is_following(self, profile):
        "Returns True if we're following profile; False otherwise"
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