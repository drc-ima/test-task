from re import sub
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from rental.forms import ReservationForm
from rental.models import Rental, Reservation
from django.db.models import OuterRef, Value, CharField
from django.db.models.functions import Coalesce

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

    # sub query using id for previous reservation
    # sub_query = Reservation.objects.filter(rental=OuterRef('rental'), id__lt=OuterRef('pk')).order_by('-id')

    # sub query using checkin date for previous reservation
    sub_query = Reservation.objects.filter(rental=OuterRef('rental'), checkin__lt=OuterRef('checkin')).order_by('-checkin')

    # using the sub query as annotate
    queryset = Reservation.objects.all().annotate(previous=Coalesce(sub_query.values('id')[:1], Value('-'), output_field=CharField()))


# add new reservation
class AddReservation(CreateView):
    template_name = 'reservation/add.html'
    form_class = ReservationForm
    success_url = reverse_lazy('reservations')

