from dataclasses import fields
from django import forms
from.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ('status',)
        #fields = '__all__'