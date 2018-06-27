"""data URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url,include
from django.urls import include,path
from polls import views as polls_views
# from django.conf.urls.defaults import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('area_prod/',polls_views.area_prod),
    path('area_under/',polls_views.area_under_crops),
    path('crop/',polls_views.crop_irrigated_csv),
    path('source/',polls_views.source_irrigated_csv),
    path('soil/',polls_views.soil_health),

    # # url(r'^polls/',polls_views.index),
    # path('abc/',polls_views.polls_create),


]

