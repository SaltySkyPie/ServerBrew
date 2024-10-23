from django.urls import path
from . import views

urlpatterns = [
    path('order/', views.order_screen, name='order_screen'),
    path('order/<uuid:order_id>/', views.order_detail_screen, name='order_detail_screen'),
    path('barista/', views.barista_screen, name='barista_screen'),
    path('order-list/', views.order_list_screen, name='order_list_screen'),
]
