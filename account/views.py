from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import LoginForm, RegisterForm


def home_view(request):
    if request.user.is_authenticated:
        return redirect('account:dashboard')
    return redirect('account:login')


def register_view(request):
    if request.user.is_authenticated:
        return redirect('account:dashboard')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم إنشاء الحساب بنجاح، يمكنك تسجيل الدخول الآن')
            return redirect('account:login')
    else:
        form = RegisterForm()

    return render(request, 'account/register.html', {'form': form, 'title': 'إنشاء حساب جديد'})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('account:dashboard')

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'تم تسجيل الدخول بنجاح')
            return redirect('account:dashboard')
    else:
        form = LoginForm()

    return render(request, 'account/login.html', {'form': form, 'title': 'تسجيل الدخول'})


def logout_view(request):
    logout(request)
    messages.info(request, 'تم تسجيل الخروج')
    return redirect('account:login')


@login_required
def profile_view(request):
    return render(request, 'account/profile.html', {'user': request.user})


@login_required
def dashboard_view(request):
    is_admin = request.user.is_staff or request.user.is_superuser
    return render(request, 'account/dashboard.html', {'user': request.user, 'is_admin': is_admin})