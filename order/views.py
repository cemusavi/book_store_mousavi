from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.db import transaction
from django.utils import datetime_safe

<<<<<<< HEAD
from .utils import order_handlers
=======
from utils import order_handlers
>>>>>>> 2e567137b12a8e3fc6bf62255974ab8998a032a4
from address.forms import AddressForm
from address.models import Address
from discount.forms import CodeDiscountForm
from . import models


class OrderCreate(generic.View):

    def get(self, request):
<<<<<<< HEAD
        order = order_handlers.get_order(request)
        order.price = order.total_price()
        order.save()
        if order.cash_discount:
            order.cash_discount.orders.remove(order)
        if order.percent_discount:
            order.percent_discount.orders.remove(order)
        context = {
            'order': order,
=======
        context = {
            'order': order_handlers.get_order(request),
>>>>>>> 2e567137b12a8e3fc6bf62255974ab8998a032a4
        }
        return render(request, 'order.html', context)


class ControlOrder(generic.View):

    def post(self, request):
        return self.get_success_url()

    @staticmethod
    def get_success_url():
        return redirect('order:order-create')


class ConfirmOrder(LoginRequiredMixin, generic.View):
    def _get_order(self, pk):
        order = get_object_or_404(models.Order, id=pk)
        if order.user is None:
            order.user = self.request.user
        return order

    def _check_order_details(self, pk):
        order = self._get_order(pk)
        if not order.is_paid:
            if order.orders.exists():
                return True
        return False

    @staticmethod
    def _update_book_inventory(order):
        with transaction.atomic():
            for detail in order.orders.all():
                book = detail.book
                book.inventory -= detail.quantity
                book.save()

    def get(self, request, pk):
        if not self._check_order_details(pk):
            return redirect('order:order-create')
        order = self._get_order(pk)
        if order.price is None:
            order.price = order.total_price()
            order.save()
        form = AddressForm()
        discount_form = CodeDiscountForm()
        context = {
            'order': order,
            'form': form,
            'discount_form': discount_form
        }
        return render(request, 'confirm_order.html', context)

    def post(self, request, pk):
        if not self._check_order_details(pk):
            return redirect('order:order-create')
        order = self._get_order(pk)
<<<<<<< HEAD
=======
        self._update_book_inventory(order)
        order.is_paid = True
        order.payment_date = datetime_safe.datetime.now()
>>>>>>> 2e567137b12a8e3fc6bf62255974ab8998a032a4
        form = AddressForm(request.POST)
        data = list(form.data.values())
        city, exact_address = data[-2], data[-1]
        if city and exact_address:
            address = Address.objects.create(
                user=request.user,
                city=city,
                exact_address=exact_address
            )
            order.address = address
        else:
<<<<<<< HEAD
            addresses = Address.objects.filter(id=request.POST.get('address'))
            if not addresses:
                return redirect('order:confirm-order', pk)
            order.address = addresses.first()
        self._update_book_inventory(order)
        order.is_paid = True
        order.payment_date = datetime_safe.datetime.now()
        if order.percent_discount:
            order.percent_discount.users.add(request.user)
        if order.cash_discount:
            order.cash_discount.users.add(request.user)
=======
            address = Address.objects.get(id=int(request.POST.get('address')))
            order.address = address
>>>>>>> 2e567137b12a8e3fc6bf62255974ab8998a032a4
        order.save()
        return render(request, 'congratulations.html')


class OrderHistory(LoginRequiredMixin, generic.ListView):
    template_name = 'order_history.html'
    model = models.Order

<<<<<<< HEAD
    def get_context_data(self,*args, **kwargs):
=======
    def get_context_data(self, *, object_list=None, **kwargs):
>>>>>>> 2e567137b12a8e3fc6bf62255974ab8998a032a4
        context = super().get_context_data()
        done_orders = models.Order.objects.filter(
            user=self.request.user,
            is_paid=True
        ).order_by('-payment_date')
        in_complete_order = models.Order.objects.get(
            user=self.request.user,
            is_paid=False
        )
        context['done_orders'] = done_orders
        context['in_complete_order'] = in_complete_order
        return context
