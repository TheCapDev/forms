from urllib import request
from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader

from .models import Login
from .forms import LoginForm

# Create your views here.
def index(request):
    context = {}
    template = loader.get_template("index.html");
    return HttpResponse(template.render(context, request));

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
    
    if form.is_valid():
        form.save()
        print("Login info saved")
    else:
        print("Invalid Form")

    email = request.POST["email"];
    password = request.POST["password"];

    context = {"usersemail": email}
    template = loader.get_template("home.html");
    return HttpResponse(template.render(context, request));

def details(request):
    detailsList = Login.objects.all()
    context = {"details": detailsList}
    template = loader.get_template("details.html");
    return HttpResponse(template.render(context, request));