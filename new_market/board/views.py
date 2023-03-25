from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView
from .tasks import complete_order
from .models import Order
from datetime import datetime


# Главная страница - таблица заказов
class IndexView(TemplateView):
    template_name = 'board/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = Order.objects.all()
        return context


# Форма нового заказа
class NewOrderView(CreateView):
    model = Order
    fields = ['products']
    template_name = 'board/new.html'

    # после валидации формы, сохраняем объект
    # считаем его стоимость
    # и вызываем задачу "завершить заказ" через минуту после вызова
    def form_valid(self, form):
        order = form.save()
        order.cost = sum([prod.price for prod in order.products.all()])
        order.save()
        complete_order.apply_async([order.pk], countdown=60)
        return redirect('/')


# from django.http import HttpResponse
# from django.views import View
# from .tasks import hello, printer
#
#
# class IndexView(View):
#     def get(self, request):
#         printer.apply_async([10], countdown=5)
#         hello.delay()
#         return HttpResponse('Hello!')
