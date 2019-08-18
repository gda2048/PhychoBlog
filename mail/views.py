from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView

from mail.forms import ContactForm


class ContactView(FormView):
    template_name = 'mail/contact_form.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Сообщение отправлено. С Вами свяжутся')
        return reverse_lazy('contact_form')
