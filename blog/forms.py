from django import forms


class AddForm(forms.Form):
    product=forms.ChoiceField(choices=[('valve','Valve')])

    oee = forms.IntegerField()
    quality = forms.IntegerField()
    volume = forms.IntegerField()