"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from pybo.views import base_views 
# include: 내부 파라미터(pybo폴더의 urls.py파일)의 매핑 정보를 읽어서 처리하라는 의미
# Django의 기본구조는 Browser에서 온 호출을 urls에 맞춰 매핑하고, urls는 전달받은 정보를 다시 views에 매핑하려 return하는 형태임.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')),
    path('common/', include('common.urls')),
    path('', base_views.index, name='index'),
]
