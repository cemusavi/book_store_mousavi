from order import models


def check_inventory(quantity, inventory):
    if inventory < quantity:
        return False
    return True


def fix_order_detail(order):
    details = [detail for detail in order.orders.all()]
    unique_ids = []
    for detail in reversed(details):
        if detail.book_id not in unique_ids:
            unique_ids.append(detail.book_id)
        else:
            detail.delete()


def get_order(request):
    if request.user.is_authenticated:
        order_que = models.Order.objects.filter(
            user=request.user,
            is_paid=False
        )
        order_1 = None
        order = None
        order_id = request.session.get('order_id')
        if order_id is not None:
            order_1 = models.Order.objects.get(id=order_id)
        if order_que:
            order = order_que.first()
            if order_1 is not None:
                order.orders.set(order_1.orders.all() | order.orders.all())
                fix_order_detail(order)
                order_1.delete()
                del request.session['order_id']
        if order is None:
            order = models.Order.objects.create(user=request.user)
    else:
        order_id = request.session.get('order_id')
        if order_id is not None:
            order = models.Order.objects.get(id=order_id)
        else:
            order = models.Order.objects.create()
            request.session['order_id'] = order.id
    return order
