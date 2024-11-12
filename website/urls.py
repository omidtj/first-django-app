from django.urls import path
from website.views import *
app_name = 'website'
urlpatterns = [
    # ("url address","view")
    path('', home_view,name='index'),
    path('about', about_view,name='about'),
    path('newsletter', newsletter_view,name='newsletter'),
    path('contact', contact_view,name='contact')
]