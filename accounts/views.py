from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CustomUserCreationForm, UsernameOrEmailAuthenticationForm,ForgotPasswordForm,SetNewPasswordForm
# Create your views here.

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UsernameOrEmailAuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                email = form.cleaned_data.get('email')
                user = authenticate(request, username=username, password=password, email=email)
                if user is not None:
                    login(request, user)
                    return redirect('/')
        form = UsernameOrEmailAuthenticationForm()
        context = {'form':form}
        return render(request,'accounts/login.html',context)
    else:
        return redirect('/')
    
def forgot_password_view(request):
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['username_or_email']
            # Store the user's ID in the session for verification
            request.session['reset_user_id'] = user.id
            return redirect('accounts:reset_password')
    else:
        form = ForgotPasswordForm()
    return render(request, 'accounts/forgot_password.html', {'form': form})

def reset_password_view(request):
    # Retrieve the user's ID from the session
    user_id = request.session.get('reset_user_id')
    if not user_id:
        return redirect('accounts:forgot_password')  # Redirect if no user ID is found

    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return redirect('accounts:forgot_password')  # Redirect if the user doesn't exist

    if request.method == 'POST':
        form = SetNewPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            # Clear the session after successful password reset
            del request.session['reset_user_id']
            return redirect('accounts:password_reset_complete')
    else:
        form = SetNewPasswordForm(user)
    return render(request, 'accounts/reset_password.html', {'form': form})

def password_reset_complete_view(request):
    return render(request, 'accounts/password_reset_complete.html')

@login_required 
def logout_view(request):
    logout(request)
    return redirect('/')

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request,messages.SUCCESS,'your account has been created.')
                return redirect('/')
            else:
                messages.add_message(request,messages.ERROR,'your account didnt create.')
        form = CustomUserCreationForm()
        context = {'form':form}
        return render(request,'accounts/signup.html',context)
    else:
        return redirect('/')
