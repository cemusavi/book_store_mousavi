from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core import validators
from django.core import exceptions

<<<<<<< HEAD
from lib.shared_models import BaseModel
from .utils import cash_code_generator
from .utils import percent_code_generator
=======
from utils.shared_models import BaseModel
>>>>>>> 2e567137b12a8e3fc6bf62255974ab8998a032a4

User = get_user_model()


class MainCodeDiscount(BaseModel):
    users = models.ManyToManyField(User,
                                   blank=True,
                                   )

    code = models.CharField(_('Code Discount'),
                            unique=True,
<<<<<<< HEAD
                            max_length=30,
                            blank=True,
=======
                            max_length=30
>>>>>>> 2e567137b12a8e3fc6bf62255974ab8998a032a4
                            )

    expiration_date = models.DateTimeField(_('Expiration Date'))

    def __str__(self):
        return f'{self.code} -> {self.expiration_date}'

    class Meta:
        abstract = True


class MainDiscount(BaseModel):
    expiration_date = models.DateTimeField(_('Expiration Date'))

    def __str__(self):
        return f'{self.expiration_date}'

    class Meta:
        abstract = True


class Cash(MainDiscount):
    cash = models.PositiveIntegerField(_('Cash Discount'))

    class Meta:
        verbose_name = _('Cash Discount')
        verbose_name_plural = _('Cash Discounts')

    def __str__(self):
        return f'{self.cash}'
<<<<<<< HEAD
=======
 
>>>>>>> 2e567137b12a8e3fc6bf62255974ab8998a032a4


class Percent(MainDiscount):
    percent = models.PositiveIntegerField(_('Percent Discount'))

    def clean(self):
        super().clean()
        if not 0 < self.percent < 100:
            raise exceptions.ValidationError(
                {'percent': 'only[1-99] is valid'}
            )

    class Meta:
        verbose_name = _('Percent Discount')
        verbose_name_plural = _('Percent Discounts')

    def __str__(self):
        return f'{self.percent}'


class CashCode(MainCodeDiscount):
    cash = models.PositiveIntegerField(_('Cash Code Discount'))

    class Meta:
        verbose_name = _('Cash Code Discount')
        verbose_name_plural = _('Cash Code Discounts')

    def __str__(self):
        return f'{self.code}->{self.cash}'

    def total_price(self, value):
        if self.cash > value:
            return value
        return value - self.cash

<<<<<<< HEAD
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.code = cash_code_generator.generate()
        super().save(force_insert=False, force_update=False, using=None,
                     update_fields=None)

=======
>>>>>>> 2e567137b12a8e3fc6bf62255974ab8998a032a4

class PercentCode(MainCodeDiscount):
    percent = models.PositiveIntegerField(_('Percent Code Discount'),
                                          validators=[validators.MaxValueValidator(
                                              limit_value=99
                                          ), validators.MinValueValidator(
                                              limit_value=1
                                          )])

    class Meta:
        verbose_name = _('Percent Code Discount')
        verbose_name_plural = _('Percent Code Discounts')

    def __str__(self):
        return f'{self.code}->{self.percent}'

    def total_price(self, value):
        result = (100 - self.percent) * value
        return result // 100

<<<<<<< HEAD
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.code = percent_code_generator.generate()
        super().save(force_insert=False, force_update=False, using=None,
                     update_fields=None)

=======
>>>>>>> 2e567137b12a8e3fc6bf62255974ab8998a032a4

class SpecificCash(Cash):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='specific_cash'
                             )

    class Meta:
        verbose_name = _('Specific Cash Discount')
        verbose_name_plural = _('Specific Cash Discounts')

    def __str__(self):
        return f'{self.cash} -> {self.user}'


class SpecificPercent(Percent):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='specific_percent'
                             )

    class Meta:
        verbose_name = _('Specific Percent Discount')
        verbose_name_plural = _('Specific Percent Discounts')

    def __str__(self):
        return f'{self.percent} -> {self.user}'
