from django.contrib import admin
from workers.models import Achievement, Person, HelpItem
from django.utils.html import mark_safe


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
    list_display = ('full_name', 'name', 'email')
    fieldsets = (
        ('Для создание пользователя',
         {'fields': ('name', 'email')}),

        ('Для заполнения профиля',
         {'fields': ('full_name', 'birth_date', 'info', 'bio', ('photo', 'img_preview'), 'alt')})
    )
    readonly_fields = ['img_preview']
    inlines = [AchievementInline, HelpItemInline]

    def img_preview(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(url=obj.photo.url,
                                                                                      width=obj.photo.width/10,
                                                                                      height=obj.photo.height/10))

    img_preview.short_description = 'Предпросмотр фото'

    def delete_queryset(self, request, queryset):
        for person in queryset:
            person.delete()

    def get_queryset(self, request):
        qs = super(PersonAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(user=request.user)
