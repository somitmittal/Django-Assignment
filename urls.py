from django.conf.urls import url
from . import views
from django.conf.urls import include

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^$', views.success_page, name = "success_page"),
    url(r'^success_page/$', views.success_page, name='success_page'), 
    url(r'^static/PC_Compound.csv', views.download,name='download')
]