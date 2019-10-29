from django.urls import path

from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.LeitorView.as_view(), name='leitores')
=======
    path('', views.LeitorView.as_view, name='leitores')
>>>>>>> 549ab3d2d6364d17f923887e1639f78f1d344584
]
