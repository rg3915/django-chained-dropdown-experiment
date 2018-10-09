from django import forms
from localflavor.br.br_states import STATE_CHOICES
from .models import City, District


class StateForm(forms.Form):
    state = forms.ChoiceField(
        choices=STATE_CHOICES,
        label='Estado',
        # widget=forms.Select(
        #     attrs={'class': 'form-control'}
        # )
    )
    city = forms.ModelChoiceField(
        queryset=City.objects.none(),
        required=False
    )
    district = forms.ModelChoiceField(
        queryset=District.objects.none(),
        required=False
    )

    class Meta:
        fields = ('state', 'city', 'district')

    def __init__(self, state=None, city=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.filter(uf=state)
        if city:
            self.fields['district'].queryset = District.objects.filter(
                city=city)
