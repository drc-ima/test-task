from django.db import models

# Create your models here.

class Rental(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    rental = models.ForeignKey('Rental', on_delete=models.DO_NOTHING, related_name='rental_reservation', blank=True, null=True)
    checkin = models.DateField(null=True, blank=True)
    checkout = models.DateField(null=True, blank=True)


