from django.contrib import admin
from workers.models import Achievement, Person, HelpItem


class PersonAdmin(admin.ModelAdmin):
    exclude = ['user', 'alt', 'width', 'height']
    list_display = ('full_name', 'name', 'email')

    def delete_queryset(self, request, queryset):
        for person in queryset:
            person.delete()


class AchievementAdmin(admin.ModelAdmin):
    exclude = ['width', 'height']
    list_display = ('alt', 'expert')


class HelpItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'expert')


admin.site.register(Person, PersonAdmin)
admin.site.register(Achievement, AchievementAdmin)
admin.site.register(HelpItem, HelpItemAdmin)
