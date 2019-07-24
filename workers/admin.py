from django.contrib import admin
from django.contrib import messages
from django.utils.html import mark_safe

from workers.models import Achievement, Person, HelpItem


class HelpItemInline(admin.TabularInline):
    model = HelpItem
    fields = ['name', 'expert', 'description']
    extra = 0


class AchievementInline(admin.TabularInline):
    model = Achievement
    list_display = ('alt', 'expert')
    fields = ['expert', 'priority', ('photo', 'img_preview'), 'alt']
    readonly_fields = ['img_preview']
    extra = 0

    def img_preview(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(url=obj.photo.url,
                                                                                      width=obj.photo.width/10,
                                                                                      height=obj.photo.height/10))

    img_preview.short_description = 'Предпросмотр фото'


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'name', 'email', 'achievement_count', 'help_item_count', 'is_superuser')
    fieldsets = (
        ('Для создание пользователя',
         {'fields': ('name', 'email')}),

        ('Для заполнения профиля',
         {'fields': ('full_name', 'birth_date', 'info', 'bio', ('photo', 'img_preview'), 'alt')})
    )
    readonly_fields = ['img_preview']
    inlines = [AchievementInline, HelpItemInline]
    list_per_page = 20

    def is_superuser(self, obj):
        return obj.user.is_superuser

    is_superuser.short_description = 'Суперпользователь'
    is_superuser.boolean = True

    def achievement_count(self, obj):
        return obj.achievements.count()

    achievement_count.short_description = 'Количество достижений'

    def help_item_count(self, obj):
        return obj.help_items.count()

    help_item_count.short_description = 'Количество пунктов помощи'

    def img_preview(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(url=obj.photo.url,
                                                                                      width=obj.photo.width/10,
                                                                                      height=obj.photo.height/10))

    img_preview.short_description = 'Предпросмотр фото'

    def delete_queryset(self, request, queryset):
        for person in queryset:
            if person.user.is_superuser:
                messages.add_message(request, messages.ERROR, "Никто не может удалить суперпользователя. "
                                                              "Для начала нужно сделать его обычным пользователем, "
                                                              "если у вас есть такие права")
            else:
                person.delete()

    def delete_model(self, request, obj):
        if obj.user.is_superuser:
            messages.add_message(request, messages.ERROR, "Никто не может удалить суперпользователя "
                                                          "Для начала нужно сделать его обычным пользователем,"
                                                          " если у вас есть такие права")
        else:
            super(PersonAdmin, self).delete_model(request, obj)

    def get_queryset(self, request):
        qs = super(PersonAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(user=request.user)
