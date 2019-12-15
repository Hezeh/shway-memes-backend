from django.db import models
import uuid
from users.models import User

class BaseModel(models.Model):
    """Base model for the application. Uses UUID for pk."""
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )

    class Meta:
        """Metadata."""
        abstract = True

class Profile(BaseModel):
    """
    Every user will have one and only one related Profile model.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    """
    Each user will have a field where they can tell other users
    something about themselves. This field will be empty when the user 
    creates their account, so we specify `blank=True`
    """
    bio = models.TextField(blank=True)
    """
    Each user may have an avatar. It is not required
    """
    image = models.URLField(blank=True)   # I prefer an ImageField. Will come back to it.
    """
    Follows is a Many-To-Many relationship where both sided of the 
    relationship are of the same model. In this case, the model is
    Profile. This relationship will be one-way. Just because you're
    following me doesn't mean I am following you. `symmetrical=False`
    does this for us
    """
    follows = models.ManyToManyField(
        'self',
        related_name='followed_by',
        symmetrical=False,
        blank=True
    )

    favorites = models.ManyToManyField(
        'photos.Meme',
        related_name='favorited_by',
        blank=True
    )

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