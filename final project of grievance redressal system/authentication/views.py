# Import necessary modules and models
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *

# Define a view function for the home page
def home(request):
	return render(request, 'index.html')

# Define a view function for the login page
def login_page(request):
	# Check if the HTTP request method is POST (form submission)
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		# Check if a user with the provided username exists
		if not User.objects.filter(username=username).exists():
			# Display an error message if the username does not exist
			messages.error(request, 'Invalid Username')
			return redirect('/login/')
		
		# Authenticate the user with the provided username and password
		user = authenticate(username=username, password=password)
		
		if user is None:
			# Display an error message if authentication fails (invalid password)
			messages.error(request, "Invalid Password")
			return redirect('/login/')
		else:
			# Log in the user and redirect to the home page upon successful login
			login(request, user)
			return redirect('/home/')
	
	# Render the login page template (GET request)
	return render(request, 'login.html')

# Define a view function for the registration page
def register_page(request):
	# Check if the HTTP request method is POST (form submission)
	if request.method == 'POST':
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		# Check if a user with the provided username already exists
		user = User.objects.filter(username=username)
		
		if user.exists():
			# Display an information message if the username is taken
			messages.info(request, "Username already taken!")
			return redirect('/register/')
		
		# Create a new User object with the provided information
		user = User.objects.create_user(
			first_name=first_name,
			last_name=last_name,
			username=username
		)
		
		# Set the user's password and save the user object
		user.set_password(password)
		user.save()
		
		# Display an information message indicating successful account creation
		messages.info(request, "Account created Successfully!")
		return redirect('/register/')
	
	# Render the registration page template (GET request)
	return render(request, 'register.html')

def home(request):
	return render(request, 'index.html')

# Define a view function for the login page
def home_page(request):
	# Check if the HTTP request method is POST (form submission)
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		# Check if a user with the provided username exists
		if not User.objects.filter(username=username).exists():
			# Display an error message if the username does not exist
			messages.error(request, 'Invalid Username')
			return redirect('/login/')
		
		# Authenticate the user with the provided username and password
		user = authenticate(username=username, password=password)
		
		if user is None:
			# Display an error message if authentication fails (invalid password)
			messages.error(request, "Invalid Password")
			return redirect('/login/')
		else:
			# Log in the user and redirect to the home page upon successful login
			login(request, user)
			return redirect('/home/')
	
	# Render the login page template (GET request)
	return render(request, 'home.html')

def about_page(request):
	return render(request, 'about.html')

def feedback_page(request):
	if request.method == "POST":
		name = request.POST.get('name')
		email = request.POST.get('email')
		feedback = request.POST.get('feedback')
		
		feedback = Feedback.objects.create(name=name, email=email, feedback=feedback)
		feedback.save()
		
		# Redirect to a thank you page or any other appropriate page
		return redirect('thank_you')
	else:
		# Handle GET request (if any)
		return render(request, 'feedback.html')		

#flowchart process

def process(request):
	return render(request, 'process.html')

def contactus_page(request):
	return render(request, 'contactus.html')

def complaint_page(request):
    if request.method == "POST":
        description = request.POST.get("description")
    else:
        description = ""  # Default value if description is not provided

    complaint = Complaint.objects.create(description=description)
    complaint.save()

    return render(request, 'complaint.html')


def index_page(request):
	return render(request,'index.html')

def thank_you(request):
	return render(request,'thank_you.html')