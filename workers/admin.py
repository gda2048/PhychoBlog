from django.contrib import admin
from workers.models import Achievement, Person, HelpItem


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'name', 'email')
    fieldsets = (
        ('Для создание пользователя',
         {'fields': ('name', 'email')}),

        ('Для заполнения профиля',
         {'fields': ('full_name', 'birth_date', 'info', 'bio', 'photo', 'alt')})
    )

    def delete_queryset(self, request, queryset):
        for person in queryset:
            person.delete()


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('alt', 'expert')
    fields = ['expert', 'priority', 'photo', 'alt']


@admin.register(HelpItem)
class HelpItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'expert')
    fields = ['name', 'expert', 'description']
