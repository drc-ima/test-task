from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from rental.forms import ReservationForm
from rental.models import Rental, Reservation

# Create your views here.


# add new rental
def add_rental(request):

    # post request
    if request.method == 'POST':
        name = request.POST.get('name')

        # create new rental object
        obj = Rental(name=name)

        # save object into database
        obj.save()

        return redirect('reservations')

    return render(request, 'rental/add.html')


# list of reservation view using a generic class based view
class Reservations(ListView):
    template_name = 'reservation/list.html'
    queryset = Reservation.objects.all()


# add new reservation
class AddReservation(CreateView):
    template_name = 'reservation/add.html'
    form_class = ReservationForm
    success_url = reverse_lazy('reservations')

