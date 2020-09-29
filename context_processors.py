from home.forms import MessageForm
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def message_form(request):
    """
    Contact message form. Located in global context as the
    message form is accessed through the footer in all pages
    of the site.
    """
    if request.method == 'GET':
        message_form = MessageForm()
        context = {'message_form': message_form}
        return context
    elif 'send-message' not in request.POST:
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
            storage = messages.get_messages(request)
            storage.used = True
            messages.success(
                request, f'Message sent successfully! A copy of the message will be sent to {email}.')
            message_form = MessageForm()
            context = {
                'message_form': message_form,
            }
            return context


def images(request):
    """
    Image context processor for Cloudinary. Most of the images
    are proccessed through these keys. They add the correct classes
    and 'on error' events to the images.
    """
    return dict(
        THUMBNAIL={
            "class": "thumbnail inline", "format": "jpg", "crop": "scale", "height": 170, "width": 300, "onerror": "this.onerror=null;this.src='https://res.cloudinary.com/chickpeas/image/upload/v1600164143/kyles_critters/noImage_mumbcz.jpg';",
        },

        DETAIL_IMAGE={
            "class": "col-auto m-3 mb-auto p-0 card card-image img-fluid", "format": "jpg", "crop": "scale", "height": 300, "onerror": "this.onerror=null;this.src='https://res.cloudinary.com/chickpeas/image/upload/v1600164143/kyles_critters/noImage_mumbcz.jpg';",
        },

        JUMBO={
            "crop": "fill", 'height': 300, "class": "jumbotron d-none d-md-block p-0 b-0 m-0 mb-2 card card-image img-fluid rounded mx-auto", "onerror": "this.onerror=null;this.src='https://res.cloudinary.com/chickpeas/image/upload/v1600164143/kyles_critters/noImage_mumbcz.jpg';",
        },

        CARD={
            "class": "card-img-top rounded-top img-fluid", "format": "jpg", "crop": "scale", "alt": "Card image cap", "onerror": "this.onerror=null;this.src='https://res.cloudinary.com/chickpeas/image/upload/v1600164143/kyles_critters/noImage_mumbcz.jpg';",
        },

        LOAN={
            "class": "hoverable grid-item p-2 waves-effect", "style": "z-index: 10", "format": "jpg", "crop": "scale", "width": 200, "onerror": "this.onerror=null;this.src='https://res.cloudinary.com/chickpeas/image/upload/v1600164143/kyles_critters/noImage_mumbcz.jpg';",
        },

        GALLERY={
            "class": "borderedpicture", "format": "jpg", "crop": "scale", "width": 300, "onerror": "this.onerror=null;this.src='https://res.cloudinary.com/chickpeas/image/upload/v1600164143/kyles_critters/noImage_mumbcz.jpg';",
        },
    )


def google_api_key(request):
    return {'api_key': settings.GOOGLE_MAPS_API_KEY}
