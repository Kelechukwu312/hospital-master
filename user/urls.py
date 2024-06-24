from django.urls import path
from .views import Doc_login_view,success_view,Doc_logout_view,\
    user_signup_view,patients_login_view,patients_success_view\
    ,doc_success_view,doctormain_login_view,pharmacy_login_view,\
    pharmacy_home_view,home_qual_view,doctor_logout_view,patient_logout_view,pharm_logout_view,Nurse_login_view,Nurse_dashboard,nurse_bookind_detail,LaboratoryUser,laboratory_dashboard
app_name="log"
urlpatterns = [
    path('login/', Doc_login_view, name='login'),
    path('success/', success_view, name='success'),
    path('logout/', Doc_logout_view, name='logout'),
    path('user-signup/', user_signup_view,name='user-signup'),
    path('patients_login/',patients_login_view, name='patients_login'),
    path('patients_success/', patients_success_view, name='patients_success'),
    path('doctor-main-success/', doc_success_view, name='doctor-main-success'),
    path('doctormain-login-view/', doctormain_login_view, name='doctormain-login-view'),
    path('pharmacy-login-view/', pharmacy_login_view, name='pharmacy-login-view'),
    path('pharmacy-home-view/', pharmacy_home_view, name='pharmacy-home-view'),
    path('home-qual-view/', home_qual_view, name='home-qual-view'),
    path('doctor-logout-view/', doctor_logout_view, name='doctor-logout-view'),
    path('patient-logout-view/', patient_logout_view, name='patient-logout-view'),
    path('pharm-logout-view/', pharm_logout_view, name='pharm-logout-view'),
    path('lab-user/', LaboratoryUser, name='lab-user'),
    path('lab-dashboard/', laboratory_dashboard, name='lab-dashboard'),
    path('Nurse-login-view',Nurse_login_view, name="Nurse_login_view"),

    path('Nurse_dashboard', Nurse_dashboard, name="Nurse_dashboard"),

    path('nurse_bookind_detail', nurse_bookind_detail, name="nurse_bookind_detail"),

]
