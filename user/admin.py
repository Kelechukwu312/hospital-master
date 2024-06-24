from django.contrib import admin
from .models import patients,Doctors,Category,category_ph,Pham_model,accountant_model,CatLeve,Laboratory,lab_test
# Register your models here.

admin.site.register(patients)
admin.site.register(Doctors)
admin.site.register(Category)
admin.site.register(category_ph)
admin.site.register(Pham_model)
admin.site.register(accountant_model)
admin.site.register(CatLeve)
admin.site.register(Laboratory)
admin.site.register(lab_test)
