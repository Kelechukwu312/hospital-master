from django.urls import path
from .views import create_doctor_view,doctor_list_view,\
    specialization_view,patients_list_view,\
    edit_specialization_view,\
    delete_specialization_view,\
     doctors_view,\
     patience_book_appointment,\
     patient_pick_cat,\
    pentience_appointment_list_view,\
    doctor_view_patirnt_appointment,\
    doctor_view_app_id,\
     rep_view,\
     doctor_view_app_declined,\
    view_accepted_appointment_list,\
     doctors_list_declined,\
      doctors_manage_patient,\
     delete_doctors_manage_patient,\
     admin_declined_appointment_list_view,\
    create_pham_view,\
    displays_pharmacy_to_admin,\
     pentience_send_view,\
    pentience_view_prescription,\
     pentience_send_prescription_view,\
    pentience_send_prescription_list,\
     pharmacy_view_patient_prescription,\
     pharmacy_view_id_patient,\
     declined_drug_view,\
     phar_view_approved_drug,\
      phar_view_declined_drug,\
     phar_display_pre_drug,\
     prescription_update_pa,\
     prescription_declined_update_pa,\
     prescription_update_pa_id,\
     doctor_change_password_view,\
     pharmacy_change_password,\
     super_admin_delete_view,\
     admin_delete_studdent_view,\
     admin_view_patient,\
     displays_pharmacy_to_admin_edit,\
     pharmac_pro_pic_view,\
     doctor_pro_pic_view,\
     patient_pro_pic_view,\
     admin_view_appointment_ap,\
     admin_view_declined_appointment_ap,\
      admin_view_accepted_prescription_ap,\
     admin_view_declined_prescription_ap,\
     admin_view_pending_appointment_ap,\
     chat_view,\
     reload_chat,\
     dr_chat,\
     dr_send_chat,\
     reload_chat_dr,Send_tophma



app_name = 'create'
urlpatterns = [
    path('create_doctor/', create_doctor_view, name='create_doctor'),
    path('doctors-list/', doctor_list_view, name='doctors-list'),
    path('specialization_view/', specialization_view, name='specialization_view'),
    path('patients-list-view/', patients_list_view, name='patients-list-view'),
    path('edit-spe/<id>/', edit_specialization_view, name="edit-spe"),
    path('delete-specialization/<id>/', delete_specialization_view, name="delete-specialization"),
    path('view-doctor/<id>/', doctors_view, name="view-doctor"),
    path('patience-book-appointment/<id>/', patience_book_appointment, name="patience-book-appointment"),
    path('patient-pick-cat/', patient_pick_cat, name="patient-pick-cat"),
    path('pentience-appointment-list-view/', pentience_appointment_list_view, name="pentience-appointment-list-view"),
    path('doctor-view-patirnt-appointment/<id>/', doctor_view_patirnt_appointment, name="doctor-view-patirnt-appointment"),
    path('doctor-view-app-id/<id>/', doctor_view_app_id, name="doctor-view-app-id"),
    path('rep_view/<id>/', rep_view, name="rep_view"),
    path('doctor-view-app-declined/<id>/', doctor_view_app_declined, name="doctor-view-app-declined"),
    path('view_accepted_appointment_list/',view_accepted_appointment_list, name="view_accepted_appointment_list"),
    path('doctors-list-declined/', doctors_list_declined, name="doctors-list-declined"),


    path('doctors-manage-patient/<id>/', doctors_manage_patient, name="doctors-manage-patient"),

    path('delete-doctors-manage-patient/<id>/',delete_doctors_manage_patient, name="delete-doctors-manage-patient"),
    path('admin-declined-appointment-list_view', admin_declined_appointment_list_view, name="admin-declined-appointment-list-view"),
    path('create-pham-view/',create_pham_view, name="create-pham-view"),
    path('displays-pharmacy-to-admin/',displays_pharmacy_to_admin, name="displays-pharmacy-to-admin"),
    path('pentience-send-view/',pentience_send_view, name="pentience-send-view"),
    path('pentience-view-prescription/<id>/',pentience_view_prescription, name="pentience-view-prescription"),
    path('pentience-send-prescription_view/<id>/',pentience_send_prescription_view, name="pentience-send-prescription-view"),
    path('pentience-send-prescription-list/<id>/',pentience_send_prescription_list, name="pentience-send-prescription-list"),
    path('pharmacy-view-patient-prescription/', pharmacy_view_patient_prescription,name="pharmacy-view-patient-prescription"),
    path('pharmacy-view-id-patient/<uuid:u_id>/', pharmacy_view_id_patient,name="pharmacy-view-id-patient"),



    path('declined-drug-view/<uuid:u_id>/',declined_drug_view, name="declined-drug-view"),

    path('phar-view-approved-drug/',phar_view_approved_drug, name="phar-view-approved-drug"),


    path('phar-view-declined-drug/',phar_view_declined_drug, name="phar-view-declined-drug"),
    path('phar-display-pre-drug/<id>/',phar_display_pre_drug, name="phar-display-pre-drug"),
    path('prescription-update-pa/', prescription_update_pa, name="prescription-update-pa"),
    path('prescription-declined-update-pa/', prescription_declined_update_pa, name="prescription-declined-update-pa"),
    path('prescription-update-pa-id/<id>', prescription_update_pa_id, name="prescription-update-pa-id"),


    path('doctor-change-password-view/', doctor_change_password_view, name="doctor-change-password-view"),
    path('pharmacy-change-password/', pharmacy_change_password, name="pharmacy-change-password"),
    path('super-admin-delete-view/<id>', super_admin_delete_view, name="super-admin-delete-view"),
    path('admin-delete-studdent-view/<id>', admin_delete_studdent_view, name="admin-delete-studdent-view"),

    path('admin-view-patient/<id>', admin_view_patient, name="admin-view-patient"),
    path('displays-pharmacy-to-admin-edit/<id>/', displays_pharmacy_to_admin_edit, name="displays-pharmacy-to-admin-edit"),
    path('pharmac-pro-pic-view', pharmac_pro_pic_view, name="pharmac-pro-pic-view"),
    path('doctor-pro-pic-view', doctor_pro_pic_view, name="doctor-pro-pic-view"),
    path('patient-pro-pic-view', patient_pro_pic_view, name="patient-pro-pic-view"),


    path('admin_view_appointment_ap', admin_view_appointment_ap, name="admin_view_appointment_ap"),
    path('admin_view_declined_appointment_ap', admin_view_declined_appointment_ap, name="admin_view_declined_appointment_ap"),

    path('admin_view_accepted_prescription_ap', admin_view_accepted_prescription_ap, name="admin_view_accepted_prescription_ap"),
    path('admin_view_declined_prescription_ap', admin_view_declined_prescription_ap, name="admin_view_declined_prescription_ap"),

    path('admin_view_pending_appointment_ap', admin_view_pending_appointment_ap, name="admin_view_pending_appointment_ap"),


    #"""this is the chat Url"""
    path('chat-view', chat_view,name="chat_view"),

    # """this is the chat Url"""
    path('reload-chat/<id>/',reload_chat,name="reload_chat"),
    #Dr chat url

    path('dr-chat/',dr_chat, name="dr_chat"),
    path('dr-send-chat',dr_send_chat, name="dr_send_chat"),

    path('reload-chat-dr/<id>/', reload_chat_dr,name="reload_chat_dr"),

    path('Send_tophma/<id>/', Send_tophma, name="Send_tophma"),

]
