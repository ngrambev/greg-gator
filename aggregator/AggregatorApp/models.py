from django.db import models

# This represents the basic building block of the page.
class Headline(models.Model):
  title = models.CharField(max_length=200)
  image = models.URLField(null=True, blank=True)
  url = models.TextField()
  def __str__(self):
    return self.title
