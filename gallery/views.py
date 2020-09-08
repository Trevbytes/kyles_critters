from django.shortcuts import render
from .models import GalleryEntry


def gallery(request):
    """ A view to return the gallery page """

    entries = GalleryEntry.objects.all()

    context = {
        'entries': entries,
    }

    return render(request, 'gallery/gallery.html', context)
