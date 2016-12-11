from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index2$', views.index2, name='index2'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

]