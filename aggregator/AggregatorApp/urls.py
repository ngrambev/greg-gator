from django.urls import path
from AggregatorApp.views import scrape, home

urlpatterns = [
  path('scrape/', scrape, name="scrape"),
  path('', home, name="home"),
]
