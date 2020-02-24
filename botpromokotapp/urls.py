from django.urls import path
from .views import *
# urls.py
from .feeds import TurboFeed

feed = TurboFeed()


urlpatterns = [
	path('forum/', Index.as_view(), name='index'),
	path('del_and_reload_db/', del_and_reload_db, name='del_and_reload_db'),
	path('campaigns/', campaigns, name='campaigns'),
	path('campaigns/t<int:pk>/', CampaignDetail.as_view(), name='campaigns_detail'),
	path('categories/', categories, name='categories'),
	path('categories/t<int:pk>/', CategoriesDetail.as_view(), name='categories_detail'),
	path('free_shipping/', FreeShipping.as_view(), name='free_shipping'),
	path('gift_to_order/', GiftToOrder.as_view(), name='gift_to_order'),
	path('robots.txt/', robots, name='robots'),
	path('sitemap.xml/', sitemap, name='sitemap'),
	path('feeds/turbo/', feed),
]
