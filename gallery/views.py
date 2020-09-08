from django.shortcuts import render

from .models import GalleryEntry


def gallery(request):
    """ A view to return the gallery page """

    entries = GalleryEntry.objects.all()

    template = 'gallery/gallery.html'
    context = {
        'entries': entries,
    }

    return render(request, template, context)
