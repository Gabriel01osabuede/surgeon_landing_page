from django.shortcuts import render
from .import forms
from django.http import HttpResponseRedirect
from .models import subscriber
# Create your views here.



def home(request):
    form = forms.SubscriberForm

    if request.method == 'POST':
        form = forms.SubscriberForm(request.POST)

        if form.is_valid():

            form.save(commit=True)
            return HttpResponseRedirect('/')


    return render(request, 'surgeonapp/index.html', {'form': form})


