from django.views import generic
from order import forms
from uuid import uuid4

from . import models
from order.models import Order


class ProductList(generic.ListView):
    queryset = models.BookObject.objects.all()
    template_name = 'product_list.html'
    context_object_name = 'products'

    @staticmethod
    def store_max_sales():
        max_sales_dict = Order.objects.get_max_sales()
        max_sales_gen = zip(max_sales_dict.values(), max_sales_dict.keys())
        max_sales = sorted(list(max_sales_gen), key=lambda x: x[0])
        if max_sales.__len__() > 5:
            tmp = max_sales[:5]
            return [x[1] for x in tmp]
        return [x[1] for x in max_sales]

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['max_sales'] = self.store_max_sales()
        return context


class ProductSearchList(generic.ListView):
    template_name = 'product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        que = self.request.GET.get('search')
        if not self.request.session.has_key('serial'):
            self.request.session['serial'] = uuid4().__str__()
        if que:
            return models.BookObject.objects.search_product(que)
        else:
            return models.BookObject.objects.all()


class ProductDetail(generic.DeleteView):
    queryset = models.BookObject.objects.all()
    template_name = 'one_product.html'
    context_object_name = 'book'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
