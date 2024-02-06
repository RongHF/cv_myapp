#from django.conf.urls import url
from django.urls import re_path # django 5.0
from . import views

urlpatterns = [
    #url(r'^$', views.index, name="home"),
    #url(r'^test/$', views.home),
    re_path(r'^$', views.index, name="home"),
    re_path(r'^test/$', views.home),

    # url(r'^Results/', views.index, name='index'),
]

