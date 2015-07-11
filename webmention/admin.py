from django.contrib import admin

from .models import WebMentionResponse


class WebMentionResponseAdmin(admin.ModelAdmin):
    model = WebMentionResponse

    fields = [
        'source_for_admin',
        'response_to_for_admin',
        'response_body',
        'reviewed',
    ]

    readonly_fields = [
        'response_body',
        'source_for_admin',
        'response_to_for_admin',
    ]

    list_display = [
        'pk',
        'source_for_admin',
        'response_to_for_admin',
        'reviewed',
    ]

    list_editable = [
        'reviewed',
    ]

admin.site.register(WebMentionResponse, WebMentionResponseAdmin)
