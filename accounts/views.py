from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import login
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from accounts.forms import UserCreationForm, UserChangeForm
# Function Based Views
from django.contrib.auth.decorators import login_required
# Class Based Views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, UpdateView

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


class PasswordChange(PasswordChangeView):
    success_url = reverse_lazy('accounts:password_change_done')


class Profile(LoginRequiredMixin, UpdateView):
    model = User
    # fields = ['username', 'first_name', 'last_name', 'email']
    template_name = 'accounts/index.html'
    form_class =UserChangeForm
    success_url = reverse_lazy('accounts:index')
    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)