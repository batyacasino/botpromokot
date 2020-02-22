from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from .models import *
from .bd_reload import *
from .utils import *


class Index(TypesMixin, View):
	types=2
	template = 'index'


class FreeShipping(TypesMixin, View):
	types=1
	template = 'free_shipping'


class GiftToOrder(TypesMixin, View):
	types=3
	template = 'gift_to_order'


class CampaignDetail(CampaignsDetailMixin, View):
	model = Campaigns
	template = 'campaign_detail'


class CategoriesDetail(CategoriesDetailMixin, View):
	model = Categories
	template = 'categories_detail'


def del_and_reload_db(request):
	del_db()
	Order_discount = Types.objects.get(id=2)
	cupons = Cupons.objects.filter(types=Order_discount)
	return render(request, 'botpromokotapp/index.html', {
															"cupons": cupons,
														})

def campaigns(request):
	del_db()
	campaigns = Campaigns.objects.all()
	return render(request, 'botpromokotapp/campaigns.html', {
																"campaigns": campaigns,
																})
def categories(request):
	categories = Categories.objects.all()
	return render(request, 'botpromokotapp/categories.html', {
																"categories": categories
																})

def sitemap(request):
    return render(request, 'botpromokotapp/sitemap.xml')

def robots(request):
    return render(request, 'botpromokotapp/robots.txt')