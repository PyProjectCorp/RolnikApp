from django.shortcuts import render
from django.views.generic import DetailView, FormView
from .models import Message
from contact.forms import MessageForm


class MessageAddView(FormView):
    form_class = MessageForm
    template_name = 'message_form.html'
    success_url= '/contact'
    def form_valid(self, form):
        form.save()
        return super(MessageAddView, self).form_valid(form)
    