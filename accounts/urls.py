from django.conf.urls import url
from accounts import views

#template URLs
app_name = 'accounts'

urlpatterns = [
    url(r'^login/$', views.user_login, name='user_login'),

]
