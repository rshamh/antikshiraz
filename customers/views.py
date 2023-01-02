from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import User
from django.contrib.auth import login
from django.urls import reverse_lazy
from customers.forms import RegisterUserForm
# Function Based Views
from django.contrib.auth.decorators import login_required
# Class Based Views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

@login_required
def index(request):
    context ={
        'user': User.objects.all()
    }
    return render(request, 'customers/index.html')

def register(request):
    if request.method == "GET":
        context = {
                "form": RegisterUserForm,
            }
        return render(request, 'customers/register.html', context=context)

    elif request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return(reverse_lazy('customers:index'))



