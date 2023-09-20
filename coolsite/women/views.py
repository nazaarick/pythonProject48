from django.http import HttpResponse
from django.shortcuts import render
# модуль для хранения представлений
# Create your views here.
def index(Irequest):
    return HttpResponse('Главная страница основого приложения')
def categorys(Irequest):
    return HttpResponse('<h1> Ссылки по категориям </h1>')
def category(Irequest,cat_id):
    return HttpResponse(f'<h1> Номер категории - </h1>,<br> {cat_id}')