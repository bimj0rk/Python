from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from .forms import NameForm
def sign_up(request):
    if request.method == 'POST':
        print("Let's process data")
        form = UserCreationForm(request.POST)
        #form = NameForm(request.POST)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponse('A new user has been successfully registered!')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})