# from django.conf import settings
# from django_elasticsearch_dsl import Document, Index, fields
# from elasticsearch_dsl import analyzer
# from django_elasticsearch_dsl_drf.compat import KeywordField, StringField

# from profiles.models import Profile

# # Name of the Elasticsearch index
# INDEX = Index(settings.ELASTICSEARCH_INDEX_NAMES[__name__])

# # See Elasticsearch Indices API reference for available settings
# INDEX.settings(
#     number_of_shards=1,
#     number_of_replicas=1
# )

# html_strip = analyzer(
#     'html_strip',
#     tokenizer="standard",
#     filter=["standard", "lowercase", "stop", "snowball"],
#     char_filter=["html_strip"]
# )

# @INDEX.doc_type
# class ProfileDocument(Document):
#     """Book Elasticsearch document."""

#     user = fields.ObjectField(properties={
#         'username': StringField(
#                 # attr='user_indexing',
#                 analyzer=html_strip,
#                 fields={
#                     'raw': KeywordField(),
#                     'suggest': fields.CompletionField(),
#                 }
#             ),
#     }
#     )

#     created = fields.DateField()

#     class Django(object):
#         """Inner nested class Django."""

#         model = Profile  # The model associate with this Document
#         parallel_indexing = True