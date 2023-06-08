import datetime
from django.forms import SelectDateWidget
from django import forms
from .models import Habit, HabitRecord


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ("name", "target", "target_number")


class HabitRecordForm(forms.ModelForm):
    class Meta:
        model = HabitRecord
        widgets = {"record_date": SelectDateWidget()}
        fields = ("record_date", "achieved")
