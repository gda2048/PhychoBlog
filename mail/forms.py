from django import forms
from django.core.mail import EmailMessage

from psycho.settings import EMAIL_MAIN


class ContactForm(forms.Form):
    name = forms.CharField(label='Ваше имя', widget=forms.TextInput(attrs={'placeholder': 'Анастасия'}))
    to_email = forms.EmailField(label='Ваш email для связи',
                                widget=forms.EmailInput(attrs={'placeholder': 'inst.art.of.life@gmail.com'}))
    subject = forms.CharField(label='Тема', required=False,
                              widget=forms.TextInput(attrs={'placeholder': 'Мероприятие "название"'}))
    message = forms.CharField(label='Ваше сообщение', widget=forms.Textarea(attrs={'placeholder': 'Сообщение'}),
                              required=False)

    def send_email(self):
        name, to_email = self.cleaned_data['name'], self.cleaned_data['to_email']
        subject, message = self.cleaned_data['subject'], self.cleaned_data['message']
        email = EmailMessage(subject, message + f'\nИмя: {name}\nEmail для связи с клиентом: {to_email}', to=EMAIL_MAIN)
        email.send()
