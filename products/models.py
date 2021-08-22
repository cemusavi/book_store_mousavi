<<<<<<< HEAD
from datetime import datetime

=======
>>>>>>> 2e567137b12a8e3fc6bf62255974ab8998a032a4
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models import Q

from author.models import Author
<<<<<<< HEAD
from lib.shared_models import BaseModel
from lib.rename_files import rename_product_pic
=======
from utils.shared_models import BaseModel
from utils.rename_files import rename_product_pic
>>>>>>> 2e567137b12a8e3fc6bf62255974ab8998a032a4
from discount import models as dis_models


class Genre(BaseModel):
    title = models.CharField(_('Title'),
                             max_length=30
                             )

    class Meta:
        verbose_name = _('Genre')
        verbose_name_plural = _('Genres')

    def __str__(self):
        return self.title


class Book(BaseModel):
    title = models.CharField(_('Title'),
                             max_length=30
                             )

    genre = models.ManyToManyField(Genre,
                                   related_name='genres'
                                   )

    author = models.ForeignKey(Author,
                               on_delete=models.SET_NULL,
                               related_name='books',
                               blank=True,
                               null=True
                               )

    isbn = models.IntegerField(_('ISBN'))

    def __str__(self):
        return f'{self.author} -> {self.title}'


class BookObjectManager(models.Manager):
    def search_product(self, que):
        look_up = Q(book__author__first_name__icontains=que) | Q(
            book__author__last_name__icontains=que) | Q(
            book__title__icontains=que) | Q(book__genre__title__icontains=que)
        return self.get_queryset().filter(look_up).distinct()


class BookObject(BaseModel):
    book = models.ForeignKey(Book,
                             on_delete=models.CASCADE,
                             related_name='books')

    price = models.PositiveIntegerField(_('Price'))
    release_date = models.DateField(_('Release date'))
    inventory = models.PositiveIntegerField(_('Inventory'),
                                            default=0
                                            )
    slug = models.SlugField(_('Slug'),
                            max_length=40,
                            blank=True,
                            null=True,
                            unique=True
                            )
    cover = models.ImageField(_('cover'),
                              upload_to=rename_product_pic,
                              default='products/book_pictures/one.jpg'
                              )
    percent_discount = models.ForeignKey(dis_models.Percent,
                                         related_name='books',
                                         on_delete=models.SET_NULL,
                                         null=True,
                                         blank=True
                                         )
    cash_discount = models.ForeignKey(dis_models.Cash,
                                      related_name='books',
                                      on_delete=models.SET_NULL,
                                      null=True,
                                      blank=True
                                      )
    objects = BookObjectManager()

    class Meta:
        verbose_name = _('Book Instance')
        verbose_name_plural = _('Book Instances')

    def __str__(self):
        return f'{self.book.title} {self.release_date}'

    def percent_reduce(self):
<<<<<<< HEAD
        if self.percent_discount.expiration_date > datetime.now():
            res = (100 - self.percent_discount.percent) * self.price
            return res // 100
        self.percent_discount.delete()
        return self.price

    def cash_reduce(self):
        if self.cash_discount.expiration_date > datetime.now():
            return self.price - self.cash_discount.cash
        self.cash_discount.delete()
        return self.price

=======
        res = (100 - self.percent_discount.percent) * self.price
        return res // 100

    def cash_reduce(self):
        return self.price - self.cash_discount.cash

 
>>>>>>> 2e567137b12a8e3fc6bf62255974ab8998a032a4
    def total_price(self):
        if self.percent_discount:
            return self.percent_reduce()
        elif self.cash_discount:
            return self.cash_reduce()
        return self.price

    def get_discount(self):
        return self.price - self.total_price()
