from django.contrib.sitemaps import ping_google
from django.core.management import BaseCommand
from django.urls import reverse


class Command(BaseCommand):

    def handle(self, *args, **options):
        try:
            ping_google(
                sitemap_url=reverse(
                    "django.contrib.sitemaps.views.sitemap"
                )
            )
            self.stdout.write(
                self.style.SUCCESS(
                    "Google pinged success!"
                )
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(
                    str(e)
                )
            )
