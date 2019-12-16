from django.db import models
from django.db.models import signals
# from versatileimagefield.fields import PPOIField, VersatileImageField
# from versatileimagefield.image_warmer import VersatileImageFieldWarmer
# from django.dispatch import receiver
import uuid
from django.db import models
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


class Tag(BaseModel):
    tag = models.TextField(default='#DankMeme')

    def __str__(self):
        return self.tag

class Meme(models.Model):
    """ 
    Every meme must have an author. 
    This gives permissions tho who gets credit for posting the
    meme and who can delete it .A Profile can have many memes"""
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )
    author = models.ForeignKey('profiles.Profile', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='memes', blank=False)
    # ppoi = PPOIField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('photos.Tag', related_name='memes', blank=True)

    def __str__(self):
        #return self.id
        return f"Posted on {self.uploaded_at} and meme key is {self.id}"

    
    # @property
    # def activity_object_attr(self):
    #     return self 
    
    # def save(self):
    #     self.create_hashtags()
    #     super(Meme, self).save()

    # def create_hashtags(self):
    #     hashtag_set = set(self.parse_hashtags())
    #     for hashtag in hashtag_set:
    #         h, created = Hashtag.objects.get_or_create(name=hashtag)
    #         h.save()
    #     Hashtag.objects.filter(name__in=hashtag_set).update(occurrences=F('occurrences')+1)

    # def parse_hashtags(self):
    #     return [slugify(i) for i in self.text.split() if i.startswith("#")]

    # def parse_mentions(self):
    #     mentions = [slugify(i) for i in self.text.split() if i.startswith("@")]
    #     return User.objects.filter(username__in=mentions)

    # def parse_all(self):
    #     parts = self.text.split()
    #     hashtag_counter = 0
    #     mention_counter = 0
    #     result = {"parsed_text": "", "hashtags": [], "mentions": []}
    #     for index, value in enumerate(parts):
    #         if value.startswith("#"):
    #             parts[index] = "{hashtag" + str(hashtag_counter) + "}"
    #             hashtag_counter += 1
    #             result[u'hashtags'].append(slugify(value))
    #         if value.startswith("@"):
    #             parts[index] = "{mention" + str(mention_counter) + "}"
    #             mention_counter += 1
    #             result[u'mentions'].append(slugify(value))
    #     result[u'parsed_text'] = " ".join(parts)
    #     return result

    class Meta:
        #ordering = ('-uploaded_at',)
        verbose_name = 'Meme'
        verbose_name_plural = 'Memes'

# @receiver(models.signals.post_save, sender=Meme)
# def warm_Meme_images(sender, instance, **kwargs):
#     "Ensures Meme images are created post-save"
#     person_img_warmer = VersatileImageFieldWarmer(
#         instance_or_queryset=instance,
#         rendition_key_set='meme_shot',
#         #image_attr='meme_shot'
#     )
#     num_created, failed_to_create = person_img_warmer.warm()



# class Like(BaseModel):
#     """A 'like' on a photo."""

#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
#     photo = models.ForeignKey(Meme, on_delete=models.CASCADE, related_name="likes")
#     date_liked = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.user} Like"

#     class Meta:
#         """Metadata."""

#         unique_together = (("user", "photo"),)
#         ordering = ["-date_liked"]