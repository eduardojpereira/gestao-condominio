from django.urls import path

from apartamento import views

urlpatterns = [
    path('', views.ApartamentoView.as_view(), name='apartamentos')
]
