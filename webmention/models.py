from django.db import models


class WebMention(models.Model):
    source = models.URLField()
    target = models.URLField()

class WebMentionResponse(models.Model):
    response_body = models.TextField()
    response_to = models.URLField()
    source = models.URLField()
    reviewed = models.BooleanField(default=False)

    def __str__(self):
        return self.source

    def source_for_admin(self):
        return '<a href="{href}">{href}</a>'.format(href=self.source)
    source_for_admin.allow_tags = True
    source_for_admin.description = 'source'

    def response_to_for_admin(self):
        return '<a href="{href}">{href}</a>'.format(href=self.response_to)
    response_to_for_admin.allow_tags = True
    response_to_for_admin.description = 'source'
