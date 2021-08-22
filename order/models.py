from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _

from author.models import Author
from products.models import BookObject
<<<<<<< HEAD
from lib.shared_models import BaseModel
=======
from utils.shared_models import BaseModel
>>>>>>> 2e567137b12a8e3fc6bf62255974ab8998a032a4
from address.models import Address
from discount import models as dis_models

User = get_user_model()


class OrderManager(models.Manager):
    def get_max_sales(self):
        max_sales = {}
        que = self.get_queryset().filter(is_paid=True)
        for order in que:
            for detail in order.orders.all():
                if max_sales.get(detail.book) is not None:
                    max_sales[detail.book] += detail.quantity
                max_sales[detail.book] = detail.quantity
        return max_sales


class Order(BaseModel):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='orders',
                             blank=True,
                             null=True
                             )

    is_paid = models.BooleanField(_('paid'),
                                  default=False
                                  )

    payment_date = models.DateTimeField(_('payment date'),
                                        default=None,
                                        null=True,
                                        blank=True
                                        )

    price = models.PositiveIntegerField(_('price'),
                                        default=None,
                                        null=True,
                                        blank=True,
                                        )

    address = models.ForeignKey(Address,
                                on_delete=models.DO_NOTHING,
                                null=True,
                                blank=True
                                )

    cash_discount = models.ForeignKey(dis_models.CashCode,
                                      related_name='orders',
                                      on_delete=models.SET_NULL,
                                      blank=True,
                                      null=True
                                      )
    percent_discount = models.ForeignKey(dis_models.PercentCode,
                                         related_name='orders',
                                         on_delete=models.SET_NULL,
                                         null=True,
                                         blank=True
                                         )
    objects = OrderManager()

    def __str__(self):
        return self.user.__str__()

    class Meta:
        verbose_name = _('order')
        verbose_name_plural = _('orders')

    def total_price(self):
        return sum(map(lambda x: x.total_price(), self.orders.all()))

    def total_discount(self):
        return sum(map(lambda x: x.total_discount(), self.orders.all()))


class OrderDetail(BaseModel):
    book = models.ForeignKey(BookObject,
                             on_delete=models.CASCADE,
                             related_name='orders'
                             )

    order = models.ForeignKey(Order,
                              on_delete=models.CASCADE,
                              related_name='orders')

    quantity = models.IntegerField(_('quantity'),
                                   default=1
                                   )

    def total_price(self):
        return self.book.total_price() * self.quantity

    def total_discount(self):
        return self.book.get_discount() * self.quantity

    def __str__(self):
        return self.order.user.__str__()

    class Meta:
        verbose_name = _('order detail')
        verbose_name_plural = _('order detail')
