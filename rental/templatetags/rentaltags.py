from django.template import Library

from rental.models import Reservation


register = Library()


# using template tags to get previous reservation of each reservation
@register.simple_tag
def previous_reservation(reservation_id):

    reservation = None
    previous = '-'
    try:
        # get reservation object with id
        reservation = Reservation.objects.get(id=reservation_id)

        # get rental object with reservation
        rental = reservation.rental
    
        # using the reservation_id to find the previous reservation by ording the id column in ascending order and slicing the results
        prev = Reservation.objects.filter(rental=rental, id__lt=reservation_id).order_by('-id')[0:1].get()
        previous = str(prev.id)
    except Reservation.DoesNotExist:pass
    
    return previous
