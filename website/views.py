from django.shortcuts import render
# آدرس شروع از فولدر تمپلیتس
def home_view(request):
    return render(request,'website/index.html')
def about_view(request):
    return render(request,'website/about.html')
def contact_view(request):
    return render(request,'website/contact.html')


  
