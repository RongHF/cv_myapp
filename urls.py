from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="home"),
    url(r'^test/$', views.home),

    # url(r'^Results/', views.index, name='index'),
]

