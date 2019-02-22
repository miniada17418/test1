from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from retailbloom import views

app_name = 'retailbloom1'


urlpatterns = [
    url(r'^$', views.modelFormUpload, name='upload_file'),
    url(r'^validate/(?P<pk>\d+)$',views.validate_page, name='validate_url_page'),
    url(r'^success/(?P<pk>\d+)$', views.upload_to_ftp, name='success_url'),
    url(r'^download-template/sample_file.csv$', views.download_template, name='download_template'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
