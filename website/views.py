from django.shortcuts import render
from django.http import HttpResponseRedirect
from website.forms import ContactForm,NewsletterForm
from django.contrib import messages
# آدرس شروع از فولدر تمپلیتس
def home_view(request):
    return render(request,'website/index.html')

def about_view(request):
    return render(request,'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.name = 'Unknown'
            obj.save()
            messages.add_message(request,messages.SUCCESS,'your ticket submited successfully')
        else:
            messages.add_message(request,messages.ERROR,'your ticket didnt submited!!')

    form = ContactForm() 
    context = {'form':form}
    return render(request,'website/contact.html',context)

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
    return HttpResponseRedirect('/')

       


 



  
