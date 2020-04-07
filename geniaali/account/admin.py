from django.contrib import admin
from .models import Country,State,City,Location,Person


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):

	#3.this will display in the list form
    list_display = ('country_id','country', 'shortname')

@admin.register(State)
class StateAdmin(admin.ModelAdmin):

	#3.this will display in the list form
    list_display = ('state_id','country', 'state')

@admin.register(City)
class CityAdmin(admin.ModelAdmin):

	#3.this will display in the list form
    list_display = ('city_id','country', 'state','city')

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):

	#3.this will display in the list form
    list_display = ('location_id','country','state','city','location')
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):

	#3.this will display in the list form
    list_display = ('id','name','country', 'state','city','location')
