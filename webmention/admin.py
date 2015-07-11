from django.contrib import admin

from .models import WebMentionResponse

class WebMentionResponseAdmin(admin.ModelAdmin):
    model = WebMentionResponse

    exclude = [
        'source',
        'response_to',
    ]

    readonly_fields = [
        'source_for_admin',
        'response_to_for_admin',
    ]

admin.site.register(WebMentionResponse, WebMentionResponseAdmin)
