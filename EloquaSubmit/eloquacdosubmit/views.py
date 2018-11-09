# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import forms
from django.shortcuts import render
from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def login_user(request):
    logout(request)
    username = password = 'test'
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/home/')
    return render(request, 'login.html')


@login_required(login_url='/login/')
def registerform(request):
 #if form is submitted
 if request.method == 'POST':
 	form = forms.RegisterForm(request.POST)
 	if form.is_valid():
 		return render(request, 'result.html', {
 'eloquacdoname': form.cleaned_data['eloquacdoname'],
 'hadooptablename': form.cleaned_data['hadooptablename'],
 'cecid': form.cleaned_data['cecid'],
 }) 
 else:
 #creating a new form
 	form = forms.RegisterForm()
 
 #returning form 
 return render(request, 'registerform.html', {'form':form});
