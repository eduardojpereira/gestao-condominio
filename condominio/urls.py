from django.urls import path

from . import views

urlpatterns = [
    path('', views.CondominioView.as_view(), name='condominios')
]