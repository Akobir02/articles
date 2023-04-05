from turtle import pd
from urllib import request
# import requests
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse
from django.template import loader

from .forms import CustomUserCreationForm
from django.views.generic import TemplateView

class About(TemplateView):
    template_name= 'about.html'
class Contact(TemplateView):
    template_name= 'contact.html'
class Index(TemplateView):
    template_name= 'index.html'
# # def testing(request):
# #   template = loader.get_template('weze.html')
#   return HttpResponse(template.render())
def home(request):
    return render(request,'home.html')
def landing_page(request):
    return render(request,'landing_page.html')
def dollor(request):
    import requests
    url = 'https://v6.exchangerate-api.com/v6/YOUR-API-KEY/latest/USD'


    response = requests.get(url).json()
    dollor_info={
        'rates' : response["conversion_rates"]["USD"]
    }
    context={'name':dollor_info}
    return render(request,'weze.html',context)

def weather(request):
    import requests
    api_key = "e350eb73ae05d393946e11ea020b13ff"
    root_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = "Samarkand"
    # res = requests.get(url.format(city)).json()
    url = f"{root_url}appid={api_key}&q={city_name}"
    r = requests.get(url).json()
    city_info={
        'city': city_name,
        'temp': r["main"]["temp"]
    }
    context = {'info': city_info}
    return render(request,'weze.html',context)
# def weather2(request):
#     import requests
#     appid = 'e350eb73ae05d393946e11ea020b13ff'
#     lat = '39.647099'
#     lon = '66.960289'
#     units = 'metric'
#     response = requests.get(
#     url='https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}&units={}'.format(lat, lon, appid,
#                                                                                                      units))
#     temprature = response.json()['main']['temp_max']
#     nome = {'info':temprature}
#     return render(request,'weze.html',nome)
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
def log_in(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request,'login.html', {"form":form})
def log_out(request):
    logout(request)
    return redirect('landing_page')
def password_change(request):
    return render(request,'password_change_done.hmtl')
def password_reset(request):
    return render(request, 'registration/password_reset_done.html')

