from django.urls import path
from langganan_app import views

urlpatterns = [
    path('',views.customers, name='customers'),
]
