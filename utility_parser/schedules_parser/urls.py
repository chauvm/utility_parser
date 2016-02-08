from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^home/', views.index, name='index'),
	url(r'^ice_rink/', views.ice_rink, name='ice_rink')
]