from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import User
from django.contrib.auth import login
from django.urls import reverse_lazy
from accounts.forms import UserCreationForm
# Function Based Views
from django.contrib.auth.decorators import login_required
# Class Based Views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

@login_required
def index(request):
    context ={
    }
    return render(request, 'accounts/index.html')

def register(request):
    if request.method == "GET":
        context = {
                "form": UserCreationForm,
            }
        return render(request, 'accounts/register.html', context=context)

    elif request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('accounts:index')



