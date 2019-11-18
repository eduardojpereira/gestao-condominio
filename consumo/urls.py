from django.urls import path
from . import views

urlpatterns = [
    path('', views.ConsumoView.as_view(), name='consumo'),
    path('<int:consumo_id>/', views.ConsumoViewId.as_view(), name='consumo-by-id')
]
