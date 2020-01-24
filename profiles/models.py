from django.db import models
import uuid
from users.models import User
from versatileimagefield.fields import VersatileImageField, PPOIField
from django.dispatch import receiver
from versatileimagefield.image_warmer import VersatileImageFieldWarmer


class Profile(models.Model):
    id = models.UUIDField(primary_key=True, editable=False,default=uuid.uuid4,)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    headshot = VersatileImageField(
        'Headshot',
        upload_to='headshots/',
        ppoi_field='headshot_ppoi'
    ) 
    headshot_ppoi = PPOIField()
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False, blank=True)

    favorites = models.ManyToManyField(
        'uploads.Image',
        related_name='favorited_by',
        blank=True
    )
    verified = models.BooleanField(default=False, null=True)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return self.user.username

    def follow(self, profile):
        " Follow profile if we aren't already  following profile."
        self.follows.add(profile)
    
    def unfollow(self, profile):
        "Unfollow profile if we're already following profile"

    def is_following(self, profile):
        "Returns True if we're following profile; False otherwise"
        return self.followed_by.filter(pk=profile.pk).exists()

    def favorite(self, meme):
        "Favorite meme if we haven't"
        self.favorites.add(meme)

    def unfavorite(self, meme):
        "Unfavorite meme if we've already favorited it."
        self.favorites.remove(meme)

    def has_favorited(self, meme):
        "Returns True if we have favorited meme; else False"
        return self.favorites.filter(pk=meme.pk).exists()


@receiver(models.signals.post_save, sender=Profile)
def warm_Person_headshot_images(sender, instance, **kwargs):
    """Ensures Profile head shots are created post-save"""
    person_img_warmer = VersatileImageFieldWarmer(
        instance_or_queryset=instance,
        rendition_key_set='person_headshot',
        image_attr='headshot'
    )
    num_created, failed_to_create = person_img_warmer.warm()