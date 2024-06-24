from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,reverse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from .models import patients
from .models import Doctors,Pham_model,CatLeve
from doc.models import Category,Medical_test,Send_report_to_pharmacy,Notification
from doc.models import Book_Apointment_model,confirm_drug,NurseModels,Vital_Signs
from .models import Laboratory
from doc.forms import ask_form

from django.contrib.auth.models import User
# Create your views here.



'''creating doc Login'''

def Doc_login_view(request):
    if request.method == "POST":
        user = request.POST['user']
        passe = request.POST['passe']
        print("printing out user",user)
        print("printing out passe", passe)
        if user == "" and passe == "":
            messages.info(request,"Fill The Fields!")
        elif not authenticate(username=user,password=passe):
            messages.info(request, "Error!")
        else:
            keep=authenticate(username=user,password=passe)
            login(request, keep)
            return HttpResponseRedirect(reverse('log:success'))
    context_view={

    }
    return render(request,'login.html')

@login_required
def success_view(request):
    user=request.user
    pat_count = patients.objects.all().count()
    doc = Doctors.objects.all().count()
    ph=Pham_model.objects.all().count()
    book_count = Book_Apointment_model.objects.filter(accepts="Accepted").count()
    book_declined_c = Book_Apointment_model.objects.filter(accepts="Declined").count()
    book_pending_c = Book_Apointment_model.objects.filter(accepts="Pending").count()
    sed_i = confirm_drug.objects.filter(confirm="Unavailable").count()
    sed_w = confirm_drug.objects.filter(confirm="Confirm").count()

    context_view ={
        'user':user,
        'pat_count':pat_count,
        'doc':doc,
        'ph':ph,
        'book_c':book_count,
        'book_declined_c':book_declined_c,
        'book_pending_c':book_pending_c,
        'sed_i':sed_i,
        'sed_w':sed_w,

    }
    return render(request,'success.html',context_view)

def Doc_logout_view(request):
    #user=request.user
    logout(request)
    return HttpResponseRedirect(reverse('log:login'))


'''User signup'''
def user_signup_view(request):
    ca = CatLeve.objects.get(Name='Patient')

    if request.method == "POST":
        FirstN = request.POST['FirstN']
        otherN = request.POST['otherN']
        email = request.POST['email']
        pas = request.POST['pas']
        conP = request.POST['conP']
        #level = request.POST['level']
        print(pas)
        print(conP)

        if patients.objects.filter(Email=email):
            messages.info(request, "user already signup!")
        elif conP not in pas:
            messages.info(request, "Password Error!")
        else:
            add_p = patients()
            add_p.Firstname = FirstN
            add_p.save()
            add_p.Othername=otherN
            add_p.save()
            add_p.Email = email
            add_p.save()
            add_p.password = pas
            add_p.save()
            add_p.category_level = ca
            add_p.save()
            return HttpResponseRedirect(reverse('log:patients_login'))
    return render(request,'user-signup.html')

def patients_login_view(request):
    name=None

    if request.method == "POST":
        ca = CatLeve.objects.get(Name='Patient')
        catwo = CatLeve.objects.get(Name='Dr')
        cathree = CatLeve.objects.get(Name='pharmacist')
        cafour = CatLeve.objects.get(Name='Nurse')

        if patients.objects.filter(category_level=ca):
            email = request.POST['email']
            passe = request.POST['passe']
            if not patients.objects.filter(Email=email):
                messages.info(request, "Incorrect Email!")
            elif not patients.objects.filter(Email=email, password=passe):
                messages.info(request, "Incorrect Password!")
            else:
                keys = patients.objects.get(Email=email, password=passe)
                keep = str(keys)
                request.session['name'] = keep
                if request.session.has_key('name'):
                    messages.info(request, "Logedin!")
                    return HttpResponseRedirect(reverse('log:patients_success'))
                else:
                    return render(request, 'patients_login.html')

        if Doctors.objects.filter(category_level=catwo):
            email = request.POST['email']
            passe = request.POST['passe']
            if not Doctors.objects.filter(email=email):
                messages.info(request, "Incorrect Email")
            elif not Doctors.objects.filter(email=email, password=passe):
                messages.info(request, "Incorrect Password")
            else:
                king = Doctors.objects.get(email=email, password=passe)
                k = str(king)
                request.session['pip'] = k
                if request.session.has_key('pip'):
                    messages.info(request, "logedin !")
                    log = Doctors.objects.filter(email=email).update(status="True")
                    return HttpResponseRedirect(reverse('log:doctor-main-success'))
                else:
                    return render(request, 'doctor-login.html')

        if Pham_model.objects.filter(category_level=cathree):
            email = request.POST['email']
            passe = request.POST['passe']
            if not Pham_model.objects.filter(email=email):
                messages.info(request, "Incorrect Email")
            elif not Pham_model.objects.filter(email=email, password=passe):
                messages.info(request, "Incorrect Password")
            else:
                king = Pham_model.objects.get(email=email, password=passe)
                k = str(king)
                request.session['pharm'] = k
                if request.session.has_key('pharm'):
                    messages.info(request, "logedin !")
                    return HttpResponseRedirect(reverse('log:pharmacy-home-view'))
                else:
                    return render(request, 'doctor-login.html')

        if NurseModels.objects.filter(category_level=cafour):
            email = request.POST['email']
            passe = request.POST['passe']
            if not NurseModels.objects.filter(email=email):
                messages.info(request, "Incorrect Email!")
            elif not NurseModels.objects.filter(email=email, password=passe):
                messages.info(request, "Incorrect Password!")
            else:
                keys = NurseModels.objects.get(email=email, password=passe)
                keep = str(keys)
                request.session['nurse'] = keep
                if request.session.has_key('nurse'):
                    messages.info(request, "Logedin!")
                    return HttpResponseRedirect(reverse('log:Nurse_dashboard'))
                else:
                    return render(request, 'patients_login.html')

    return render(request,'patients_login.html')



def patients_success_view(request):
    if not request.session.has_key('name'):
        return HttpResponseRedirect(reverse('log:patients_login'))
    elif request.session.has_key('name'):
        us = request.session['name']
        print(us)
        userr = patients.objects.get(Firstname=us)
        count_t = Book_Apointment_model.objects.filter(patients=userr, accepts="Declined").count()
        count_a = Book_Apointment_model.objects.filter(patients=userr, accepts="Accepted").count()
        Medd = Medical_test.objects.filter(patient=userr).count()
        pre_up = confirm_drug.objects.filter(Send_pharmacy__patient=userr, confirm="Confirm").count()
        pre_up1 = confirm_drug.objects.filter(Send_pharmacy__patient=userr, confirm="Unavailable").count()
        pre = confirm_drug.objects.filter(Send_pharmacy__patient=userr, confirm="Confirm")
        print("this :",pre)
        print("\n")

        if request.method == "POST" and 'ph' in request.POST:
            #formF = request.FILES.get('formF', False)
            formF = request.POST['formF']

            userr.med_history = formF
            userr.save()
            messages.info(request, "Successful Upload!")
            return HttpResponseRedirect(reverse('log:patients_success'))
        context_view = {
            'userr': userr,
            'count_t': count_t,
            'Medd': Medd,
            'count_a': count_a,
            'pre_up': pre_up,
            'pre_up1': pre_up1,
        }
        return render(request,'index.html',context_view)


def doctormain_login_view(request):
    pip = None
    if request.method == "POST":
        email = request.POST['email']
        passe = request.POST['passe']
        if not Doctors.objects.filter(email=email):
            messages.info(request, "Incorrect Email")
        elif not Doctors.objects.filter(email=email,password=passe):
            messages.info(request, "Incorrect Password")
        else:
            king = Doctors.objects.get(email=email,password=passe)
            k = str(king)
            request.session['pip'] = k
            if request.session.has_key('pip'):
                messages.info(request,"logedin !")
                log = Doctors.objects.filter(email=email).update(status="True")
                return HttpResponseRedirect(reverse('log:doctor-main-success'))
            else:
                return render(request, 'doctor-login.html')
    return render(request,'doctor-login.html')

def doc_success_view(request):
    if not request.session.has_key('pip'):
        return HttpResponseRedirect(reverse('log:doctormain-login-view'))

    elif request.session.has_key('pip'):

        drop = request.session['pip']
        print(drop)
        link = Doctors.objects.get(Firstname=drop)
        noti = Notification.objects.filter(Dr_notify=link)
        count = Book_Apointment_model.objects.filter(doctors=link, accepts="Pending").count()
        print("drag ", link)
        hw = Category.objects.filter(doctors__category__name='Dermatologist')
        print('this is printed', hw)
        context_view = {
            'user': link,
            'count': count,
            'noti':noti.first()

        }
        return render(request, 'doctors-home.html', context_view)






'''Pharmacist authentication view'''
def pharmacy_login_view(request):
    pharm = None
    if request.method == "POST":
        email = request.POST['email']
        passe = request.POST['passe']
        if not Pham_model.objects.filter(email=email):
            messages.info(request, "Incorrect Email")
        elif not Pham_model.objects.filter(email=email,password=passe):
            messages.info(request, "Incorrect Password")
        else:
            king = Pham_model.objects.get(email=email,password=passe)
            k = str(king)
            request.session['pharm'] = k
            if request.session.has_key('pharm'):
                messages.info(request,"logedin !")
                return HttpResponseRedirect(reverse('log:pharmacy-home-view'))
            else:
                return render(request, 'doctor-login.html')
    context_v={

    }
    return render(request,'doctor-login.html',context_v)

'''pharmacy home page view'''


#Nurse login

def Nurse_dashboard(request):
    if request.session.has_key('nurse'):
        us = request.session['nurse']
        ussas = NurseModels.objects.get(First_name=us)

        context_view = {
            'userr':ussas

        }
        return render(request, 'nurse_dashboard.html', context_view)
    else:
        return render(request, 'nurse_dashboard.html')






def Nurse_login_view(request):

    nurse=None
    if request.method == "POST":
        email = request.POST['email']
        passe = request.POST['passe']
        if not NurseModels.objects.filter(email=email):
            messages.info(request, "Incorrect Email!")
        elif not NurseModels.objects.filter(email=email, password=passe):
            messages.info(request, "Incorrect Password!")
        else:
            keys=NurseModels.objects.get(email=email, password=passe)
            keep = str(keys)
            request.session['nurse'] = keep
            if request.session.has_key('nurse'):
                messages.info(request, "Logedin!")
                return HttpResponseRedirect(reverse('log:Nurse_dashboard'))
            else:
                return render(request, 'patients_login.html')
    return render(request,'nurse_login.html')


def nurse_bookind_detail(request):
    if request.session.has_key('nurse'):
        us = request.session['nurse']
        ussas = NurseModels.objects.get(First_name=us)


        ask_f = ask_form(request.POST or None)
        vital_s = Vital_Signs.objects.all()
        if request.method == "POST" and 'signup' in request.POST:
            if ask_f.is_valid():
                temperature = request.POST['temperature']
                heart_rate = request.POST['heart_rate']
                blood_pressure = request.POST['blood_pressure']
                admitted_date = request.POST['admitted_date']
                discharge_date = request.POST['discharge_date']
                bookapointment = ask_f.cleaned_data.get('bookapointment')

                vital_signs = Vital_Signs()
                vital_signs.temperature = temperature
                vital_signs.save()
                vital_signs.heart_rate = heart_rate
                vital_signs.save()
                vital_signs.blood_pressure = blood_pressure
                vital_signs.save()
                vital_signs.admitted_date = admitted_date
                vital_signs.save()
                vital_signs.discharged_date = discharge_date
                vital_signs.save()
                vital_signs.bookapointment = bookapointment
                vital_signs.save()
                messages.info(request, "Successful, Booking Registered!")
                return HttpResponseRedirect(reverse('log:nurse_bookind_detail'))

        context_view = {
            'ask_f': ask_f,
            'vital_s': vital_s,
            'userr': ussas

        }
        return render(request, 'booking-detail.html', context_view)






def pharmacy_home_view(request):
    if not request.session.has_key('pharm'):
        return HttpResponseRedirect(reverse('log:pharmacy-login-view'))
    elif request.session.has_key('pharm'):
        drop = request.session['pharm']
        print(drop)
        link = Pham_model.objects.get(First_name=drop)
        re_send=Send_report_to_pharmacy.objects.all().count()
        sed = confirm_drug.objects.filter(Pham=link, confirm="Pending").count()
        Con_f = confirm_drug.objects.filter(Pham=link, confirm="Confirm").count()
        un_f = confirm_drug.objects.filter(Pham=link, confirm="Unavailable").count()
        print("dispaly the number :",re_send)
        context_v = {
            'link': link,
            'sed': sed,
            'Con_f': Con_f,
            'un_f': un_f,
            're_send':re_send,

        }
        return render(request, 'pharmacy-home.html', context_v)


def home_page_view(request):
    return render(request,'home-page.html')

def home_qual_view(request):
    return render(request,'home-qualified.html')


'''Doctors Logout view'''
def doctor_logout_view(request):
    #doc = Doctors.objects.get(id=id)
    Dr_k = request.session['pip']
    log = Doctors.objects.filter(Firstname=Dr_k).update(status="False")

    del request.session['pip']

    return HttpResponseRedirect(reverse('log:doctormain-login-view'))


'''patient logout view'''
def patient_logout_view(request):
    #doc = Doctors.objects.get(id=id)
    del request.session['name']
    return HttpResponseRedirect(reverse('log:patients_login'))

'''pharm logout view'''
def pharm_logout_view(request):
    #doc = Doctors.objects.get(id=id)
    del request.session['pharm']
    return HttpResponseRedirect(reverse('log:pharmacy-login-view'))


def LaboratoryUser(request):
    lab_user = None
    if request.method == "POST":
        email = request.POST['email']
        passe = request.POST['passe']
        if not Laboratory.objects.filter(email=email).exists():
            messages.info(request, "Incorrect Email!")
        elif not Laboratory.objects.filter(email=email, password=passe).exists():
            messages.info(request, "Incorrect Password!")
        else:
            lab_user = Laboratory.objects.get(email=email, password=passe)
            request.session['laboratory'] = lab_user.id
            if request.session.has_key('laboratory'):
                messages.info(request, "Logged in!")
                return HttpResponseRedirect(reverse('log:lab-dashboard'))
            else:
                return render(request, 'lab-login.html')
    return render(request, 'lab-login.html')
     
def laboratory_dashboard(request):
    return render(request, "lab-dashboard.html")

