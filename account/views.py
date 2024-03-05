from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView
from django.contrib.auth import get_user_model, logout, authenticate, login

from .forms import SignUpForm, LoginForm

User = get_user_model()


class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'accaount/signup.html'
    success_url = '/'

def login_view(request):
    form = LoginForm
    if request.method == 'POST':
        phone = request.POST['phone']
        password = request.POST['password']
        user = authenticate(request, phone=phone, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('app:home'))

    return render(request, 'accaount/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect(reverse('account:login'))
