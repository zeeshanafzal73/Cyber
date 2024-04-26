from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import DocumentForm


# Create your views here.

def upload_file(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/')
        else:
            return render(request, 'upload_document.html', {'form': form})
    else:
        form = DocumentForm()
    return render(request, 'upload_document.html', {'form': form})
