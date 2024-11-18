from django.shortcuts import render

# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        msg=f'{request.user.get_full_name()} is authenticated'
    else :
        msg = 'user is not authenticated' 
    context = {'msg':msg}       
    return render(request,'accounts/login.html',context)

# def logout_view(request):
#     return render(request,'accounts/logout.html')

def signup_view(request):
    return render(request,'accounts/signup.html')

