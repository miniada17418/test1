from django.shortcuts import render, redirect
from django.utils import timezone
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, DetailView
from django.views.generic.base import TemplateResponseMixin, View
from django.views.generic.edit import FormMixin
from django.views.generic.list import MultipleObjectMixin
from wsgiref.util import FileWrapper
from django.conf import settings

import os

from .forms import VendorIDForm
from .models import RepricingOMXData
from .custom_code import *


class FormListView(FormMixin, MultipleObjectMixin, TemplateResponseMixin, View):
    """
     A View which takes a queryset and filters it via a validated form submission
    """
    model = RepricingOMXData
    form_class = VendorIDForm
    template = 'repricing/vendoridsubmit.html'

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return self.render_to_response(self.get_context_data(form=form))

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        queryset = self.get_queryset()
        vendorNumber = form.cleaned_data['vendorID']
        object_list = RepricingOMXData.objects.filter(vendorID=vendorNumber)
        context = self.get_context_data(vendorID=object_list, form=form)
        return self.render_to_response(context)


def vendor_id_call(request):
    template_name = 'repricing/validate.html'
    model = RepricingOMXData
    form_class = VendorIDForm

    # if request.method == 'POST':
    form = form_class(request.POST)
    if form.is_valid():
        vendor_data = model.objects.filter(vendorID=form.cleaned_data['vendorID'])
        VendorID = form.cleaned_data['vendorID']
        total_rows = model.objects.all()
        row_count = total_rows.count()
    else:
        form = VendorIDForm()
        return render(request, template_name, {
        'form':form
    })

    context = {'form':form, 'VendorData': vendor_data, 'VendorID':VendorID, 'RowCount':row_count}

    return render(request, template_name, context)


def download_vendor_file(request,supplierID):
    """

    """
    template_name = 'repricing/validate.html'
    model = RepricingOMXData
    file_name = settings.MEDIA_ROOT + '/repricing/repricingvendor{}products.csv'.format(supplierID)
    xlsx_file_name = settings.MEDIA_ROOT + '/repricing/repricingvendor{}products.xlsx'.format(supplierID)

    render(request, template_name)

    formated_pd_file = convert_queryset_csv(model.objects.filter(vendorID=supplierID),file_name)
    xlsx_file_name = format_excel_file(formated_pd_file,xlsx_file_name)

    wrapper = FileWrapper(open(xlsx_file_name, 'rb'))
    response = HttpResponse(wrapper, content_type='application/vnd.ms-excel')
    response['Content-Length'] = os.path.getsize(xlsx_file_name)


    return response
