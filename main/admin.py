from django.contrib import admin
from main.models import Achievement, Person, Article, Announcement, HelpItem, Event


class PersonAdmin(admin.ModelAdmin):
    exclude = ['user']
    list_display = ('full_name', 'name', 'email')

    def delete_queryset(self, request, queryset):
        for person in queryset:
            person.delete()


admin.site.register(Person, PersonAdmin)
admin.site.register(Achievement)
admin.site.register(Article)
admin.site.register(Announcement)
admin.site.register(HelpItem)
admin.site.register(Event)
# from django.contrib.auth.models import User, Group
# TODO admin.site.unregister(User)
# TODO admin.site.unregister(Group)
