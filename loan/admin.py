from django.contrib import admin
from .models import LoanRequest


class LoanRequestAdmin(admin.ModelAdmin):

    readonly_fields = ('order_number', 'date',)

    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county',
              'critter_request', 'request_info')

    list_display = ('order_number', 'date', 'full_name',
                    'critter_request',)

    ordering = ('-date',)


admin.site.register(LoanRequest, LoanRequestAdmin)
