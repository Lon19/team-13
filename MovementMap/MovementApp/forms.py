from django import forms


class MapForm(forms.Form):
    ward_search = forms.CharField(label='Ward Search', max_length=100)
