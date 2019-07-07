from django.contrib import admin
from main.models import Achievement, Person


class PersonAdmin(admin.ModelAdmin):
    def delete_queryset(self, request, queryset):
        for person in queryset:
            person.delete()


admin.site.register(Person, PersonAdmin)
admin.site.register(Achievement)
