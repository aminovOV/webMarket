from celery import shared_task
from .models import Order


@shared_task
def complete_order(oid):
    order = Order.object.get(pk=oid)
    order.complete = True
    order.save()


# from celery import shared_task
# import time
#
#
# @shared_task
# def hello():
#     time.sleep(10)
#     print('hello')
#
#
# @shared_task
# def printer(n):
#     for i in range(n):
#         time.sleep(1)
#         print(i+1)
