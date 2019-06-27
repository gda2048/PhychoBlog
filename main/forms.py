from django import forms
from .models import *

class PersonForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)
        self.fields['birth_date'].widget = forms.SelectDateWidget(years=(year for year in range(1970,2005)))
        self.fields['password'].widget = forms.PasswordInput()

    class Meta:
        model = Person
        fields = '__all__'

class PersonFormUpdate(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('full_name','email', 'bio', 'info', 'photo')


class ArticleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        self.fields['author'].choices = Person.objects.all().values_list('id','name')

    class Meta:
        model = Article
        fields = '__all__'


class AnnouncementForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AnnouncementForm, self).__init__(*args, **kwargs)
        self.fields['article'].choices = Article.objects.all().values_list('id', 'name')
        self.fields['date'].widget = forms.SelectDateWidget(years=(year for year in range(1970,2005)))

    class Meta:
        model = Announcement
        fields = '__all__'


class AchievementForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AchievementForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Achievement
        fields = '__all__'


class HelpItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(HelpItemForm, self).__init__(*args, **kwargs)
        self.fields['expert'].choices = Person.objects.all().values_list('id', 'name')

    class Meta:
        model = HelpItem
        fields = '__all__'
