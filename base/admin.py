from django.contrib import admin

from .models import Conference, Podpiska, ParticipantStatus, EventStatus, Country

admin.site.register(Conference)
admin.site.register(Podpiska)
admin.site.register(ParticipantStatus)
admin.site.register(EventStatus)
admin.site.register(Country)