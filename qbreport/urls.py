from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from qbreport import views

app_name = 'qbreport1'


urlpatterns = [
    url(r'^$', views.modelFormUpload, name='upload_QB_File'),
    url(r'^download/(?P<file_name>.+)$', views.send_file, name='download_file'),
    url(r'^download-template/template.csv$', views.download_template, name='download_template'),
    url(r'^vendor-not-in-database/$', views.vendor_not_in_datab , name='vendor_not_in_db')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
