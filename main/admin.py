from django.contrib import admin
from main.models import Achievement, Person, Article, ArticlePhotoReport, Announcement, HelpItem, Event


class PersonAdmin(admin.ModelAdmin):
    exclude = ['user', 'alt', 'width', 'height']
    list_display = ('full_name', 'name', 'email')

    def delete_queryset(self, request, queryset):
        for person in queryset:
            person.delete()


class ArticlePhotoReportAdmin(admin.ModelAdmin):
    exclude = ['width', 'height']
    list_display = ('article',)


class EventAdmin(admin.ModelAdmin):
    exclude = ['width', 'height']
    list_display = ('name', 'type')


class AchievementAdmin(admin.ModelAdmin):
    exclude = ['width', 'height']
    list_display = ('alt', 'expert')


class HelpItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'expert')


class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('name', 'event')


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'release_date')


admin.site.register(Person, PersonAdmin)
admin.site.register(Achievement, AchievementAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticlePhotoReport, ArticlePhotoReportAdmin)
admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(HelpItem, HelpItemAdmin)
admin.site.register(Event, EventAdmin)
# from django.contrib.auth.models import User, Group
# TODO admin.site.unregister(User)
# TODO admin.site.unregister(Group)
