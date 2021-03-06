from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

def register(request):
      if request.method == 'POST':
            print("I'm in POST")
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                  print("I'm validated")
                  form.save()
                  username = form.cleaned_data.get('username')
                  messages.success(request, f'Account created for {username}!. You can now login')
                  return redirect('login')
            else:
                  print("I'm not validated")
      else:
            print("I'm not in PPOST")      
            form = UserRegisterForm()
      return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
      return render(request, 'users/profile.html')