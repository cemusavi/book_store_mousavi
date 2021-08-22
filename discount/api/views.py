import re
from datetime import datetime

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from discount import models
from order.models import Order


class ApplyDiscount(generics.UpdateAPIView):
<<<<<<< HEAD
=======

>>>>>>> 2e567137b12a8e3fc6bf62255974ab8998a032a4
    @staticmethod
    def discount_handler(code):
        percent_pattern = r'^bkino#\*prcnt.*'
        cash_pattern = r'^boki9@\*csh.*'
        if re.match(percent_pattern, code, re.I):
            return models.PercentCode
        elif re.match(cash_pattern, code, re.I):
            return models.CashCode
        return None

    def patch(self, request, *args, **kwargs):
        code = request.POST.get('code')
        order_id = request.POST.get('order_id')
<<<<<<< HEAD
        code_type = self.discount_handler(code)
        if code_type is None:
            return Response({'result': 'fake'}, status=status.HTTP_403_FORBIDDEN)
        order = Order.objects.get(id=order_id)
        discount_que = code_type.objects.filter(code=code)
        if not discount_que:
            return Response({'result': 'not found'}, status=status.HTTP_404_NOT_FOUND)
        discount = discount_que.first()
        if discount.expiration_date < datetime.now():
            return Response({'result': 'expired'}, status=status.HTTP_402_PAYMENT_REQUIRED)
        if order in discount.orders.all() or request.user in discount.users.all():
            return Response({'result': 'used'}, status=status.HTTP_400_BAD_REQUEST)
        price = discount.total_price(order.price)
        order.price = price
        order.save()
        discount.orders.add(order)
        return Response({'price': price}, status=status.HTTP_200_OK)
=======
        order = Order.objects.get(id=order_id)
        code_type = self.discount_handler(code)
        if code_type is None:
            return Response({'result': 'fake'}, status=status.HTTP_403_FORBIDDEN)
        discount_que = code_type.objects.filter(code=code)
        if discount_que:
            discount = discount_que.first()
            if discount.expiration_date < datetime.now():
                return Response({'result': 'expired'}, status=status.HTTP_402_PAYMENT_REQUIRED)
            if discount.users.filter(id=order.user_id).exists():
                return Response({'result': 'used'}, status=status.HTTP_400_BAD_REQUEST)
            price = discount.total_price(order.price)
            order.price = price
            discount.users.add(order.user)
            print(discount.users.all())
            order.save()
            return Response({'price': price}, status=status.HTTP_200_OK)
        return Response({'result': 'not found'}, status=status.HTTP_404_NOT_FOUND)
>>>>>>> 2e567137b12a8e3fc6bf62255974ab8998a032a4
