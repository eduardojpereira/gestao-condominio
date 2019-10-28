from django.urls import path

from . import views

urlpatterns = [
    path('', views.ApartamentoView.as_view(), name='apartamentos')
]
