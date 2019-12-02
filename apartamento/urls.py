from django.urls import path

from . import views

urlpatterns = [
    path('', views.ApartamentoView.as_view(), name='apartamentos'),
    path('<int:apartamento_id>/', views.ApartamentoViewId.as_view(), name='apartamentos-by-id'),
]
