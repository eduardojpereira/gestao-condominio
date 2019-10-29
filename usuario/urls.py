from django.urls import path

from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.UsuarioView.as_view(), name='usuarios')
=======
    path('', views.UsuarioView.as_view, name='usuarios')
>>>>>>> 549ab3d2d6364d17f923887e1639f78f1d344584
]
