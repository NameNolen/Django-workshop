from django.conf.urls import url#include	
#from django.contrib import admin

from  .  import views

urlpatterns=[
     url(r'^$',views.IndexView.as_view(),name='index'),
     url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='detail'),
     url(r'^(?P<pk>[0-9]+)/results/$',views.ResultsView.as_view(),name='results'),
     url(r'^(?P<blog_id>[0-9]+)/vote/$',views.vote,name='vote'),
     url(r'^add/$', views.BlogCreate.as_view(), name='BlogCreate'),
     url(r'^update/(?P<pk>[0-9]+)/$', views.BlogUpdate.as_view(), name='BlogUpdate'),
     url(r'^delete/(?P<pk>[0-9]+)/$',views.BlogDelete.as_view(),name='BlogDelete'),
  ]
  
