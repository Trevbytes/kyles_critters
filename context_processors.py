from home.forms import MessageForm
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from profiles.models import UserProfile


def message_form(request):
    """
    Contact Message Form

    Located in global context as the
    message form is accessed through the footer in all pages
    of the site.
    """
    if (request.method == 'GET') or ('send-message' not in request.POST):
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                message_form = MessageForm(initial={
                    'message_full_name': profile.user.get_full_name(),
                    'message_email': profile.user.email,
                    'message_phone_number': profile.default_phone_number,
                })
                context = {'message_form': message_form}
                return context
            except UserProfile.DoesNotExist:
                message_form = MessageForm()
                context = {'message_form': message_form}
                return context
        else:
            message_form = MessageForm()
            context = {'message_form': message_form}
            return context
    else:
        message_form = MessageForm(request.POST)
        if message_form.is_valid():
            full_name = message_form.cleaned_data['message_full_name']
            email = message_form.cleaned_data['message_email']
            phone_number = message_form.cleaned_data['message_phone_number']
            message_subject = message_form.cleaned_data['message_subject']
            message_body = message_form.cleaned_data['message_body']
            subject = render_to_string(
                'home/message_emails/message_email_subject.txt')
            body = render_to_string(
                'home/message_emails/message_email_body.html',
                {'full_name': full_name,
                 'sender_email': email,
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
                request, f'Message sent successfully! \
                    A copy of the message will be sent to {email}.')
            message_form = MessageForm()
            context = {
                'message_form': message_form,
            }
            return context


def images(request):
    """
    Image context processor for Cloudinary.

    Most of the images
    are proccessed through these keys. They add the correct classes
    and 'on error' events to the images.
    """
    image_error = "this.onerror=null;this.src='https://res.cloudinary.com/chickpeas/image/upload/v1600164143/kyles_critters/noImage_mumbcz.jpg';"
    return dict(
        THUMBNAIL={
            "alt": "critter picture",
            "class": "thumbnail inline",
            "format": "jpg", "crop": "scale",
            "height": 170, "width": 300,
            "onerror": image_error,
        },

        DETAIL_IMAGE={
            "alt": "critter picture",
            "class": "col-auto m-3 mb-auto p-0 card card-image img-fluid",
            "format": "jpg", "crop": "scale", "height": 300,
            "onerror": image_error,
        },

        JUMBO={
            "alt": "jumbo banner", "crop": "fill", 'height': 300,
            "class": "jumbotron d-none d-md-block\
                 p-0 b-0 m-0 mb-2 card card-image img-fluid rounded mx-auto",
            "onerror": image_error,
        },

        CARD={
            "class": "card-img-top rounded-top img-fluid", "format": "jpg",
            "crop": "scale", "alt": "Card image cap",
            "onerror": image_error,
        },

        LOAN={
            "alt": "critter name",
            "class": "hoverable grid-item p-2 waves-effect",
            "style": "z-index: 10", "format": "jpg", "crop": "scale",
            "width": 200,
            "onerror": image_error,
        },

        GALLERY={
            "alt": "critter picture",
            "class": "borderedpicture", "format": "jpg",
            "crop": "scale", "width": 300,
            "onerror": image_error,
        },
    )


def google_api_key(request):
    return {'api_key': settings.GOOGLE_MAPS_API_KEY}
