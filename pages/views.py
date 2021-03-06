from django.shortcuts import render, redirect
from django.shortcuts import render
from .forms import RegistrationForm, UserCreationForm, AuthenticationForm,User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from articles.models import Product

def index(request):
    new_articles = Product.objects.order_by('-date')[:3]
    context = {
        'articles': new_articles
    }
    return render(request, 'pages/index.html', context)


@login_required
def special(request):
    return HttpResponse("You are logged in !")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            #u = authenticate(username=user.username, password= user.password)
            login(request, user)
            return redirect('/')
    else:
        form = RegistrationForm()

    return render(request, 'pages/registration.html', {'form': form, })


def aboutus(request):
    return render(request, 'pages/aboutus.html')


def contactus(request):
    return render(request, 'pages/contactus.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'pages/login.html', {})

# Create your views here.
