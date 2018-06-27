from django.shortcuts import render
from django.core import serializers

from django.http import HttpResponse
from django.http import JsonResponse
# from .models import Combine, area_under_crop, crop_irrigated,source_irrigated
from .models import agro_chemical_abbreviations,agro_chemical_formulation,agro_chemical_products

def agro_chemical(request):
	if request.method=='GET':
		users = agro_chemical_abbreviations.objects.all().values()
		state=request.GET.get('shortcut')
		if(state is not None):
			users=users.filter(shortcut=state)
		state=request.GET.get('full_form')
		if(state is not None):
			users=users.filter(full_form=state)
		users_list = list(users)  # important: convert the QuerySet to a list object
		return JsonResponse(users_list, safe=False)

def agro_formulation(request):
	if request.method=='GET':
		users = agro_chemical_formulation.objects.all().values()  # or simply .values() to get all fields
		state=request.GET.get('shortcut')
		if(state is not None):
			users=users.filter(shortcut=state)
		state=request.GET.get('full_form')
		if(state is not None):
			users=users.filter(full_form=state)
		users_list = list(users)  # important: convert the QuerySet to a list object
		return JsonResponse(users_list, safe=False)

def agro_chemical_product(request):
	if request.method=='GET':
		users = agro_chemical_products.objects.all().values()
		a=request.GET.get('category')
		if(a is not None):
			users=users.filter(category=a)
		a=request.GET.get('mixture')
		if(a is not None):
			users=users.filter(mixture=a)
		a=request.GET.get('technical')
		if(a is not None):
			users=users.filter(technical=a)

		users_list = list(users)  
		return JsonResponse(users_list, safe=False)