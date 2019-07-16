from django import forms
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Person, Achievement, Announcement, Article, HelpItem


class PersonCreate(CreateView):
    model = Person
    fields = ['full_name', 'name', 'birth_date', 'email', 'info', 'bio', 'photo', 'password']
    template_name = 'post.html'
    success_url = '/author/'

    def get_form(self, form_class=None):
        form = super(PersonCreate, self).get_form(form_class)
        form.fields['birth_date'].widget = forms.SelectDateWidget()
        return form


class PersonUpdate(UpdateView):
    model = Person
    fields = ['full_name', 'name', 'birth_date', 'email', 'info', 'bio', 'photo', 'password']
    template_name = 'post.html'
    success_url = '/author/'

    def get_form(self, form_class=None):
        form = super(PersonUpdate, self).get_form(form_class)
        form.fields['birth_date'].widget = forms.SelectDateWidget()
        return form


class PersonDelete(DeleteView):
    model = Person
    template_name = 'post.html'
    success_url = '/author/'


class PersonListView(ListView):
    model = Person
    template_name = 'people.html'
    context_object_name = 'authors_list'
    paginate_by = 4


class ArticleCreate(CreateView):
    model = Article
    template_name = 'post.html'
    success_url = '/article/'
    fields = ['name', 'content', 'content_min', 'author']


class ArticleUpdate(UpdateView):
    model = Article
    template_name = 'post.html'
    success_url = '/article/'
    fields = ['name', 'content', 'content_min', 'author']


class ArticleDelete(DeleteView):
    model = Article
    template_name = 'post.html'
    success_url = '/article/'


class ArticleListView(ListView):
    model = Article
    template_name = 'articles.html'
    context_object_name = 'articles_list'
    paginate_by = 3


class AnnouncementCreate(CreateView):
    fields = ['name', 'content', 'article', 'date', 'main']
    model = Announcement
    template_name = 'post.html'
    success_url = '/announcement/'

    def get_form(self, form_class=None):
        form = super(AnnouncementCreate, self).get_form(form_class)
        form.fields['date'].widget = forms.SelectDateWidget()
        return form


class AnnouncementUpdate(UpdateView):
    model = Announcement
    fields = ['name', 'content', 'article', 'date', 'main']
    template_name = 'post.html'
    success_url = '/announcement/'

    def get_form(self, form_class=None):
        form = super(AnnouncementUpdate, self).get_form(form_class)
        form.fields['date'].widget = forms.SelectDateWidget()
        return form


class AnnouncementDelete(DeleteView):
    model = Announcement
    template_name = 'post.html'
    success_url = '/announcement/'


class AnnouncementListView(ListView):
    model = Announcement
    template_name = 'announcements.html'
    context_object_name = 'announcement_list'
    paginate_by = 1
    ordering = ['-main']


class AchievementCreate(CreateView):
    model = Achievement
    template_name = 'post.html'
    fields = ['alt', 'photo', 'priority']
    success_url = '/achievement/'


class AchievementUpdate(UpdateView):
    model = Achievement
    fields = ['alt', 'photo', 'priority']
    template_name = 'post.html'
    success_url = '/achievement/'


class AchievementDelete(DeleteView):
    model = Achievement
    template_name = 'post.html'
    success_url = '/achievement/'


class AchievementListView(ListView):
    model = Achievement
    template_name = 'achievements.html'
    context_object_name = 'achievement_list'
    ordering = ['-priority']


class HelpItemCreate(CreateView):
    model = HelpItem
    template_name = 'post.html'
    success_url = '/help_item/'
    fields = ['name', 'description', 'expert']


class HelpItemUpdate(UpdateView):
    model = HelpItem
    template_name = 'post.html'
    success_url = '/help_item/'
    fields = ['name', 'description', 'expert']


class HelpItemDelete(DeleteView):
    model = HelpItem
    template_name = 'post.html'
    success_url = '/help_item/'


class HelpItemListView(ListView):
    model = HelpItem
    template_name = 'help_items.html'
    context_object_name = 'help_item_list'


def main(request):
    return render(request, 'main.html')
