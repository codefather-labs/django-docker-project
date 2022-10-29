from django.urls import path, include

from apps.core import views as core_views

core_patterns = [
    path('', core_views.main, name='main_url'),

]

urlpatterns = []
urlpatterns += core_patterns
