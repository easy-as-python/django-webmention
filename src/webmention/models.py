from django.contrib.admin import display
from django.db import models
from django.utils.html import format_html


class WebMentionResponse(models.Model):
    id: int
    response_body = models.TextField()
    response_to = models.URLField()
    source = models.URLField()
    reviewed = models.BooleanField(default=False)
    current = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "webmention"
        verbose_name_plural = "webmentions"

    def __str__(self):
        return self.source

    @display(description="source")
    def source_for_admin(self):
        return format_html('<a href="{}">{}</a>', self.source, self.source)

    @display(description="response to")
    def response_to_for_admin(self):
        return format_html('<a href="{}">{}</a>', self.response_to, self.response_to)

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
