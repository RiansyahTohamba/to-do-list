from django.conf.urls import url
from lists import views

urlpatterns = [
    url(r'^new$', views.new_list, name='new_list'),
    url(r'^finish_task/(\d+)$', views.finish_task, name='finish_task'),
    url(r'^(\d+)/$', views.view_list, name='view_list'),
    url(r'^users/(.+)/$', views.my_lists, name='my_lists'),
]

