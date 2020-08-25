from django.shortcuts import render

# Create your views here.


def loan(request):
    """ A view to return the loan a critter page """

    return render(request, 'loan/loan.html')
