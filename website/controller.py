#! /usr/bin/env python
# coding: utf-8

"""This file is the controller file: It contains all functions responsible of the research part of the app"""

from django.core.paginator import Paginator
from website.models import Product

def get_product_infos(product):
    """ Get product informations """
    id = product.id
    name = product.name
    nutriscore = product.nutriscore
    category = product.category
    stores = product.stores
    url = product.url
    image_url = product.image_url
    image_small_url = product.image_small_url
    energy = product.energy
    sugar = product.sugar
    salt = product.salt
    fat = product.fat
    saturated_fat = product.saturated_fat
    sodium = product.sodium
    proteins = product.proteins
    carbohydrates = product.carbohydrates
    infos = { 
        'id' : id,
        'name' : name,
        'nutriscore' : nutriscore,
        'category' : category,
        'stores' : stores,
        'url' : url,
        'image_url' : image_url,
        'image_small_url' : image_small_url,
        'energy' : energy,
        'sugar' : sugar,
        'salt' : salt,
        'fat' : fat,
        'saturated_fat' : saturated_fat,
        'sodium' : sodium,
        'proteins' : proteins,
        'carbohydrates' : carbohydrates,
    }
    return infos

def get_product(search):
    """ Retrieves first product matching the search, or None if no results"""
    try:
        product = Product.objects.filter(name__icontains=search)
        return get_product_infos(product[0])
    except IndexError:
        return None

def get_product_by_id(id):
    """ Retrieves first product matching the search, or None if no results"""
    try:
        product = Product.objects.filter(id=id)
        return get_product_infos(product[0])
    except IndexError:
        return None

def get_substitutes(product):
    """ Finds substitutes to product from same category """
    category = product['category']
    cats = category.split(", ")
    category_search = cats[-1]
    substitutes = Product.objects.filter(category__icontains=category_search).order_by("nutriscore")
    return substitutes

def save_product(user, product_id):
    """ Add product to user's favorites""" 
    product = Product.objects.filter(id=product_id)[0]
    user.product_set.add(product)
    return("Votre produit a bien été sauvegardé.")

def remove_saved_product(user, product_id):
    """ Remove product from user's favorites"""
    product = Product.objects.filter(id=product_id)[0]
    user.product_set.remove(product)   
    return("Votre produit a bien été retiré de votre liste des favoris.")

def get_saved_product(user):
    """ Retrieves products saved by user"""
    saved_product = user.product_set.all()
    return saved_product


