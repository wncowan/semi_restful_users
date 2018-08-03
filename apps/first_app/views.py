# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
# from django.utils.crypto import get_random_string
from random import *
from time import gmtime, strftime
from .models import User

# Create your views here.
def index(request):
    users = User.objects.all()
    context = {
        "all_users" : users
    }
    return render(request, "first_app/index.html", context)

def new(request):
    return render(request, 'first_app/new.html')

def create(request):
    print('entered create')
    new_user = User.objects.create(
        first_name=request.POST['first_name'], 
        last_name=request.POST['last_name'], 
        email=request.POST['email'])
    print(new_user.first_name)
    print(new_user.last_name)
    print(new_user.email)
    print(new_user.id)
    return redirect('/users')

def edit(request, id):
    context = {
        "my_user" : User.objects.get(id=id)
    }
    return render(request, "first_app/edit.html", context)

def update(request, id):
    print('entered update!')
    my_user_id = id
    my_user_first_name = request.POST['first_name']
    my_user_last_name = request.POST['last_name']
    my_user_email = request.POST['email']
    b = User.objects.get(id=my_user_id)
    b.first_name = my_user_first_name
    b.last_name = my_user_last_name
    b.email = my_user_email
    b.save()
    print(my_user_id)
    return redirect('/users')

def show(request, id):
    print('entered show')
    context = {
        "my_user" : User.objects.get(id=id)
    }
    return render(request, "first_app/profile.html", context)

def destroy(request, id):
    return redirect("/")