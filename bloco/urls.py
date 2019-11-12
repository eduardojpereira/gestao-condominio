from django.urls import path
from bloco import views

urlpatterns = [
    path('', views.BlocoView.as_view(), name='blocos'),
]