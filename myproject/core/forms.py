from django import forms
from localflavor.br.br_states import STATE_CHOICES


class StateForm(forms.Form):
    state = forms.ChoiceField(
        choices=STATE_CHOICES,
        label='Estado',
        # widget=forms.Select(
        #     attrs={'class': 'form-control'}
        # )
    )
