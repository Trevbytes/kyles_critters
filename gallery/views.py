from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import GalleryEntry
from .forms import GalleryEntryForm
from random import shuffle
from profiles.models import UserProfile


def gallery(request):
    """ A view to return the gallery page """

    entries = GalleryEntry.objects.all()
    shuffled_entries = list(entries)
    shuffle(shuffled_entries)
    template = 'gallery/gallery.html'
    context = {
        'entries': entries,
        'shuffled_entries': shuffled_entries,
    }

    return render(request, template, context)


@login_required
def add_entry(request):
    """ Add an entry to the gallery """
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, only logged in users can do that.')
        return redirect(reverse('gallery'))

    if request.method == 'POST':
        form = GalleryEntryForm(request.POST, request.FILES)
        if form.is_valid():
            # Add unique entry number
            entry_number = form.save()
            # Attach the user's profile to the order
            profile = UserProfile.objects.get(user=request.user)
            new_entry = get_object_or_404(GalleryEntry, entry_number=entry_number)
            new_entry.user_profile = profile
            new_entry.save()
            messages.success(request, 'Successfully added entry!')
            return redirect(reverse('gallery'))
        else:
            messages.error(request, 'Failed to add entry. Please ensure the form is valid.')
    else:
        form = GalleryEntryForm()

    template = 'gallery/add_entry.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_entry(request, entry_number):
    """ Edit an entry in the gallery """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only logged in users can do that.')
        return redirect(reverse('gallery'))

    entry = get_object_or_404(GalleryEntry, entry_number=entry_number)
    if request.method == 'POST':
        form = GalleryEntryForm(request.POST, request.FILES, instance=entry)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated entry!')
            return redirect(reverse('gallery'))
        else:
            messages.error(request, 'Failed to update entry. Please ensure the form is valid.')
    else:
        form = GalleryEntryForm(instance=entry)
        messages.info(request, f'You are editing {entry.critter_name}')

    template = 'gallery/edit_entry.html'
    context = {
        'form': form,
        'entry': entry,
    }

    return render(request, template, context)


@login_required
def delete_entry(request, entry_number):
    """ Delete an entry from the gallery """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only logged in users can do that.')
        return redirect(reverse('gallery'))

    entry = get_object_or_404(GalleryEntry, entry_number=entry_number)
    entry.delete()
    messages.success(request, 'Entry deleted!')
    return redirect(reverse('gallery'))
