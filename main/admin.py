from django.contrib import admin
from main.models import Achievement, Person


class PersonAdmin(admin.ModelAdmin):
    pass


admin.site.register(Person, PersonAdmin)
admin.site.register(Achievement)
