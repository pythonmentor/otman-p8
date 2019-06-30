#! /usr/bin/env python
# coding: utf-8
""" Views file used for the website """

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import User

from .forms import SignUpForm
from datetime import datetime

from website.controller import *

User = get_user_model()


def paginator(request, objects_list):
    """ Paginator used for result and favorites views """
    paginator = Paginator(objects_list, 6)
    page = request.GET.get('page')
    objects = paginator.get_page(page)
    return objects

def index(request):
    """ Index page view """
    return render(request, 'website/index.html')

def redirection(request):
    """ Redirection to index after connect/disconnect """
    return redirect('index')

def signup(request):
    """ Sign up view """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user:
                login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'website/signup.html', {'form': form})

@login_required
def account(request):
    """ Access to account view """
    return render(request, 'website/account.html')

def result(request):
    """ View displaying results of a search """
    search = request.GET.get("search")
    product = get_product(search)
    if product is None:
        error = "Nous n'avons pas trouvé le produit que vous cherchez à substituer."
        return render(request, 'website/index.html', {'error' : error})
    else:
        substitutes_list = get_substitutes(product)
        substitutes = paginator(request, substitutes_list)
        return render(request, 'website/result.html', {'product' : product, 'substitutes' : substitutes})

def product(request, product_id):
    """ View displaying product infos """
    product = get_product_by_id(int(product_id))
    return render(request, 'website/product.html', {'product' : product})

@login_required
def favorites(request):
    """ Favorites page view """
    user = request.user
    favorites_list = get_saved_product(user)
    favorites = paginator(request, favorites_list)
    return render(request, 'website/favorites.html', {'favorites' : favorites})

@login_required
def save(request, product_id):
    """ View saving a product and displaying favorites page afterwards"""
    user = request.user
    text = save_product(user, product_id)
    favorites_list = get_saved_product(user)
    favorites = paginator(request, favorites_list)
    return render(request, 'website/favorites.html', {'text' : text, 'favorites': favorites})

@login_required
def remove(request, product_id):
    """ View removing a product and displaying favorites page afterwards"""
    user = request.user
    text = remove_saved_product(user, product_id)
    favorites_list = get_saved_product(user)
    favorites = paginator(request, favorites_list)
    return render(request, 'website/favorites.html', {'text' : text, 'favorites': favorites})

def contact(request):
    """ Contact page view """
    return render(request, 'website/contact.html')

def legal_terms(request):
    """ Legal terms page view """
    return render(request, 'website/legal_terms.html')