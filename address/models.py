from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _

<<<<<<< HEAD
from lib.shared_models import BaseModel
=======
from utils.shared_models import BaseModel
>>>>>>> 2e567137b12a8e3fc6bf62255974ab8998a032a4

User = get_user_model()


class Address(BaseModel):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='addresses'
                             )
    city = models.CharField(_('City'), max_length=30)
    exact_address = models.CharField(_('Exact address'), max_length=300)

    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')

    def __str__(self):
        return f'{self.city} -> {self.exact_address}'
