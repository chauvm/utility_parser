from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^new_post/$', views.new_post, name='blog-views-new'),
	url(r'^(?P<slug>[\w\-]+)/$', views.post, name='blog-views-post'),
	
]