from django.db import models
from django.utils.translation import ugettext_lazy as _


class BaseModel(models.Model):
    created = models.DateTimeField(_('created'),
                                   auto_now_add=True,
                                   )
    updated = models.DateTimeField(_('updated'),
                                   auto_now=True)

    class Meta:
        abstract = True
