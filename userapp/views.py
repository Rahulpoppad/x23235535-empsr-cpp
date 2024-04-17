from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken")
                return redirect('register/')  # Adjusted the redirect URL
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already taken")
                return redirect('register/')  # Adjusted the redirect URL
            else:
                user_reg = User.objects.create_user(username=username, email=email, password=password)
                user_reg.save()
                messages.info(request, "Successfully created")
                return redirect('/')
        else:
            messages.info(request, "Password doesn't match")
            return redirect('register/')  # Adjusted the redirect URL

    return render(request, 'reg.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, "Login Success")
            return redirect('/')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('login/')

    return render(request, 'log.html')

def logout(request):
    # Use logout() from django.contrib.auth module, not authenticate.logout()
    from django.contrib.auth import logout
    logout(request)
    return redirect('/')
