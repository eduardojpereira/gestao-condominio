from django.urls import path
from . import views

urlpatterns = [
    path('', views.ConsumoView.as_view(), name='consumo')
]
