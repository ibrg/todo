# from django import forms
import floppyforms.__future__ as forms
from .models import Todo
from floppyforms.widgets import DateInput, TimeInput
import datetime
from django.utils.timezone import utc


class TodoForm(forms.ModelForm):
    date = forms.DateField(initial=datetime.date.today(), localize=True)
    time = forms.TimeField(initial=datetime.datetime.now().replace(tzinfo=utc).strftime('%H:%M'), localize=True)

    class Meta:
        model = Todo
        fields = ('task', 'date', 'time')
