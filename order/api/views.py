from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from products.models import BookObject
<<<<<<< HEAD
from ..utils import order_handlers
from order import models
from order.utils.order_handlers import check_inventory
=======
from utils import order_handlers
from order import models
from utils.order_handlers import check_inventory
>>>>>>> 2e567137b12a8e3fc6bf62255974ab8998a032a4
from . import serializers


class UpdateOrderDetail(generics.UpdateAPIView):
    serializer_class = serializers.OrderDetailSerializer

    @staticmethod
    def controller(quantity):
        if quantity - 1 >= 0:
            return True
        return False

<<<<<<< HEAD
    @staticmethod
    def update_order_price(order):
        order.price = order.total_price()
        order.save()

=======
>>>>>>> 2e567137b12a8e3fc6bf62255974ab8998a032a4
    def patch(self, request, *args, **kwargs):
        detail = self.get_object()
        order = detail.order
        quantity = detail.quantity
        inventory = detail.book.inventory
        action = request.POST.get('action')
        if action == '-':
            if self.controller(detail.quantity):
                quantity -= 1
<<<<<<< HEAD
                if bool(quantity):
                    detail.quantity = quantity
                    detail.save()
                else:
                    detail.delete()
                    self.update_order_price(order)
                    return Response({
                        'quantity': 0,
                        'order_price': order.price,
                        'order_discount': order.total_discount(),
                        'count': order.orders.count()
                    }, status=status.HTTP_200_OK)

=======
                if not bool(quantity):
                    detail.delete()
                    return Response({
                        'quantity': 0,
                        'count': order.orders.count()
                    }, status=status.HTTP_200_OK)
                else:
                    detail.quantity = quantity
                    detail.save()
>>>>>>> 2e567137b12a8e3fc6bf62255974ab8998a032a4
        else:
            if check_inventory(quantity + 1, inventory):
                detail.quantity += 1
                detail.save()
<<<<<<< HEAD
        self.update_order_price(order)
=======
>>>>>>> 2e567137b12a8e3fc6bf62255974ab8998a032a4
        return Response({
            'quantity': detail.quantity,
            'detail_price': detail.total_price(),
            'detail_discount': detail.total_discount(),
<<<<<<< HEAD
            'order_price': order.price,
=======
            'order_price': order.total_price(),
>>>>>>> 2e567137b12a8e3fc6bf62255974ab8998a032a4
            'order_discount': order.total_discount(),
            'count': order.orders.count()
        }, status=status.HTTP_200_OK)

    def get_object(self):
        pk = self.request.POST.get('pk')
        return models.OrderDetail.objects.get(id=pk)


class AddOrderDetail(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        slug = request.POST.get('slug')
        order = order_handlers.get_order(self.request)
        book = get_object_or_404(BookObject, slug=slug)
        inventory = book.inventory
        order_detail = order.orders.filter(book=book)
        if order_detail:
            obj = order_detail.first()
            if check_inventory(obj.quantity, inventory):
                obj.quantity += 1
                obj.save()
        else:
            if check_inventory(1, inventory):
                models.OrderDetail.objects.create(order=order, book=book, quantity=1)
        count = order.orders.count()
        return Response({'count': count}, status=status.HTTP_200_OK)
