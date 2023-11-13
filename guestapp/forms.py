from django.forms import ModelForm

from guestapp.models import Guest


class GuestCreationForm(ModelForm):

    class Meta:
        model = Guest
        fields = ['writer', 'content']