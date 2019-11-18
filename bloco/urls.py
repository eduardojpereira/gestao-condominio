from django.urls import path
from bloco import views

urlpatterns = [
    path('', views.BlocoView.as_view(), name='blocos'),
    # path('<int:bloco_id>/', views.BlocoViewId.as_view(), name = 'blocos-by-id'),
]