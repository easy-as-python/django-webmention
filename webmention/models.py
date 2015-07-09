from django.db import models


class WebMention(models.Model):
    source = models.URLField()
    target = models.URLField()
