# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.conf import settings
from django.core.files.storage import FileSystemStorage

# def simple_upload(request):
#     if request.method == 'POST' and request.FILES['myfile']:
#         myfile = request.FILES['myfile']
#         fs = FileSystemStorage()
#         filename = fs.save(myfile.name, myfile)
#         uploaded_file_url = fs.url(filename)
#         return render(request, 'simple_upload.html', {'uploaded_file_url': uploaded_file_url})
#     return render(request, 'simple_upload.html')


from upload.models import UploadForm,Upload
from django.http import HttpResponseRedirect
from django.urls import reverse
import csv

from django.http import HttpResponse


import Child_Datasets
import Round_off
import Mean
import pandas as pd
import StringIO


# Create your views here.
def home(request):
    if request.method=="POST":
        file_upload = UploadForm(request.POST, request.FILES)       
        if file_upload.is_valid():
            file_upload.save()  
            pc,lpc,plasma=Child_Datasets.child_dataset()
            roundoffdata=Round_off.roundoff()
            meandata=Mean.findmean()
            pc.to_csv("PC_Compound.csv",index=False)
            lpc.to_csv("LPC_Compound.csv",index=False)
            plasma.to_csv("Plasmalogen_Compound.csv",index=False)
            roundoffdata.to_csv("RoundoffData.csv",index=False)
            meandata.to_csv("MeanValues.csv",index=False)
            return HttpResponseRedirect(reverse('success_page'))

    else:
        f=UploadForm()
    files=Upload.objects.all()
    return render(request,'home.html',{'form':f,'images':files})


def success_page(request):
	return render(request,'../templates/success_page.html')


import os, tempfile, zipfile
from wsgiref.util import FileWrapper
from django.conf import settings
import mimetypes


def download(request):
  path="/home/somit/elucidata"
  filename= path+"/"+"PC_Compound"+".csv" # Select your file here.
  download_name ="file1.csv"
  wrapper=FileWrapper(open(filename))
  content_type = mimetypes.guess_type(filename)[0]
  response=HttpResponse(wrapper,content_type=content_type)
  response['Content-Length']=os.path.getsize(filename)    
  response['Content-Disposition']="attachment; filename=%s"%download_name
  return response


# def download(request):
#     # Files (local path) to put in the .zip
#     # FIXME: Change this (get paths from DB etc)
#     filenames = ["/home/somit/elucidata/PC_Compound.csv", "/home/somit/elucidata/LPC_Compound.csv","/home/somit/elucidata/Plasmalogen_Compound.csv"]

#     # Folder name in ZIP archive which contains the above files
#     # E.g [thearchive.zip]/somefiles/file2.txt
#     # FIXME: Set this to something better
#     zip_subdir = "CompoundFiles"
#     zip_filename = "%s.zip" % zip_subdir

#     # Open StringIO to grab in-memory ZIP contents
#     s = StringIO.StringIO()

#     # The zip compressor
#     zf = zipfile.ZipFile(s, "w")

#     for fpath in filenames:
#         # Calculate path for file in zip
#         fdir, fname = os.path.split(fpath)
#         zip_path = os.path.join(zip_subdir, fname)

#         # Add file, at correct path
#         zf.write(fpath, zip_path)

#     # Must close zip for all contents to be written
#     zf.close()

#     # Grab ZIP file from in-memory, make response with correct MIME-type
#     resp = HttpResponse(s.getvalue(), mimetype = "application/x-zip-compressed")
#     # ..and correct content-disposition
#     resp['Content-Disposition'] = 'attachment; filename=%s' % zip_filename

#     return resp