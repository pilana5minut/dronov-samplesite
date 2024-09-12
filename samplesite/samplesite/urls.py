"""samplesite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

Виды функций
    1. Добавьте импорт: from my_app import views
    2. Добавьте URL в urlpatterns: path('', views.home, name='home')
Представления на основе классов
    1. Добавьте импорт: from other_app.views import Home
    2. Добавьте URL в urlpatterns: path('', Home.as_view(), name='home')
Включение другого URLconf
    1. Импортируем функцию include(): from django.urls import include, path
    2. Добавьте URL в urlpatterns: path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('bboard/', include('bboard.urls')),
    path('admin/', admin.site.urls),
]
