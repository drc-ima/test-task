from django import forms

from rental.models import Reservation


class ReservationForm(forms.ModelForm):
    checkin = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    checkout = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Reservation
        fields = ['rental', 'checkin', 'checkout']
        widgets = {
            'rental': forms.Select(attrs={'required': True})
        }