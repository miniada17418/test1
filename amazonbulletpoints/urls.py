from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from amazonbulletpoints import views

app_name = 'amzbullet'


urlpatterns = [
    url(r'^$', views.itemcodeUpload, name='amz_upload_file'),
    url(r'^download/(?P<file_name>.+)$', views.download_template, name='download_file')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
