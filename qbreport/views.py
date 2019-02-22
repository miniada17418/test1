from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import (TemplateView, ListView,
                                    DetailView, CreateView)
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.template import loader
from wsgiref.util import FileWrapper

# Create your views here.
import os
from .custom_code import *
from .forms import DocumenUpload
from .models import UploadFile, VendorNames, OMXOrderHistory, QBImportFile, NeedToAddVendorToDatabase


#View that pulls in the file
def modelFormUpload(request):
    if request.method == 'POST':
        form = DocumenUpload(request.POST, request.FILES)
        if form.is_valid():
            #Function that saves the file with a unique name
            #formats the file to match the QBImportFile Table
            #Then uploads the file data to the database
            UploadedFilePath = handle_uploaded_file(request.FILES['orderReport'])
            QBFile, vendorissue = formatfile(UploadedFilePath)

            if vendorissue:
                return redirect('qb:vendor_not_in_db')
            else:
                uploadToDatabase(QBFile)

            finialFormatedFile = join_Database()

            obj = form.save(commit=False)
            obj.userName = request.user
            obj.formatedFile = finialFormatedFile
            obj.save()

            #saves the user and email address to the UploadFile table
            form.save()

            NewFileName = finialFormatedFile.split('/')

            return redirect('qb:download_file', file_name=NewFileName[-1])

    else:
        form = DocumenUpload()
    return render(request, 'qbreport/uploadfile.html', {
        'form': form
    })


def send_file(request,file_name):
    """
    Send a file through Django without loading the whole file into
    memory at once. The FileWrapper will turn the file object into an
    iterator for chunks of 8KB.
    """
    render(request, 'qbreport/download.html')
    file_path = settings.MEDIA_ROOT +'/qbreports/uploads/'+ file_name
    #filename = 'media/qbreports/uploads/custom_qb_report.xlsx' # Select your file here.
    wrapper = FileWrapper(open(file_path, 'rb'))
    response = HttpResponse(wrapper, content_type='application/vnd.ms-excel')
    response['Content-Length'] = os.path.getsize(file_path)
    print("file pushed for download")
    return response

def download_template(request):
    """
    When the Downloads a template file of the headers need to
    upload a file correctly to the tool
    """
    file_path = settings.MEDIA_ROOT +'/qbreports/uploads/'+ "qb_report_template_file.csv"
    wrapper = FileWrapper(open(file_path, 'rb'))
    response = HttpResponse(wrapper, content_type='text/csv')
    response['Content-Length'] = os.path.getsize(file_path)
    return response


def vendor_not_in_datab(request):
    """
    if a vendor name is not in our database the user will be able to views
    the names of the vendors that need to be added to the Database.
    """

    vendors = NeedToAddVendorToDatabase.objects.all().values()

    return render(request, 'qbreport/new-vendor.html', {'vendors':vendors} )
