"""
URL configuration for linguacards project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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

from django.contrib import admin  # Imports the Django admin module (Importuje moduł admina Django)
from django.urls import path, include  # Imports path and include functions to combine URL routers from apps (Importuje funkcje path i include do łączenia routerów URL z aplikacji)

urlpatterns = [  # Defines the main project URL routing patterns (Definiuje główne wzorce routingu adresów URL projektu)
    path('admin/', admin.site.urls),  # Maps the admin URL path to Django's admin site (Mapuje ścieżkę URL admina do panelu administracyjnego Django)
    path('', include('vocabulary.urls')),  # Includes all URL patterns from our vocabulary app at the root website level (Dołącza wszystkie wzorce URL z naszej aplikacji vocabulary na głównym poziomie strony)
]