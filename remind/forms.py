from django import forms
from .models import  SubjectModel
from django.contrib.admin import widgets

Choice = {
    (True, "リマインドする"),
    (False,"リマインドを停止する"),
}

class RemindRadioForm(forms.Form):
    remind=forms.ChoiceField(label="リマインドについて", widget=forms.RadioSelect, choices=Choice,initial=True)


