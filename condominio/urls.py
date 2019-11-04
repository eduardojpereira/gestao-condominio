from django.urls import path

from . import views

urlpatterns = [
    path('', views.CondominioView.as_view(), name='condominios'),
    path('<int:condominio_id>/', views.CondominioViewId.as_view(), name='condominios-by-id'),
]