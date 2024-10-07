from django.urls import path
from website.views import *
urlpatterns = [
    # ("url address","view")
    path('', home_view),
    path('about', about_view),
    path('contact', contact_view)
]