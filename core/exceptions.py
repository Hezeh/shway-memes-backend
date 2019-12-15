from django.utils.translation import ugettext_lazy as _ 


class ReadOnlyException(Exception):
    def __init__(self, msg=None):
        if msg is None:
            msg = _("API runs in read-only mode")
        super().__init__(msg)