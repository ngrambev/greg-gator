import requests
from urllib.parse import urljoin
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup as BSoup
from news.models import Headline
from django.http import HttpResponse
from django.views import View

requests.packages.urllib3.disable_warnings()


class Headlines(View):
    def get(self, request):
        return HttpResponse('result')


def news_list(request):
	scrape(request)
	headlines = Headline.objects.all()[::-1]
	context = {
		'object_list': headlines,
	}
	return render(request, "home.html", context)

def scrape(request):
	# Delete all previous headlines, they may be outdated.
	Headline.objects.all().delete()

	# Fill the database up again.

	# Motortrend
	motorTrend = "https://www.motortrend.com/"

	session = requests.Session()
	content = session.get(motorTrend + "auto-news/", verify=False).content
	soup = BSoup(content, "html.parser")

	# Find all instances of the proper class which represents a headline.
	News = soup.find_all('a', class_="_22VtJ")
	for article in News:
		# Parse out the data out of the html.
		title = article.getText()
		link = urljoin(motorTrend, article['href'])

		# Create a Headline object, and store pertinent info.
		new_headline = Headline()
		new_headline.title = title
		new_headline.url = link

		# Save the headline into the database.
		new_headline.save()

	# The Drive
	theDrive = "https://www.thedrive.com/"

	content = session.get(theDrive + "the-war-zone/", verify=False).content
	soup = BSoup(content, "html.parser")

	# Find all instances of the proper class which represents a headline.
	News = soup.find_all('a', class_="MuiBox-root css-3f60fj")
	for article in News:
		# Parse out the data out of the html.
		title = article.find('h3', class_="MuiTypography-root MuiTypography-h5 css-z31x94").getText()
		link = urljoin(theDrive, article['href'])

		# Create a Headline object, and store pertinent info.
		new_headline = Headline()
		new_headline.title = title
		new_headline.url = link

		# Save the headline into the database.
		new_headline.save()

	return redirect("../")
