from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
# from django.core.mail import send_mail
# from django.conf import settings

# Create your views here.
def login_view(request):
    if not request.user.is_authenticated:
        form=AuthenticationForm() #get
        if request.method == 'POST':
            form = AuthenticationForm(request=request,data=request.POST) #post
            username= request.POST['username']
            password= request.POST['password']
            user_data = User.objects.get(Q(username__iexact=username) | Q(email__iexact=username))
            user = authenticate(username=user_data.username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
        context={'form':form}    
        return render(request,'accounts/login.html',context)
    else:
        return redirect('/')

#حتما باید لاگین باشه
@login_required    
def logout_view(request):
    logout(request)
    return redirect('/')

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
                form = UserCreationForm(request.POST)
                if form.is_valid():
                    username= request.POST['username']
                    password= request.POST['password1']
                    email= request.POST['email']
                    first_name= request.POST['first_name']
                    last_name= request.POST['last_name']
                    user = User.objects.create_user(username,email,password)
                    user.first_name = first_name
                    user.last_name = last_name
                    user.save()
                    return redirect('/')
        form =UserCreationForm()
        context={'form':form}
        return render(request,'accounts/signup.html',context)
    else:
        return redirect('/')

""" def forget_password_view(request):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['omid.tajer@gmail.com',]   
    send_mail( subject, message, email_from, recipient_list )  
    return redirect('/')   """      
