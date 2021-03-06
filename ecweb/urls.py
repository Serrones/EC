from django.conf.urls import include, url

from . import views


urlpatterns = [
    url(r'^$', views.home_dashboard),
    url(r'^dashboard/', views.home_dashboard, name='home_dashboard'),
    url(r'^student/', views.user_detail, name='user_detail'),
    url(r'^classroom/$', views.classroom_view, name='classroom_view'),
    url(r'^logout/$', views.logout_view),
    url(r'^class/$', views.classes_view, name='classes_views'),
    url(r'^class/(?P<class_id>[0-9]+)/attendances/$', views.class_view, name='class_view'),
]
