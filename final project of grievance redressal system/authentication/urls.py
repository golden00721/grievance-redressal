# Import necessary modules
from django.contrib import admin # Django admin module
from django.urls import path	 # URL routing
from authentication.views import * # Import views from the authentication app
from django.conf import settings # Application settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns # Static files serving

# Define URL patterns
urlpatterns = [
	path('', home ,name='home'),	 # Home page
	
	path('login/', login_page, name='login_page'), # Login page
	path('register/', register_page, name='register'), # Registration page
    path('home/', home_page, name='home'), # Registration page
    path('about/', about_page, name='about'),   #About Us
    path('feedback/', feedback_page, name='feedback'), #Feedback form
    path('process/', process, name='process'),
    path('contactus/', contactus_page, name='contactus'),
    path('complaint/', complaint_page, name='complaint'),
    path('index/', index_page, name='index'),
    path('thank_you/', thank_you, name='thank_you'),
]



