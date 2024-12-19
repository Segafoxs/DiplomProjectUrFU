from django import forms
from .models import Department, Permit


class DepartmentForm(forms.Form):
    department = forms.ModelChoiceField(queryset=Department.objects.all(), label="department", widget=forms.Select(attrs={"class": "form-select form-select-lg mb-3"}))



# class Status(forms.Form):
#     state = forms.ChoiceField(choices=Permit.statusPermit, widget=forms.Select(attrs={"class": "form-select form-select-lg mb-3"}))

class ChoiceDirector(forms.Form):
    name = forms.CharField(label="director name", max_length=100, widget=forms.TextInput(attrs={"class":"form-control form-control-lg"}))

class ChoiceManager(forms.Form):
    name = forms.CharField(label="manager name", max_length=100, widget=forms.TextInput(attrs={"class":"form-control form-control-lg"}))
class LinePermit(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100, widget=forms.TextInput(attrs={"class":"form-control form-control-lg"}))
    your_post = forms.CharField(label="Your post", max_length=100, widget=forms.TextInput(attrs={"class":"form-control form-control-lg"}))

