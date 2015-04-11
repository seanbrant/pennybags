from django.contrib import admin

from pennybags.models import Prize, Marker, CollectedMarker


admin.site.register(Prize, list_display=['id', 'name'])
admin.site.register(Marker, list_display=['id', 'prize_id'])
admin.site.register(CollectedMarker)
