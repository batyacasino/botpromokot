from django.urls import path

from .views import *

urlpatterns = [
	path('', Index.as_view(), name='index'),
	path('campaigns/', Campaigns.as_view(), name='campaigns'),
	path('campaigns/t<int:pk>/', CampaignDetail.as_view(), name='campaigns_detail'),
	path('categories/', Categories.as_view(), name='categories'),
	path('categories/t<int:pk>/', CategoriesDetail.as_view(), name='categories_detail'),
	path('free_shipping/', FreeShipping.as_view(), name='free_shipping'),
	path('gift_to_order/', GiftToOrder.as_view(), name='gift_to_order'),
]
