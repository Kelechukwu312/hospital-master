from django.db import models
from PIL import Image
from decimal import Decimal
from user.models import Category
from user.models import Doctors,patients,Pham_model,CatLeve
import uuid

# Create your models here.



class Book_Apointment_model(models.Model):
    patients = models.ForeignKey(patients,null=True, related_name='pa', blank=True,on_delete=models.CASCADE)
    fee = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal('0.0'),null=True, blank=True)
    Date = models.CharField(max_length=120)
    Time = models.CharField(max_length=300)
    doctors = models.ForeignKey(Doctors,null=True, blank=True,on_delete=models.CASCADE)
    accepts = models.CharField(max_length=150,null=True, blank=True,default="Pending")
    #card_num = models.CharField
    uu_id = models.UUIDField(default=uuid.uuid4)
    st = models.DateTimeField(auto_now_add=True)
    level = models.CharField(max_length=120,null=True, blank=True)
    matriculationnumber  = models.CharField(max_length=120,null=True, blank=True)

    #vital_signs = models.ForeignKey(Vital_Signs,null=True, blank=True,on_delete=models.CASCADE)


    class Meta:
        ordering = ['-st',]


    def __str__(self):
        return f"{self.patients}, {self.Time}, {self.Date}"



class Decline_note(models.Model):
    #patient = models.ForeignKey(patients,null=True, related_name='patient', blank=True,on_delete=models.SET_NULL)
    doctors = models.ForeignKey(Doctors, null=True, blank=True, on_delete=models.CASCADE)
    book_apointment = models.ForeignKey(Book_Apointment_model,null=True, related_name='book', blank=True,on_delete=models.CASCADE)
    Note = models.TextField(max_length=500)
    st = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Note

    class Meta:
        ordering = ['-st',]



class Medical_test(models.Model):
    blood_pressure = models.CharField(max_length=500)
    Weight = models.CharField(max_length=500)
    blood_sugar = models.CharField(max_length=500)
    body_tempreture = models.CharField(max_length=500)
    medical_prescription = models.TextField(max_length=700)
    patient = models.ForeignKey(patients,null=True, related_name='patient', blank=True,on_delete=models.CASCADE)
    doctors = models.ForeignKey(Doctors, null=True, blank=True, on_delete=models.CASCADE)
    u_id = models.UUIDField(default=uuid.uuid4)
    Book_Apointment_mo = models.ForeignKey(Book_Apointment_model, related_name='Book_Apointment',null=True, blank=True, on_delete=models.SET_NULL)
    st = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'medical {}'.format(self.patient, self.doctors,self.blood_pressure)

    class Meta:
        ordering = ['-st',]

class Send_report_to_pharmacy(models.Model):
    Date = models.CharField(max_length=120,blank=True,null=True)
    Time_send = models.CharField(max_length=300,blank=True,null=True)
    patient = models.ForeignKey(patients,null=True, blank=True,on_delete=models.CASCADE)
    #confirm = models.CharField(max_length=120, null=True, blank=True, default="Pending")
    time = models.DateTimeField(auto_now_add=True)
    #Pham = models.ForeignKey(Pham_model,null=True, related_name='pham',blank=True,on_delete=models.SET_NULL)
    medical = models.ForeignKey(Medical_test, null=True, related_name='medical', blank=True, on_delete=models.CASCADE)
    class Meta:
        ordering = ['-time',]
    def __str__(self):
        return 'report {}'.format(self.patient,self.Date)

class confirm_drug(models.Model):
    confirm = models.CharField(max_length=120,null=True, blank=True,default="Pending")
    Pham = models.ForeignKey(Pham_model,null=True, related_name='pham',blank=True,on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    drug_name = models.TextField(max_length=500, null=True, blank=True)
    drug_price = models.CharField(max_length=120, null=True, blank=True)
    Send_pharmacy = models.ForeignKey(Send_report_to_pharmacy,null=True, related_name='pham',blank=True,on_delete=models.CASCADE)

    class Meta:
        ordering = ['-time',]

    def __str__(self):
        return self.confirm
'''
class add_drugs(models.Model):
    drug_name = models.CharField(max_length=120, null=True, blank=True)
    drug_price = models.CharField(max_length=120, null=True, blank=True)
    drug_num   = models.CharField(max_length=120, null=True, blank=True)

'''

class chat_model(models.Model):
    user = models.ForeignKey(patients,blank=True, null=True, related_name='sender',on_delete=models.CASCADE)
    other_user = models.ForeignKey(Doctors,blank=True, null=True, related_name='reciever',on_delete=models.CASCADE)
    message = models.TextField(max_length=90000,blank=True,null=True)
    time = models.DateTimeField(auto_now_add=True)
    viewed = models.CharField(max_length=500, default=True)
    Sender_back = models.CharField(max_length=400,default=False)
    reciever_back = models.CharField(max_length=400, default=False)
    #class Meta:
    #    ordering = ['-time',]

    def __str__(self):
        return self.message


class Notification(models.Model):
    Dr_notify = models.ForeignKey(Doctors,blank=True, null=True, related_name='Dr_notify',on_delete=models.CASCADE)
    pq_message = models.ForeignKey(patients,blank=True, null=True, related_name='pq_message',on_delete=models.CASCADE)
    viewed = models.CharField(max_length=500,default=False)
    time = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-time',]

    def __str__(self):
        return 'report {}'.format(self.Dr_notify)



class NurseModels(models.Model):
    First_name = models.CharField(max_length=500,null=True,blank=True)
    email = models.CharField(max_length=500, null=True,blank=True)
    password = models.CharField(max_length=500,null=True,blank=True)
    time = models.DateTimeField(auto_now_add=True)
    category_level = models.ForeignKey(CatLeve, null=True, blank=True, on_delete=models.SET_NULL)


    class Meta:
        ordering = ['-time',]
    def __str__(self):
        return self.First_name

class Vital_Signs(models.Model):
    temperature = models.CharField(max_length=500,null=True,blank=True)
    heart_rate = models.CharField(max_length=500,null=True,blank=True)
    blood_pressure = models.CharField(max_length=500,null=True,blank=True)
    admitted_date = models.CharField(max_length=500,null=True,blank=True)
    discharged_date = models.CharField(max_length=500,null=True,blank=True)
    bookapointment = models.ForeignKey(Book_Apointment_model,null=True, related_name='bookpoint', blank=True,on_delete=models.SET_NULL)
    time = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-time',]
    def __str__(self):
        return self.temperature

