import datetime
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Order
from django.db import models
from django.db.models import Avg
from django.utils import timezone
from django.views.generic import View

def is_htmx_request(request):
    return request.headers.get('HX-Request') == 'true'

def order_screen(request):
    if request.method == 'POST':
        drink = request.POST.get('drink')
        order_number = ((Order.objects.count()) % 99) + 1
        order = Order.objects.create(drink=drink, order_number=order_number)
        return redirect('order_detail_screen', order_id=order.id)

    return render(request, 'order_screen.html', {
        'drinks': Order.DRINK_CHOICES,
        'is_htmx': is_htmx_request(request),
    })


def order_detail_screen(request, order_id):
    return render(request, 'order_detail_screen.html', {
        'order': get_object_or_404(Order, id=order_id),
        'is_htmx': is_htmx_request(request),
    })


def barista_screen(request):
    orders = Order.objects.filter(
        status__in=['ordered', 'ready']).order_by('created_at')

    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        action = request.POST.get('action')

        order = Order.objects.get(id=order_id)
        if action == 'ready':
            order.status = 'ready'
            order.total_preparing_time = (timezone.now() - order.created_at).seconds
        elif action == 'collected':
            order.status = 'collected'
        order.save()

        return redirect('barista_screen')

    return render(request, 'barista_screen.html', {'orders': orders, "is_htmx": is_htmx_request(request)})


def order_list_screen(request):
    not_ready_orders = Order.objects.filter(
        status='ordered').order_by('created_at')
    ready_orders = Order.objects.filter(status='ready').order_by('created_at')


    average_times = []

    for drink in Order.DRINK_CHOICES:
        orders = Order.objects.filter(drink=drink[0], total_preparing_time__isnull=False)[:25]
        avg_time = orders.aggregate(Avg('total_preparing_time'))['total_preparing_time__avg']
        avg_time_formatted = f"{int(avg_time) // 60}:{int(avg_time) % 60:02}" if avg_time else None
        if avg_time_formatted:
            average_times.append((drink[1], avg_time_formatted))

    return render(request, 'order_list_screen.html', {
        'not_ready_orders': not_ready_orders,
        'ready_orders': ready_orders,
        'is_htmx': is_htmx_request(request),
        "average_preparation_times":  average_times
    })
