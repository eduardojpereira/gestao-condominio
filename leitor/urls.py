from django.urls import path

from . import views

urlpatterns = [
    path('', views.LeitorView.as_view(), name='leitores')
]
