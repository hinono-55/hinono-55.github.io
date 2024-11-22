from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import ContactmailForm
from django.contrib import messages
from django.core.mail import EmailMessage

class ContactmailView(FormView):
    template_name='contact.html'
    form_class=ContactmailForm
    success_url=reverse_lazy('contactmail:contact')

    def form_valid(self, form):
        name=form.cleaned_data['name']
        email=form.cleaned_data['email']
        title=form.cleaned_data['title']
        message=form.cleaned_data['message']
        subject='お問い合わせ:{}'.format(title)
        message=\
        '送信者名:{0}\nメートルアドレス:{1}\nタイトル:{2}\nメッセージ:\n{3}'\
        .format(name, email, title, message)
        from_email='kmm2459388@stu.o-hara.ac.jp'
        to_list=['kmm2459388@stu.o-hara.ac.jp']
        message=EmailMessage(subject=subject, body=message, from_email=from_email, to=to_list,)
        message.send()
        messages.success(self.request, 'お問い合わせは正常に送信されました')
        return super().form_valid(form)