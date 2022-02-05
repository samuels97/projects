#from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
#    url(r'^$', views.index, name='index'),
#   url(r'^likepost/$', views.likePost, name='likepost'), #likepost view at /likepost
    path('/', views.index, name='index'),
    path('likepost/', views.likePost, name='likepost'),

]
