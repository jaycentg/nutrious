from django import forms
from donation.models import Donatee

class OpenDonationForm(forms.ModelForm):
    class Meta:
       model = Donatee
       fields = ('name', 'description', 'amountNeeded')

       widgets = {
            'description': forms.Textarea(attrs={'cols': 24, 'rows': 4}),
       }


    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['amountNeeded'].min_value = 100000
