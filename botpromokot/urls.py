from django.contrib import admin
from django.urls import path
import botpromokotapp.views
from botpromokotapp.models import Cupons
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap

from botpromokotapp.sitemaps import StaticViewSitemap

sitemaps = {
    'botpromokotapp': GenericSitemap({
        'queryset': Cupons.objects.all(),
        'date_field': 'updated',
    }, priority=0.9),
    'static': StaticViewSitemap,
}

urlpatterns = [
	path('', botpromokotapp.views.Index.as_view(), name='index'),
	path('admin/', admin.site.urls),
    path('campaigns/', botpromokotapp.views.Campaigns.as_view(), name='campaigns'),
    path('campaigns/t<int:pk>/', botpromokotapp.views.CampaignDetail.as_view(), name='campaigns_detail'),
    path('categories/', botpromokotapp.views.Categories.as_view(), name='categories'),
    path('categories/t<int:pk>/', botpromokotapp.views.CategoriesDetail.as_view(), name='categories_detail'),
    path('free_shipping/', botpromokotapp.views.FreeShipping.as_view(), name='free_shipping'),
    path('gift_to_order/', botpromokotapp.views.GiftToOrder.as_view(), name='gift_to_order'),   
    path('static_sitemap.xml', sitemap,
         {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('sitemap.xml/', botpromokotapp.views.sitemap, name='sitemap'),
    path('robots.txt/', botpromokotapp.views.robots, name='robots'),
    
]






