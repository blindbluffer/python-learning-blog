from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'groups'

"""urlpatterns = [
    url(r'^$',views.ListGroups.as_view(),name='all'),
    url(r'^new/$',views.CreateGroup.as_view(),name='create'),
    url(r'posts/in/(?P<slug>[-\w]+)/$',views.SingleGroup.as_view(),name='single'),
    url(r'join/(?P<slug>[-\w]+)/$',views.JoinGroup.as_view(),name='join'),
    url(r'leave/(?P<slug>[-\w]+)/$',views.LeaveGroup.as_view(),name='leave'),

]"""

urlpatterns = [
    path('',views.ListGroups.as_view(),name='all'),
    path('new/',views.CreateGroup.as_view(),name='create'),
    path('posts/in/<slug:slug>/',views.SingleGroup.as_view(),name='single'),
    path('join/<slug:slug>/',views.JoinGroup.as_view(),name='join'),
    path('leave/<slug:slug>/',views.LeaveGroup.as_view(),name='leave'),

]
