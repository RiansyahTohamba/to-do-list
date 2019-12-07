from django.conf.urls import url
from accounts import views
from django.contrib.auth import logout

urlpatterns = [
    url(r'^send_email$', views.send_login_email, name='send_login_email'),
    url(r'^login$', views.login, name='login'),
	url(r'^logout$', logout, {'next_page': '/'}, name='logout'),
]