from django.db import models


class WebMentionResponse(models.Model):
    response_body = models.TextField()
    response_to = models.URLField()
    source = models.URLField()
    reviewed = models.BooleanField(default=False)
    current = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'webmention'
        verbose_name_plural = 'webmentions'

    def __str__(self):
        return self.source

    def source_for_admin(self):
        return '<a href="{href}">{href}</a>'.format(href=self.source)
    source_for_admin.allow_tags = True
    source_for_admin.short_description = 'source'

    def response_to_for_admin(self):
        return '<a href="{href}">{href}</a>'.format(href=self.response_to)
    response_to_for_admin.allow_tags = True
    response_to_for_admin.short_description = 'response to'

    def invalidate(self):
        if self.id:
            self.current = False
            self.save()

    def update(self, source, target, response_body):
        self.response_body = response_body
        self.source = source
        self.response_to = target
        self.current = True
        self.save()
