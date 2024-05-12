from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from . models import Customer
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

# Create User and Customers

def account_page (request) :
    context = {}
    if request.POST:
        if 'register' in request.POST :
            context['register'] = True
            try:
                username = request.POST.get('username')
                email = request.POST.get('email')
                address = request.POST.get('address')
                phone = request.POST.get('phone')
                password = request.POST.get('password')

                # Create New User
                new_user = User.objects.create_user(
                username = username,
                email = email,
                password = password
                )
                
                # Through that user creating customer
                new_customer = Customer.objects.create(
                    user = new_user,
                    name = username,
                    phone = phone,
                    address = address
                )
                new_customer.save()

                success_msg = "User registered successfully"

                messages.success(request, success_msg)
            except Exception as e :
                print(e)
                error_msg = "Duplicate Username or Invalid credentials"
                messages.error(request, error_msg)
        
        if 'login' in request.POST :
            context['register'] = False
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username = username, password = password)

            if user :
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Invalid credentials")

    return render(request, 'user/account.html', context)

def signout (request) :

    logout(request)
    return redirect('home')