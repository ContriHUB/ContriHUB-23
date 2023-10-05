"""contrihub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from decouple import config
from django.contrib import admin
# from django.conf.urls import
from django.urls import path, include, re_path

BASE_URL = config('BASE_URL', default=None)

basepatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('profile/', include('user_profile.urls')),
    path('project/', include('project.urls')),

    # this url is handled by social_django app under social-auth-app-django python library
    re_path(r'^oauth/', include('social_django.urls', namespace='social')),
]

if BASE_URL:
    urlpatterns = [
        path(str(BASE_URL), include(basepatterns))
    ]
else:
    urlpatterns = basepatterns
