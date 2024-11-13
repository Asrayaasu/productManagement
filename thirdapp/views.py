from django.shortcuts import render
from .models import User
# Create your views here.
def login(request):
    return render(request,'thirdapp/login.html')
def signup(request):
    message = ''
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Implement the logic to create a new user
        #check whether user already exist
        userexit = User.objects.filter(email=email, password=password).exists()
        # If user already exist, display a message, else create a new user
        if userexit:
            message = 'Username already exist'
        else:
            # Create a new user
            user = User(email=email, password=password)
            user.save()
            message = 'User registered successfully'
    return render(request, 'thirdapp/signup',{'message':message})

def home(request):
    return render(request,'thirdapp/home')