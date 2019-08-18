from django.contrib import admin
from django.contrib import messages
from django.db.models import Count

from main.admin import AdminImagePreviewMixin
from workers.models import Achievement, Person, HelpItem


class HelpItemInline(admin.TabularInline):
    model = HelpItem
    fields = ['name', 'expert', 'description']
    extra = 0
    classes = ['collapse']


class AchievementInline(AdminImagePreviewMixin, admin.TabularInline):
    model = Achievement
    list_display = ('alt', 'expert')
    fields = ['expert', 'priority', ('photo', AdminImagePreviewMixin.readonly_fields[0]), 'alt']
    extra = 0
    classes = ['collapse']

    def get_queryset(self, request):
        return super(AchievementInline, self).get_queryset(request).defer('binary_image', 'ext')


@admin.register(Person)
class PersonAdmin(AdminImagePreviewMixin, admin.ModelAdmin):
    list_display = ('full_name', 'name', 'email', 'achievement_count', 'help_item_count', 'is_superuser')
    fieldsets = (
        ('Для создание пользователя',
         {'fields': (('name', 'email'),)}),

        ('Для заполнения профиля',
         {'fields': ('full_name', 'birth_date', 'contacts', ('info', 'bio'), ('photo', 'img_preview'), 'alt')})
    )
    inlines = [AchievementInline, HelpItemInline]
    list_per_page = 20

    def is_superuser(self, obj):
        return obj.user.is_superuser

    is_superuser.short_description = 'Суперпользователь'
    is_superuser.boolean = True

    def achievement_count(self, obj):
        return obj.achievements_count

    achievement_count.short_description = 'Количество достижений'

    def help_item_count(self, obj):
        return obj.help_items_count

    help_item_count.short_description = 'Количество пунктов помощи'

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
        qs = super(PersonAdmin, self).get_queryset(request).select_related("user") \
            .defer('user__password', "user__last_login", "user__date_joined", "binary_image", "ext") \
            .annotate(help_items_count=Count("help_items", distinct=True),
                      achievements_count=Count("achievements", distinct=True))
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(user=request.user)
