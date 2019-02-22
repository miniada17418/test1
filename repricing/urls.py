from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from repricing import views

app_name = 'reprice1'


urlpatterns = [
    url(r'^$', views.vendor_id_call, name='findVendorId'),
    url(r'^download/vendor(?P<supplierID>.+)template$', views.download_vendor_file, name='download_vendor_file')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
