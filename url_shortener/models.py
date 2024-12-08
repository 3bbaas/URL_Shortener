from django.db import models


class shorten(models.Model):
    url = models.CharField(max_length=203)
    shortened_url = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.url
