"""gestaocondominio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('docs/', include_docs_urls(title='Gestão de Condomínio',
                                    authentication_classes=[],
                                    permission_classes=[])),
    path('v1/apartamentos/', include('apartamento.urls')),
    path('v1/condominios/', include('condominio.urls')),
    path('v1/usuarios/', include('usuario.urls')),
    path('v1/leitores/', include('leitor.urls')),
    path('v1/blocos/', include('bloco.urls'))

]
