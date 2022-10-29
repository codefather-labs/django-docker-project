from django.contrib.sitemaps import Sitemap
from django.core.paginator import Paginator, Page
from django.urls import reverse

from settings.environment.settings import get_settings_module, environment

settings = get_settings_module()
DEFAULT_PROTOCOL_STRATEGY = 'https' \
    if environment.value == 'Production' else 'http'


class StaticSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = DEFAULT_PROTOCOL_STRATEGY

    def items(self):
        return [
            'core-urls:main_url',
        ]

    def location(self, item):
        return reverse(item)
