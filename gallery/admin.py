from django.contrib import admin

from .models import GalleryEntry


class GalleryAdmin(admin.ModelAdmin):

    readonly_fields = ('entry_number', 'user_profile', 'date')

    fields = ('entry_number', 'user_profile', 'date', 'critter_name',
              'critter_type', 'critter_info', 'image')

    list_display = ('date', 'user_profile',
                    'critter_type', 'entry_number',)

    ordering = ('-date',)


admin.site.register(GalleryEntry, GalleryAdmin)
