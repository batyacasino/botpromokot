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


class Campaigns(ObjMixin, View):
	
	model = Campaigns
	template = 'campaigns'


class Categories(ObjMixin, View):
	model = Categories
	template = 'categories'


