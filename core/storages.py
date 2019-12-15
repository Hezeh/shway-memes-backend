from django.conf import settings 
from storages.backends.gcloud import GoogleCloudStorage

class GCSMediaStorage(GoogleCloudStorage):
    def __init__(self, *args, **kwargs):
        self.bucket_name = settings.GS_MEDIA_BUCKET_NAME
        super().__init__(*args, **kwargs)