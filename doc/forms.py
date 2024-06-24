from django import forms
from user.models import Pham_model,Doctors,patients
from doc.models import Vital_Signs
'''
from django import forms
from .models import Book_Apointment_model
from user.models import Category
cat=[Category.objects.all()]
class specialization_Form(forms.ModelForm):
    doc_specialization = forms.Select(cat)
    class Meta:
        model = Book_Apointment_model
        fields = {
            'doc_specialization',
        }

'''

class pharm_image_form(forms.ModelForm):
    class Meta:
        model = Pham_model
        fields  =[
            'image',
        ]




class Doctor_image_form(forms.ModelForm):
    class Meta:
        model = Doctors
        fields  =[
            'image',
        ]


class patient_image_form(forms.ModelForm):
    class Meta:
        model = patients
        fields  =[
            'image',
        ]



class ask_form(forms.ModelForm):

    class Meta:
        model = Vital_Signs
        fields =[
            'bookapointment',

        ]

