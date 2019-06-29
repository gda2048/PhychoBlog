from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Person, Achievement, Announcement, Article, HelpItem
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.core.paginator import Paginator


class PersonCreate(CreateView):
    model = Person
    template_name = 'post.html'
    success_url = '/author/'

    def form_valid(self, form):
        res = form.save(commit=False)
        print(res.name, res.email, res.password)
        user = User.objects.create_user(res.name, res.email, res.password)
        user.save()
        return super(PersonCreate, self).form_valid(form)


class PersonUpdate(UpdateView):
    model = Person
    template_name = 'post.html'
    success_url = '/author/'

    def form_valid(self, form):
        res = form.save(commit=False)
        user  = User.objects.get(username = self.object.name)
        user.email = res.email
        user.save()
        return super(PersonUpdate, self).form_valid(form)


class PersonDelete(DeleteView):
    model = Person
    template_name = 'post.html'
    success_url = '/author/'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        user = User.objects.get(username=self.object.name)
        user.delete()
        self.object.delete()
        return HttpResponseRedirect(success_url)


class PersonListView(ListView):
    model = Person
    template_name = 'people.html'
    context_object_name = 'authors_list'
    paginate_by = 1


class ArticleCreate(CreateView):
    model = Article
    template_name = 'post.html'
    success_url = '/article/'


class ArticleUpdate(UpdateView):
    model = Article
    template_name = 'post.html'
    success_url = '/article/'


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
    model = Announcement
    template_name = 'post.html'
    success_url = '/announcement/'


class AnnouncementUpdate(UpdateView):
    model = Announcement
    template_name = 'post.html'
    success_url = '/announcement/'


class AnnouncementDelete(DeleteView):
    model = Announcement
    template_name = 'post.html'
    success_url = '/announcement/'


class AnnouncementListView(ListView):
    model = Announcement
    template_name = 'announcements.html'
    context_object_name = 'announcement_list'


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
    fields = ['alt', 'photo', 'priority']
    template_name = 'post.html'
    success_url = '/achievement/'


class AchievementListView(ListView):
    model = Achievement
    template_name = 'achievements.html'
    context_object_name = 'achievement_list'


class HelpItemCreate(CreateView):
    model = HelpItem
    template_name = 'post.html'
    success_url = '/help_item/'


class HelpItemUpdate(UpdateView):
    model = HelpItem
    template_name = 'post.html'
    success_url = '/help_item/'


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
