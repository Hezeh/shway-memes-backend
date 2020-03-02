from django.db import models
from django.db.models import signals, F
import uuid
from django.db import models
from users.models import User
from profiles.models import Profile


# class Tag(models.Model):
#     id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4,)
#     title = models.CharField(max_length=255, unique=True)
#     occurrences = models.IntegerField(default=0)
#     trending = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


#     class Meta(object):
#         """Meta options."""

#         verbose_name = ("Tag")
#         verbose_name_plural = ("Tags")
#         ordering = ['-updated_at']

#     def __str__(self):
#         return self.title


class Image(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4,)
    photo = models.ImageField(upload_to='uploads/', blank=False, default=None)
    created = models.DateTimeField(auto_now_add=True)
    caption = models.CharField(max_length=255, blank=True)
    # tags = models.ManyToManyField('uploads.Tag', related_name='images', blank=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='images', default=None)

    def __str__(self):
        return str(self.id)

    class Meta(object):
        verbose_name = 'Image'
        verbose_name_plural = 'images'
        ordering = ['-created']

    # @property
    # def print_self(self):
    #     print(self.caption)
    
    # @property
    # def activity_object_attr(self):
    #     return self 

    # def save(self, *args, **kwargs):
    #     self.create_hashtags()
    #     super(Image, self).save(*args, **kwargs)

    # def create_hashtags(self):
    #     hashtag_set = set(self.parse_hashtags())
    #     for hashtag in hashtag_set:
    #         h, created = Tag.objects.get_or_create(title=hashtag)
    #         h.save()
    #     Tag.objects.filter(title__in=hashtag_set).update(occurrences=F('occurrences')+1)

    # def parse_hashtags(self):
    #     return [ i for i in self.caption.split() if i.startswith("#")]

    # def parse_mentions(self):
    #     mentions = [i for i in self.caption.split() if i.startswith("@")]
    #     return User.objects.filter(username__in=mentions)

    # def parse_all(self):
    #     parts = self.caption.split()
    #     hashtag_counter = 0
    #     mention_counter = 0
    #     result = {"parsed_text": "", "hashtags": [], "mentions": []}
    #     for index, value in enumerate(parts):
    #         if value.startswith("#"):
    #             parts[index] = "{hashtag" + str(hashtag_counter) + "}"
    #             hashtag_counter += 1
    #             result[u'hashtags'].append(value)
    #             parts[index] = "{mention" + str(mention_counter) + "}"
    #             mention_counter += 1
    #             result[u'mentions'].append(value)
    #     result[u'parsed_text'] = " ".join(parts)
    #     return result

    # @property
    # def activity_notify(self):
    #     targets = [feed_manager.get_news_feeds(self.user_id)['timeline']]
    #     for hashtag in self.parse_hashtags():
    #         targets.append(feed_manager.get_feed('user', 'hash_%s' % hashtag))
    #     for user in self.parse_mentions():
    #         targets.append(feed_manager.get_news_feeds(user.id)['timeline'])
    #     return targets
