from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import *

def paginate(cupons, request):
	paginator = Paginator(cupons, 48)
	page_number = request.GET.get('page', 1)
	page = paginator.get_page(page_number)

	is_paginated = page.has_other_pages()
	if page.has_previous():
		prev_url =f'?page={page.previous_page_number()}'
	else:
		prev_url = ''

	if page.has_next():
		next_url =f'?page={page.next_page_number()}'
	else:
		next_url = ''
	pag = [page, is_paginated, next_url, prev_url]
	return pag

class CampaignsDetailMixin:
	model = None
	template = None

	def get(self, request, pk):
		obj = get_object_or_404(self.model, id=pk)
		cupons = Cupons.objects.filter(campaigns=obj)
		pag = paginate(cupons, request)
		return render(request, f'botpromokotapp/{self.template}.html', {
																			"cupons": pag[0],
																			"is_paginated": pag[1],
																			"next_url": pag[2],
																			"prev_url": pag[3],
																			"title": obj.name
																			})

class CategoriesDetailMixin:
	model = None
	template = None

	def get(self, request, pk):
		obj = get_object_or_404(self.model, id=pk)
		cupons = Cupons.objects.filter(categories=obj)
		pag = paginate(cupons, request)
		return render(request, f'botpromokotapp/{self.template}.html', {
																			"cupons": pag[0],
																			"is_paginated": pag[1],
																			"next_url": pag[2],
																			"prev_url": pag[3],
																			"title": obj.name
																			})

class TypesMixin:
	types = None
	template = None

	def get(self, request):
		cupons = Cupons.objects.filter(types=self.types)
		pag = paginate(cupons, request)
		return render(request, f'botpromokotapp/{self.template}.html', {
																			"cupons": pag[0],
																			"is_paginated": pag[1],
																			"next_url": pag[2],
																			"prev_url": pag[3],
																			})	
class ObjMixin:
	model = None
	template = None

	def get(self, request):
		

		obj = self.model.objects.all()
		return render(request, f'botpromokotapp/{self.template}.html', {self.model.__name__.lower(): obj})