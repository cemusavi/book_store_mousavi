import re
from datetime import datetime

from discount import models
from order.models import Order


class DiscountCheck:

    @staticmethod
    def discount_handler(code):
        percent_pattern = r'^bkino#\*prcnt.*'
        cash_pattern = r'^boki9@\*csh.*'
        if re.match(percent_pattern, code, re.I):
            return models.PercentCode
        elif re.match(cash_pattern, code, re.I):
            return models.CashCode
        return None

    def code_handler(self, request, action1, action2, action3, action4, action5):
        code = request.POST.get('code')
        order_id = request.POST.get('order_id')
        code_type = self.discount_handler(code)
        if code_type is None:
            return action1()
        order = Order.objects.get(id=order_id)
        discount_que = code_type.objects.filter(code=code)
        if not discount_que:
            return action2()
        discount = discount_que.first()
        if discount.expiration_date < datetime.now():
            return action3()
        if order in discount.orders.all() or request.user in discount.users.all():
            return action4()
        price = discount.total_price(order.price)
        order.price = price
        order.save()
        discount.orders.add(order)
        return action5(price)
