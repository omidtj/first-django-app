from django.urls import path
from website.views import *
urlpatterns = [
    # ("url address","view")
    # just for test
    path('json-test', json_test),
    # like real project
    path('', home_view),
    path('about', about_view),
    path('contact', contact_view)
]