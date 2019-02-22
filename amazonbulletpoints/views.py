from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.template import loader
from django.conf import settings
from wsgiref.util import FileWrapper

# Create your views here.
import os

from .forms import ItemCodeUploadFile
from .customcode import file_upload

def itemcodeUpload(request):
    if request.method == 'POST':
        form = ItemCodeUploadFile(request.POST, request.FILES)
        if form.is_valid():
            #Function that saves the file with a unique name
            #formats the file to match the QBImportFile Table
            #Then uploads the file data to the database
            file_for_download = file_upload(request.FILES['itemCode'])

            #saves the user and email address to the UploadFile table
            form.save()

            NewFileName = file_for_download.split('/')

            return redirect('amz:download_file', file_name=NewFileName[-1])

    else:
        form = ItemCodeUploadFile()
    return render(request, 'amazonbulletpoints/uploadfile.html', {
        'form': form
    })

def download_template(request,file_name):
    """
    When the Downloads a template file of the headers need to
    upload a file correctly to the tool
    """
    file_path = settings.MEDIA_ROOT +'/amazon/uploads/'+ file_name
    wrapper = FileWrapper(open(file_path, 'rb'))
    response = HttpResponse(wrapper, content_type='text/csv')
    response['Content-Length'] = os.path.getsize(file_path)
    return response
