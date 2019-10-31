from django.shortcuts import render
from django.http import HttpResponse
import datetime
import json
import requests
import random
import os
from dotenv import load_dotenv
from .forms import PostForm
from django.http import HttpResponse


load_dotenv()

def index(request):
    """render main page"""
    return render(request, 'weats_template/main_page.html')

def register(request):
    """render register page"""
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
        return HttpResponse("Register success")
    else:
        form = PostForm()
    return render(request, 'weats_template/register.html', {'form': form})

def search(request):
    """render restaurant database"""
    today = datetime.datetime.today()
    weekday = today.strftime('%A')
    month = today.strftime('%b %d')
    city = request.GET.get('q')
    city_list = ["san francisco", "San Francisco", "Oakland", "oakland", "Berkeley", "berkeley"]
    if city in city_list:
        url = 'http://api.openweathermap.org/data/2.5/weather'
        api_key = os.getenv('WEATHER_API')
        params = {'appid': api_key, 'q': city, 'units': 'imperial'}
        r = requests.get(url, params=params)
        temp = r.json().get('main').get('temp')
        wind = r.json().get('wind').get('speed')
        str = "The weather today in {} is {}".format(city, temp)
        restaurant_list = random.sample(analyze(temp, city), k=8)
        return render(request, 'weats_template/search.html', {'str': str, 'temp': temp, 'wind': wind, 'restaurant_list': restaurant_list, 'city': city, "weekday": weekday, "month": month})
    else:
        return render(request, 'weats_template/main_page.html')

def restaurant(term, city):
    """retrieve restaurant database"""
    api_key = os.getenv('YELP_API')
    headers = {'Authorization': 'Bearer %s' % api_key}
    url='https://api.yelp.com/v3/businesses/search'
    params = {'term': term,'location': city, 'limit': 8}
    req=requests.get(url, params=params, headers=headers)
    return (req.json())

def analyze(temp, city):
    """analyze weather and give the recommend retaurant"""
    restaurant_list = []
    if temp >= 80:
        food_list = ['salad', 'ice cream', 'fruit', 'smothie', 'boba tea', 'acai']
        for food in food_list:
            result = restaurant(food, city)
            for business in result.get('businesses'):
                detail_list = []
                detail_list.append(business.get('name'))
                detail_list.append(business.get('url'))
                detail_list.append(business.get('price'))
                detail_list.append(business.get('rating'))
                detail_list.append(business.get('image_url'))
                restaurant_list.append(detail_list)
        return restaurant_list
    elif temp > 60 and temp < 80:
        food_list = ['BBQ', 'sea food', 'steak', 'burger', 'banh mi', 'burrito',
                    'ice cream', 'fruit', 'smothie', 'boba tea', 'acai', 'spagetti', 'hot dogs']
        for food in food_list:
            result = restaurant(food, city)
            for business in result.get('businesses'):
                detail_list = []
                detail_list.append(business.get('name'))
                detail_list.append(business.get('url'))
                detail_list.append(business.get('price'))
                detail_list.append(business.get('rating'))
                detail_list.append(business.get('image_url'))
                restaurant_list.append(detail_list)
        return restaurant_list
    elif temp <= 60:
        food_list = ['soup', 'ramen', 'pho', 'stew', 'spagetti', 'grill']
        for food in food_list:
            result = restaurant(food, city)
            for business in result.get('businesses'):
                detail_list = []
                detail_list.append(business.get('name'))
                detail_list.append(business.get('url'))
                detail_list.append(business.get('price'))
                detail_list.append(business.get('rating'))
                detail_list.append(business.get('image_url'))
                restaurant_list.append(detail_list)
        return restaurant_list
