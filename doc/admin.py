from django.contrib import admin
from .models import (
    Book_Apointment_model,
    Decline_note,
    Medical_test,
    Send_report_to_pharmacy,
    confirm_drug,
    chat_model,
    Notification,
    NurseModels,
    Vital_Signs,
)
# Register your models here.


admin.site.register(Book_Apointment_model)
admin.site.register(Decline_note)
admin.site.register(Medical_test)
admin.site.register(Send_report_to_pharmacy)
admin.site.register(confirm_drug)

admin.site.register(chat_model)

admin.site.register(Notification)


admin.site.register(NurseModels)
admin.site.register(Vital_Signs)
