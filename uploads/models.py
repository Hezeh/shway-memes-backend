from django.db import models
from django.db.models import signals
from versatileimagefield.fields import PPOIField, VersatileImageField
from versatileimagefield.image_warmer import VersatileImageFieldWarmer
from django.dispatch import receiver
import uuid
from django.db import models
from users.models import User
from django.db.models.signals import post_save
from versatileimagefield.fields import VersatileImageField, PPOIField

class Tag(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4,)
    title = models.CharField(max_length=255, unique=True)

    class Meta(object):
        """Meta options."""

        verbose_name = ("Tag")
        verbose_name_plural = ("Tags")

    def __str__(self):
        return self.title

class Image(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4,)
    publisher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='images')
    # photo = models.ImageField(upload_to='images', blank=False)
    photo = VersatileImageField(
        'Upload',
        upload_to='uploads/',
        ppoi_field='photo_ppoi'
    )
    photo_ppoi = PPOIField()
    publication_date = models.DateTimeField(auto_now_add=True)
    caption = models.CharField(max_length=255)
    tags = models.ManyToManyField('uploads.Tag', related_name='images', blank=True)
    
    # looped_by = models.ManyToManyField('profiles.Profile', related_name='reposters')

    class Meta(object):
        """Meta options."""
        ordering = ["publication_date"]
        verbose_name = 'Image'
        verbose_name_plural = 'images'

    def __str__(self):
        return self.id

    """
    The only  publisher information we're going to need in our document
    is the publisher name. Since publisher isn't a required field,
    we define a properly on a model level to avoid indexing errors on
    non-existing relation.
    """
    # @property
    # def publisher_indexing(self):
    #     """
    #     Publisher for indexing. 
    #     Used in Elasticsearch indexing.
    #     """
    #     if self.publisher is not None:
    #         return self.publisher.name

    """
    As of tags, again, we only need a flat list of tags names, on which
    we can filter. Therefore, we define a properly on a model level, which
    will return a JSON dumped list of tags relevant to the current 
    meme model object
    """
    # @property
    # def tags_indexing(self):
    #     """
    #     Tags for indexing.
    #     Used in Elasticsearch indexing
    #     """
    #     return [tag.title for tag in self.tags.all()]

    
    # @property
    # def activity_object_attr(self):
    #     return self 
    
    # def save(self):
    #     self.create_hashtags()
    #     super(Image, self).save()

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



@receiver(models.signals.post_save, sender=Image)
def warm_Meme_images(sender, instance, **kwargs):
    "Ensures images are created post-save"
    person_img_warmer = VersatileImageFieldWarmer(
        instance_or_queryset=instance,
        rendition_key_set='meme_shot',
        #image_attr='meme_shot'
    )
    num_created, failed_to_create = person_img_warmer.warm()


# class Like(models.Model):
#     post = models.ForeignKey(Image, related_name='liked_post')
#     user = models.ForeignKey(User, related_name='liker')
#     dated_created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'{self.user} : {self.post}'

# def parse_hash_tags(sender, instance, created, **kwargs):
#     post_save.disconnect(parse_hash_tags, sender=Image)
#     instance.tags = ','.join(re.findall(r'(?:#(\w+))', instance=caption))
#     instance.save()
#     post_save.connect(parse_hash_tags, sender=Image)

# post_save.connect(parse_hash_tags, sender=Image)
