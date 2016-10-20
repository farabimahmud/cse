from django.conf.urls import url
from CSEDAY2016 import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

]