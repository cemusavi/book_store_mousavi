from django.db import models
from django.utils.translation import ugettext_lazy as _

<<<<<<< HEAD
from lib.shared_models import BaseModel
=======
from utils.shared_models import BaseModel
>>>>>>> 2e567137b12a8e3fc6bf62255974ab8998a032a4


class Author(BaseModel):
    first_name = models.CharField(_('first name'),
                                  max_length=30,
                                  )

    last_name = models.CharField(_('last name'),
                                 max_length=40
                                 )

    birth_day = models.DateTimeField(_('birthday'),
                                     blank=True,
                                     null=True
                                     )

    death_day = models.DateTimeField(_('death day'),
                                     blank=True,
                                     null=True
                                     )

    class Meta:
        verbose_name = _('Author')
        verbose_name_plural = _('Authors')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
