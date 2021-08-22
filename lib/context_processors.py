from order.utils import order_handlers


def order_detail_count(request):
    order = order_handlers.get_order(request)
    count = order.orders.count()
    return {
        'count': count
    }


