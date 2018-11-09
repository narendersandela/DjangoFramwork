# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.db import models
from blog.models import posts

def home(request):
	return render(request, 'index.html')

def index(request):
	return render(request, 'index1.html')
 
