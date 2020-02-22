from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['index', 'campaigns', 'categories', 'free_shipping']

    def location(self, item):
        return reverse(item)
