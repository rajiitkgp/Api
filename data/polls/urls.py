from django.urls import path
from django.conf.urls import url
from polls import views

urlpatterns = [
    url(r'^index/$',"polls.views.index" ),
    url(r'^polls_create/$', "polls.views.polls_create"),
    # path('', views.index, name='index'),
    # path('',views.polls_create,name='polls_create')

]