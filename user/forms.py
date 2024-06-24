from .models import Doctors,Category,Pham_model,accountant_model
from django import forms
from .models import Laboratory

cat=[Category.objects.all()]
class DoctorsForm(forms.ModelForm):
    Firstname =forms.CharField(label="",widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'First Name'}))
    Othername =forms.CharField(label="",widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Other Names'}))
    email = forms.CharField(label="",widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Email'}))
    price = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'price'}))
    category = forms.Select(cat)
    class Meta:
        model = Doctors
        fields =[
            'Firstname',
            'Othername',
            'email',
            'price',
            'category',

        ]


class specialization_Form(forms.ModelForm):
    name = forms.CharField(label="",widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Specialization Name'}))\

    class Meta:
        model = Category
        fields = {
            'name',
        }



class Pham_Form(forms.ModelForm):
    First_name =forms.CharField(label="",widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'First Name'}))
    Other_name =forms.CharField(label="",widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Other Names'}))
    email = forms.CharField(label="",widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Email'}))
    class Meta:
        model = Pham_model
        fields =[
            'First_name',
            'Other_name',
            'email',


        ]

class Accountant_Form(forms.ModelForm):
    First_name =forms.CharField(label="",widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'First Name'}))
    Other_name =forms.CharField(label="",widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Other Names'}))
    email = forms.CharField(label="",widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Email'}))
    class Meta:
        model = accountant_model
        fields =[
            'First_name',
            'Other_name',
            'email',


        ]

class Laboratory_Form(forms.ModelForm):
    First_name =forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'First Name'}))
    Other_name =forms.CharField(label="",widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Other Names'}))
    email = forms.CharField(label="",widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Email'}))
    class Meta:
        model = Laboratory
        fields = [
            'First_name',
            'Other_name',
            'email',


         ]   

