from django.shortcuts import render
from django.views.generic import View
from .models import *
from django.http import HttpResponse
import json


# Create your views here.


class IndexView(View):

	def get(self, request):
		return render(request, 'shop/index.html')


class ContactView(View):

	def get(self, request):
		return render(request, 'shop/contact.html')


class ProductPageView(View):

	counter = 0

	def get(self, request):
		product = [
					# {'img': 'products/img-1.jpg',
		           #  'status': 'p-status',
					# 'status_text': 'new',
		           #  'name': 'Green Dress with details',
		           #  'price': '$22.90'},
		           # {'img': 'products/img-2.jpg',
		           #  'status': 'p-status sale',
		           #  'status_text': 'sale',
		           #  'name': 'Yellow Maxi Dress',
		           #  'price': '$25.90'},
		           # {'img': 'products/img-3.jpg',
		           #  'status': 'p-status',
		           #  'status_text': 'new',
		           #  'name': 'One piece bodysuit',
		           #  'price': '$19.90'},
		           # {'img': 'products/img-4.jpg',
		           #  'status': 'p-status popular',
		           #  'status_text': 'popular',
		           #  'name': 'Blue Dress with details',
		           #  'price': '$35.50'}
		]

		for i in product:
			p = Product(img=i['img'], status=i['status'], status_text=i['status_text'], name=i['name'], price=i['price'])
			p.save()

		p = Product.objects.all().values()
		product = list(p)

		if not request.is_ajax():
			return render(request, 'shop/product-page.html', {'product': product})
		else:
			return HttpResponse(json.dumps({'product': product}), content_type='application/json')

	def post(self, request):
		global counter
		if request.is_ajax():
			message = f'ProductPageView: {counter}'
			counter += 1
			print(message)
		else:
			message = 'Not AJAX request'

		return HttpResponse(message)

