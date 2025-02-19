from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from website.models import Contact
from website.forms import ContactForm,Newsletterform
from django.contrib import messages
# Create your views here.
def index_view (request):
    return render(request,'website/index.html') 

def about_view (request):
    return render(request,'website/about.html') 

def contact_view (request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            messages.add_message(request,messages.SUCCESS,'your ticket submited succesfully.')
        else:
            messages.add_message(request,messages.ERROR,"your ticket didn't submit")
    form = ContactForm() 
    return render(request,'website/contact.html',{'form':form}) 

def newsletter_view(request):
    if request.method == 'POST':
        form = Newsletterform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
