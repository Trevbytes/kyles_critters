from home.forms import MessageForm
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.shortcuts import HttpResponseRedirect, redirect, reverse


def message_form(request):
    if request.method == 'GET':
        message_form = MessageForm()
        context = {'message_form': message_form}
        return context
    else:
        message_form = MessageForm(request.POST)
        if message_form.is_valid():
            full_name = message_form.cleaned_data['full_name']
            email = message_form.cleaned_data['email']
            phone_number = message_form.cleaned_data['phone_number']
            message_subject = message_form.cleaned_data['message_subject']
            message_body = message_form.cleaned_data['message_body']
            subject = render_to_string(
                'home/message_emails/message_email_subject.txt')
            body = render_to_string(
                'home/message_emails/message_email_body.html',
                {'full_name': full_name,
                 'phone_number': phone_number,
                 'message_body': message_body,
                 'message_subject': message_subject,
                 'contact_email': settings.DEFAULT_FROM_EMAIL})
            plain_message = strip_tags(body)

            send_mail(
                subject,
                plain_message,
                settings.DEFAULT_FROM_EMAIL,
                [email],
                html_message=body
            )
            messages.success(request, f'Message sent successfully! A copy of the message will be sent to {email}.')
            message_form = MessageForm()
            context = {
                    'message_form': message_form,
                    }
        return context
