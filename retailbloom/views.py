from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views.generic import (TemplateView, ListView,
                                    DetailView, CreateView)
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.template import loader
from wsgiref.util import FileWrapper

# Create your views here.
from itertools import islice
import os
from .custom_code import *
from .forms import UploadFileForm
from .models import RetailBloom
from .smtplib_email_notification import *
from ftplib import FTP

ftp = FTP(host='ftp.dropshipadministrator2717.com')
ftp.login(user='dropshi8', passwd='E2f$145*')
ftp.cwd('/dropshipadministrator2717.com/channelsale2')

def placeFile(f):
    ftp.cwd('/dropshipadministrator2717.com/channelsale2')
    filename = f
    ftp.storbinary('STOR ' + filename, open(filename, 'rb'))
    ftp.rename(f,'retailbloom_price_and_qty.csv')
    ftp.quit()



#View that pulls in the file
def modelFormUpload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            #Function that saves the file with a unique name
            #formats the file to match the QBImportFile Table
            #Then uploads the file data to the database
            fileLocation = handle_uploaded_file(request.FILES['retailbloom_Report'],request.FILES['retailbloom_Report'].name)
            total_rows_in_file = sum(1 for line in request.FILES['retailbloom_Report'])
            fileName = request.FILES['retailbloom_Report'].name

            with open(fileLocation) as myfile:
                head = list(islice(myfile, 1))

            if head[0].rstrip() != 'ItemCode':
                return render(request, 'retailbloom/error.html', {'header':head[0]})

            obj = form.save(commit=False)
            obj.total_rows = total_rows_in_file
            obj.file_location = fileLocation
            obj.file_name = fileName
            obj.save()
            #saves the user and email address to the UploadFile table
            form.save()

            return redirect('bloom:validate_url_page', pk=obj.id)

    else:
        form = UploadFileForm()
    return render(request, 'retailbloom/submit.html', {
        'form': form
    })

def download_template(request):
    """
    When the Downloads a template file of the headers need to
    upload a file correctly to the tool
    """
    file_path = settings.MEDIA_ROOT +'/retailbloom/uploads/'+ "retailbloom_template_file.csv"
    wrapper = FileWrapper(open(file_path, 'rb'))
    response = HttpResponse(wrapper, content_type='text/csv')
    response['Content-Length'] = os.path.getsize(file_path)
    return response


def validate_page(request, pk):
    """
    validates that all the data in the file is uploaded correctly .
    """
    file_details = get_object_or_404(RetailBloom, pk=pk)
    total_rows_in_file = file_details.total_rows
    post_pk = file_details.pk
    fileName = file_details.file_name

    with open(file_details.file_location) as myfile:
        head = list(islice(myfile, 25))

    return render(request, 'retailbloom/validate.html', {'total_rows':total_rows_in_file, 'sample_file': head, 'upload_pk':post_pk, 'file_name':fileName} )

def upload_to_ftp(request, pk):

    file_details = get_object_or_404(RetailBloom, pk=pk)
    fileLocation = file_details.file_location
  
    os.chdir(settings.MEDIA_ROOT  +"/retailbloom/uploads/")

    try:
        placeFile(file_details.file_name)
        send_update_email(email_from='cyle@blackforestdecor.com',
                          email_to='cyle@blackforestdecor.com',
                          subject_line='Retail Bloom File Upload',
                          file_attachment=file_details.file_name,
                          message="RetailBloom's file was successfully poasted to the FTP site.")
    except Exception as e:
        print(e)

    return render(request, 'retailbloom/success.html')
