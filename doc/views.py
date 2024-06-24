from django.shortcuts import render,reverse,get_object_or_404,redirect
from user.forms import DoctorsForm,Pham_Form
from user.forms import Laboratory_Form
import random
from user.models import Doctors,Category,Pham_model
from django.contrib import messages
from django.http import HttpResponseRedirect
from user.forms import specialization_Form
from user.models import patients
from user.models import lab_test
from doc.models import Medical_test,Send_report_to_pharmacy,Send_report_to_pharmacy,confirm_drug,chat_model
from .models import Book_Apointment_model,Decline_note,Notification,Vital_Signs,Send_report_to_pharmacy
from .forms import pharm_image_form,Doctor_image_form,patient_image_form
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
'''this view creates the Pham'''

def create_pham_view(request):
    #-------------------------------
    user=request.user
    pat_count = patients.objects.all().count()
    doc = Doctors.objects.all().count()
    ph1=Pham_model.objects.all().count()
    book_count = Book_Apointment_model.objects.filter(accepts="Accepted").count()
    book_declined_c = Book_Apointment_model.objects.filter(accepts="Declined").count()
    book_pending_c = Book_Apointment_model.objects.filter(accepts="Pending").count()
    sed_i = confirm_drug.objects.filter(confirm="Unavailable").count()
    sed_w = confirm_drug.objects.filter(confirm="Confirm").count()
    #=============================================================
    pF = Pham_Form(request.POST or None)
    ph=Pham_model.objects.all()
    your_letters='abcdefghi'
    i= ''.join((random.choice(your_letters) for i in range(5)))
    if request.method == "POST":
        if pF.is_valid():
            email = request.POST['email']
            if Pham_model.objects.filter(email=email).exists():
                messages.info(request, "Pharmacist exist")
            else:
                y=pF.save()
                y.password = i
                y.save()
                messages.info(request, "Added Successfully")
                return HttpResponseRedirect(reverse('log:success'))
    context_view={
        'pF':pF,
        'ph':ph,
        'user': user,
        'pat_count': pat_count,
        'doc': doc,
        'ph1': ph1,
        'book_c': book_count,
        'book_declined_c': book_declined_c,
        'book_pending_c': book_pending_c,
        'sed_i': sed_i,
        'sed_w': sed_w,
    }
    return render(request,'add-pha.html', context_view)


def displays_pharmacy_to_admin(request):
    #-------------------------------
    user=request.user
    pat_count = patients.objects.all().count()
    doc = Doctors.objects.all().count()
    ph1=Pham_model.objects.all().count()
    book_count = Book_Apointment_model.objects.filter(accepts="Accepted").count()
    book_declined_c = Book_Apointment_model.objects.filter(accepts="Declined").count()
    book_pending_c = Book_Apointment_model.objects.filter(accepts="Pending").count()
    sed_i = confirm_drug.objects.filter(confirm="Unavailable").count()
    sed_w = confirm_drug.objects.filter(confirm="Confirm").count()
    #=============================================================
    ph = Pham_model.objects.all()
    con_v={
        'ph':ph,
        'user':user,
        'pat_count': pat_count,
        'doc': doc,
        'ph1': ph1,
        'book_c': book_count,
        'book_declined_c': book_declined_c,
        'book_pending_c': book_pending_c,
        'sed_i': sed_i,
        'sed_w': sed_w,
    }
    return render(request,'admin-pharm-list.html',con_v)

def create_doctor_view(request):
    user = request.user
    pat_count = patients.objects.all().count()
    doc = Doctors.objects.all().count()
    ph=Pham_model.objects.all().count()
    book_count = Book_Apointment_model.objects.filter(accepts="Accepted").count()
    book_declined_c = Book_Apointment_model.objects.filter(accepts="Declined").count()
    book_pending_c = Book_Apointment_model.objects.filter(accepts="Pending").count()
    sed_i = confirm_drug.objects.filter(confirm="Unavailable").count()
    sed_w = confirm_drug.objects.filter(confirm="Confirm").count()
    #-----this part holds the templatting count, with no inheritance


    form=DoctorsForm(request.POST or None)
    your_letters='abcdefghi'
    i= ''.join((random.choice(your_letters) for i in range(5)))
    if request.method == "POST":
        if form.is_valid():
            email = request.POST['email']
            if Doctors.objects.filter(email=email).exists():
                messages.info(request, "Doctor exist")
            else:
                y=form.save()
                y.password = i
                y.save()
                messages.info(request, "Add Successfully")
                return HttpResponseRedirect(reverse('create:create_doctor'))
    context_view={
        'form':form,
        #-------------------------
        'user':user,
        'pat_count': pat_count,
        'doc': doc,
        'ph': ph,
        'book_c': book_count,
        'book_declined_c': book_declined_c,
        'book_pending_c': book_pending_c,
        'sed_i': sed_i,
        'sed_w': sed_w,
    }
    return render(request,'add-doctor.html',context_view)

def doctor_list_view(request):
    doctors = Doctors.objects.all()
    #--------------------------------------
    # this is for the template
    user=request.user
    pat_count = patients.objects.all().count()
    doc = Doctors.objects.all().count()
    ph=Pham_model.objects.all().count()
    book_count = Book_Apointment_model.objects.filter(accepts="Accepted").count()
    book_declined_c = Book_Apointment_model.objects.filter(accepts="Declined").count()
    book_pending_c = Book_Apointment_model.objects.filter(accepts="Pending").count()
    sed_i = confirm_drug.objects.filter(confirm="Unavailable").count()
    sed_w = confirm_drug.objects.filter(confirm="Confirm").count()
    context_view={
        'doctors':doctors,
        #----------------
        'user': user,
        'pat_count': pat_count,
        'doc': doc,
        'ph': ph,
        'book_c': book_count,
        'book_declined_c': book_declined_c,
        'book_pending_c': book_pending_c,
        'sed_i': sed_i,
        'sed_w': sed_w,
    }
    return render(request,'doctor-list.html',context_view)

def specialization_view(request):
    #============================
    #template
    user=request.user
    pat_count = patients.objects.all().count()
    doc = Doctors.objects.all().count()
    ph=Pham_model.objects.all().count()
    book_count = Book_Apointment_model.objects.filter(accepts="Accepted").count()
    book_declined_c = Book_Apointment_model.objects.filter(accepts="Declined").count()
    book_pending_c = Book_Apointment_model.objects.filter(accepts="Pending").count()
    sed_i = confirm_drug.objects.filter(confirm="Unavailable").count()
    sed_w = confirm_drug.objects.filter(confirm="Confirm").count()
    form_cat = specialization_Form(request.POST or None)
    """Collecting from Database"""
    category = Category.objects.all()
    if request.method =="POST":
        if form_cat.is_valid:
            form_cat.save()
            messages.info(request, "Add Successfully")
            return HttpResponseRedirect(reverse('create:specialization_view'))

    context_view={
        'category':category,
        'form_cat':form_cat,
        'user': user,
        'pat_count': pat_count,
        'doc': doc,
        'ph': ph,
        'book_c': book_count,
        'book_declined_c': book_declined_c,
        'book_pending_c': book_pending_c,
        'sed_i': sed_i,
        'sed_w': sed_w,
    }
    return render(request,'add-specialization.html',context_view)

'''retriving patients'''

def patients_list_view(request):
    #---------------------
    user=request.user
    pat_count = patients.objects.all().count()
    doc = Doctors.objects.all().count()
    ph=Pham_model.objects.all().count()
    book_count = Book_Apointment_model.objects.filter(accepts="Accepted").count()
    book_declined_c = Book_Apointment_model.objects.filter(accepts="Declined").count()
    book_pending_c = Book_Apointment_model.objects.filter(accepts="Pending").count()
    sed_i = confirm_drug.objects.filter(confirm="Unavailable").count()
    sed_w = confirm_drug.objects.filter(confirm="Confirm").count()
    #----------------------------------

    pat =patients.objects.all()
    context_v={
        'pat':pat,
        #'pat_count':pat_count,
        'user': user,
        'pat_count': pat_count,
        'doc': doc,
        'ph': ph,
        'book_c': book_count,
        'book_declined_c': book_declined_c,
        'book_pending_c': book_pending_c,
        'sed_i': sed_i,
        'sed_w': sed_w,
    }
    return render(request,'patients_list.html',context_v)

def edit_specialization_view(request,id):
    #-------------------------------
    #template
    user=request.user
    pat_count = patients.objects.all().count()
    doc = Doctors.objects.all().count()
    ph=Pham_model.objects.all().count()
    book_count = Book_Apointment_model.objects.filter(accepts="Accepted").count()
    book_declined_c = Book_Apointment_model.objects.filter(accepts="Declined").count()
    book_pending_c = Book_Apointment_model.objects.filter(accepts="Pending").count()
    sed_i = confirm_drug.objects.filter(confirm="Unavailable").count()
    sed_w = confirm_drug.objects.filter(confirm="Confirm").count()
    if request.method == "POST":
        edit = request.POST['edit']
        Category.objects.filter(id=id).update(name=edit)
        messages.info(request, "Edited Successfully")
        return HttpResponseRedirect(reverse('create:specialization_view'))
    con_v={
        'user': user,
        'pat_count': pat_count,
        'doc': doc,
        'ph': ph,
        'book_c': book_count,
        'book_declined_c': book_declined_c,
        'book_pending_c': book_pending_c,
        'sed_i': sed_i,
        'sed_w': sed_w,

    }
    return render(request,'edit-specia.html',con_v)


'''This will be deleting specialization list'''
def delete_specialization_view(request,id):
    """Deleting from Database"""
    cat = Category.objects.get(id=id)
    cat.delete()
    messages.info(request, "Deleted Successfully")
    return HttpResponseRedirect(reverse('create:specialization_view'))

def doctors_view(request,id):
    docc = Doctors.objects.get(id=id)
    #--------------------------------------
    #template
    user=request.user
    pat_count = patients.objects.all().count()
    doc = Doctors.objects.all().count()
    ph=Pham_model.objects.all().count()
    book_count = Book_Apointment_model.objects.filter(accepts="Accepted").count()
    book_declined_c = Book_Apointment_model.objects.filter(accepts="Declined").count()
    book_pending_c = Book_Apointment_model.objects.filter(accepts="Pending").count()
    sed_i = confirm_drug.objects.filter(confirm="Unavailable").count()
    sed_w = confirm_drug.objects.filter(confirm="Confirm").count()
    cont_view={
        'docc':docc,
        #-----------------------
        'user': user,
        'pat_count': pat_count,
        'doc': doc,
        'ph': ph,
        'book_c': book_count,
        'book_declined_c': book_declined_c,
        'book_pending_c': book_pending_c,
        'sed_i': sed_i,
        'sed_w': sed_w,
    }
    return render(request,'view-doctors.html',cont_view)


@csrf_exempt
def patient_pick_cat(request):
    cate = Doctors.objects.all()
    us=request.session['name']
    p = patients.objects.all()
    #pk = request.POST.get('pk')
    #print("print pk with out ajax :",pk)
    #for c in p:
    #    if c.is_authenticate:
    #        answer =True
    #        print("the current Logged User :",c.Firstname, answer,request.session.has_key('name'))
    #    else:
    #        answer =False
    #        print("the current Logged User :",c.Firstname, answer,request.session.has_key('name'))
    print(us)
    userr = patients.objects.get(Firstname=us)
    #chat = chat_model.objects.filter(Q(sender=userr,reciever="naame"))
    #chat=""
    count_t = Book_Apointment_model.objects.filter(patients=userr, accepts="Declined").count()
    count_a = Book_Apointment_model.objects.filter(patients=userr, accepts="Accepted").count()
    Medd = Medical_test.objects.filter(patient=userr).count()
    pre_up = confirm_drug.objects.filter(Send_pharmacy__patient=userr, confirm="Confirm").count()
    pre_up1 = confirm_drug.objects.filter(Send_pharmacy__patient=userr, confirm="Unavailable").count()

    #chat = chat_model.objects.filter(Q(user=userr, other_user=D))
    #D = Doctors.objects.get(id=id)
    chat = chat_model.objects.filter(user=userr)

      #  print("display the content :")

    #print("display user :",D.Firstname)
    answer =None
    '''''''''
    for C in chat:
        if "True" in C.Sender_back:
            print("User Sent This :", C.message)
            answer=C.message
        elif "True" in C.reciever_back:
            print("Dr Sent This :", C.message)
            answerer = C.message
        else:
            print("None :")

          '''
    if request.is_ajax():
        pk = request.POST.get('pk')
        print("The Great Output :", pk)
        dr=Doctors.objects.get(id=pk)

        print()
        print("Print out come :",dr)
        ok ="hello"
        d = dr
        print(d)
        return JsonResponse({'ok':ok,'dr':d.Firstname,'otherN':d.Othername,'image':d.image.url,'dr_id':d.id,'dr_status':d.status})

    context_view = {
        'userr': userr,
        'cate':cate,
        'count_t': count_t,
        'Medd': Medd,
        'count_a': count_a,
        'pre_up': pre_up,
        'pre_up1': pre_up1,
        'chat':chat,

    }
    return render(request,'patient-pick-cat.html',context_view)


'''**This is a view function that handles the sending and receiving  of the chat'''

def chat_view(request):
    us = request.session['name']
    userr = patients.objects.get(Firstname=us)
    if request.is_ajax():
        id = request.POST.get('pk')
        message_c = request.POST.get('message_c')
        dr = Doctors.objects.get(id=id)
        print("All Went Well",dr)

        chat = chat_model()
        chat.message = message_c
        chat.save()
        chat.user=userr
        chat.save()
        chat.other_user = dr
        chat.save()
        chat.Sender_back = True
        chat.save()
        if Notification.objects.filter(pq_message = userr,Dr_notify = dr).exists():
            Notification.objects.filter(pq_message = userr).update(pq_message = userr,Dr_notify = dr,viewed="False")
        else:
            N = Notification()
            N.Dr_notify = dr
            N.save()
            N.pq_message = userr
            N.save()

        context_ajax = {
            #"hello":"hello",
            'id':id,
            'message_c':message_c,
            'user':userr.id,
        }
        return JsonResponse(context_ajax)

def reload_chat(request,id):
    us = request.session['name']
    userr = patients.objects.get(Firstname=us)
    #print("the user id",userr)


    #chat = chat_model.objects.filter(sender=userr)
    D = Doctors.objects.get(id=id)
    #print("the Dr id", D)
    chat = chat_model.objects.filter(Q(user=userr,other_user=D))

    userr = patients.objects.filter(Firstname=us)

    class_name=None
    #all_chat = None
    all_chat = None
    for i in chat:
        #print(i.message)
        if i.reciever_back == "True":
            class_name = "client-chat"
            all_chat = i.message
            print(class_name,all_chat,i.other_user)

        if i.Sender_back == "True":
            class_name = "my-chat"
            all_chat = i.message
            print(class_name,all_chat,i.user)

    #pye = userr

    #if chat_all is userr:
    #    print("hello")

    return JsonResponse({'chat':list(chat.values()),'id':D.id,'class_name':class_name,'all_chat':all_chat}, safe=False)


def patience_book_appointment(request,id):
    #per = specialization_Form(request.POST or None)
    us = request.session['name']
    patie=patients.objects.get(Firstname=us)
    us=request.session['name']
    print(us)

    Bob = Book_Apointment_model()
    dc = Doctors.objects.get(id=id)

    #=====================================================================================
    #This is An update
    userr = patients.objects.get(Firstname=us)
    count_t = Book_Apointment_model.objects.filter(patients=userr, accepts="Declined").count()
    count_a = Book_Apointment_model.objects.filter(patients=userr, accepts="Accepted").count()
    Medd = Medical_test.objects.filter(patient=userr).count()
    pre_up = confirm_drug.objects.filter(Send_pharmacy__patient=userr, confirm="Confirm").count()
    pre_up1 = confirm_drug.objects.filter(Send_pharmacy__patient=userr, confirm="Unavailable").count()
    #=================================================================================================
    if request.method == "POST":
        num = request.POST['num']
        date = request.POST['date']
        ime = request.POST['ime']
        matric = request.POST['matric']
        level = request.POST['level']

        Bob.fee = num
        Bob.save()
        Bob.Date = date
        Bob.save()
        Bob.Time = ime
        Bob.save()
        Bob.doctors=dc
        Bob.save()
        Bob.patients = patie
        Bob.save()
        Bob.matriculationnumber = matric
        Bob.save()
        Bob.level = level
        Bob.save()
        messages.info(request, "Add Successfully")
        return redirect('create:patience-book-appointment',id=id)
    context_v={
       # 'per':per,
        'dc':dc,
        'userr': userr,
        'count_t': count_t,
        'Medd': Medd,
        'count_a': count_a,
        'pre_up': pre_up,
        'pre_up1': pre_up1,
    }

    return render(request,'patient-bookappointment.html',context_v)

def pentience_appointment_list_view(request):
    us = request.session['name']
    patie = patients.objects.get(Firstname=us)
    userr = patients.objects.get(Firstname=us)
    book = Book_Apointment_model.objects.filter(patients=patie)
    bokd = Book_Apointment_model.objects.filter(patients=patie, accepts="Accepted")
    bokd2 = Book_Apointment_model.objects.filter(patients=patie, accepts="Declined")

    #This is An update on the template side
    userr = patients.objects.get(Firstname=us)
    count_t = Book_Apointment_model.objects.filter(patients=userr, accepts="Declined").count()
    count_a = Book_Apointment_model.objects.filter(patients=userr, accepts="Accepted").count()
    Medd = Medical_test.objects.filter(patient=userr).count()
    pre_up = confirm_drug.objects.filter(Send_pharmacy__patient=userr, confirm="Confirm").count()
    pre_up1 = confirm_drug.objects.filter(Send_pharmacy__patient=userr, confirm="Unavailable").count()
    #=================================================================================================

    contex_view={
        'book': book,
        'bokd':bokd,
        'bokd2':bokd2,
        'userr':userr,
        #'count_t':count_t

        'count_t': count_t,
        'Medd': Medd,
        'count_a': count_a,
        'pre_up': pre_up,
        'pre_up1': pre_up1,

    }

    return render(request,'patient-booked-appointment.html',contex_view)

def doctor_view_patirnt_appointment(request,id):
    drop = request.session['pip']
    print(drop)
    link = Doctors.objects.get(Firstname=drop)
    book = Book_Apointment_model.objects.filter(doctors=link, doctors__id=id)
    bokd = Book_Apointment_model.objects.filter(doctors=link,accepts="Accepted")
    b = Book_Apointment_model.objects.filter(doctors__id=id)
    count = Book_Apointment_model.objects.filter(doctors=link, accepts="Pending")
    print("display the count :",count)
    print(b)
    if bokd:
        print("this is accepted")
    else:
        print("Not accepted")
    #===================================
    #For Template View
    link = Doctors.objects.get(Firstname=drop)
    count1 = Book_Apointment_model.objects.filter(doctors=link, accepts="Pending").count()
    print("drag ",link)
    #====================================
    context_v={
        'book':book,
        'bokd': bokd,
        'count':count,

        'user': link,
        'count1': count1,
    }

    return render(request,'doctor-view-appointment.html',context_v)

'''This is the view that accepts appointment from the  doctors side'''
def doctor_view_app_id(request,id):
    drop = request.session['pip']
    print(drop)
    link = Doctors.objects.get(Firstname=drop)
    Book_Apointment_model.objects.filter(doctors=link,id=id).update(accepts="Accepted")
    messages.info(request, "Accepted Successfully")
    return redirect('create:rep_view', id=id)

'''this is the view method that declines an appointment from the doctors side '''

def doctor_view_app_declined(request,id):
    drop = request.session['pip']
    print(drop)
    link = Doctors.objects.get(Firstname=drop)
    #patient = models.ForeignKey(patients,null=True, related_name='patient', blank=True,on_delete=models.SET_NULL)
    #doctors = models.ForeignKey(Doctors, null=True, blank=True, on_delete=models.SET_NULL)
    #book_apointment = models.ForeignKey(patients,null=True, related_name='book', blank=True,on_delete=models.SET_NULL)
    #Note = models.TextField(max_length=500)

'''this is the appointment list view'''
def rep_view(request,id):
    drop = request.session['pip']
    print(drop)
    link = Doctors.objects.get(Firstname=drop)
    Book=Book_Apointment_model.objects.get(id=id)
    Bo = Vital_Signs.objects.filter(bookapointment__id=Book.id)

    print("Dis ",Bo)

    bokd = Book_Apointment_model.objects.filter(doctors=link, accepts="Accepted",id=id)
    dclined = Book_Apointment_model.objects.filter(doctors=link, accepts="Declined", id=id)

    #======================================================================
    #For the Template
    link = Doctors.objects.get(Firstname=drop)
    count1 = Book_Apointment_model.objects.filter(doctors=link, accepts="Pending").count()
    print("drag ",link)
    #-------------------------------------------------------------------------------
    if request.method == "POST" and 'order' in request.POST:
        notice = request.POST['notice']
        Book_Apointment_model.objects.filter(doctors=link, id=id).update(accepts="Declined")
        de=Decline_note()
        de.doctors = link
        de.save()
        de.book_apointment = Book
        de.save()
        de.Note=notice
        de.save()
        messages.info(request, "Declined Successfully")
        return redirect('create:rep_view', id=id)
    if bokd:
        print("this is accepted")
    else:
        print("Not accepted")
    context_v={
        'Book':Book,
        'bokd':bokd,
        'dclined':dclined,


        'user': link,
        'count1': count1,
        'Bo':Bo,
    }
    return render(request, 'doctor-confirm-appointment.html', context_v)


'''this is the view that displays all accepted appointment from a loged
in doctor
'''

def view_accepted_appointment_list(request):
    drop = request.session['pip']
    print(drop)
    link = Doctors.objects.get(Firstname=drop)
    print("road :",link)
    bokd = Book_Apointment_model.objects.filter(doctors=link, accepts="Accepted")
    #Medical_t = Medical_test.objects.get(doctors=link,patient__id=13)
    #print("real ",Medical_t)
    #======================================================================
    #For the Template
    link = Doctors.objects.get(Firstname=drop)
    count1 = Book_Apointment_model.objects.filter(doctors=link, accepts="Pending").count()
    print("drag ",link)
    #-------------------------------------------------------------------------------
    context_view={
        'bokd':bokd,
        #'Medical_t':Medical_t,

        'user': link,
        'count1': count1,
    }
    return render(request,'accepted-appointment.html',context_view)

'''this is the view that manages appointment'''


'''this the list of declined appointment'''
def doctors_list_declined(request):
    drop = request.session['pip']
    print(drop)
    link = Doctors.objects.get(Firstname=drop)
    dic = Decline_note.objects.filter(doctors=link, book_apointment__accepts="Declined")

    #========================================================
    link = Doctors.objects.get(Firstname=drop)
    count1 = Book_Apointment_model.objects.filter(doctors=link, accepts="Pending").count()
    print("drag ",link)
    #-------------------------------------------------------------------------------
    context_view={
        'dic':dic,
        'user': link,
        'count1': count1,
    }
    return render(request,'doctors-declined-appointment.html',context_view)


def doctors_manage_patient(request,id):
    drop = request.session['pip']
    print(drop)
    link = Doctors.objects.get(Firstname=drop)
    B=Book_Apointment_model.objects.get(doctors=link,id=id)
    pr=str(B.patients.Firstname)
    print("This gives the name :",pr)
    Medical_t = Medical_test.objects.filter(doctors=link,Book_Apointment_mo=B)

    #========================================================
    link = Doctors.objects.get(Firstname=drop)
    count1 = Book_Apointment_model.objects.filter(doctors=link, accepts="Pending").count()
    print("drag ",link)
    #-------------------------------------------------------------------------------
    if request.method == "POST" and "lab-button" in request.POST:
        test_result = request.FILES["test_result"]
        test_name = request.POST["test_name"]
        Xy=lab_test()
        Xy.test_result = test_result
        Xy.test_name = test_name
        Xy.save()
        Xy.doctor_key = link
        Xy.patient_key = pr
        Xy,save()
        messaages.info(request, f"Successful")
        return redirect("create:doctors-manage-patient", id = id)
    if request.method == "POST":
        #blood_p = request.POST['blood_p']
        #weight = request.POST['weight']
        #blood_s = request.POST['blood_s']
        #body_t = request.POST['body_t']
        medical_p = request.POST['medical_p']
        med=Medical_test()
        #med.blood_pressure = blood_p
        #med.save()
        #med.Weight = weight
        #med.save()
        #med.blood_sugar = blood_s
        #med.save()
        #med.body_tempreture = body_t
        #med.save()
        med.medical_prescription = medical_p
        med.save()
        med.patient = B.patients
        med.save()
        med.doctors = link
        med.save()
        med.Book_Apointment_mo = B
        med.save()
        messages.info(request, "Medical Report Added Successfully")
        return redirect('create:doctors-manage-patient', id=id)
    context_v={
        'out_p':Medical_t,
        #'R':R,
        'user': link,
        'count1': count1,
    }
    return render(request,'doctor-manage-patients.html',context_v)


def Send_tophma(request,id):
    mke = Medical_test.objects.get(id=id)
    send_r  = Send_report_to_pharmacy()
    send_r.patient = mke.patient
    send_r.save()
    send_r.medical = mke
    send_r.save()
    messages.info(request, "Successfully sent prescription")

    return redirect('create:doctors-manage-patient',id=mke.Book_Apointment_mo.id)


#return redirect("home_m:blog_detail_view", slug=slug, id=id)


def delete_doctors_manage_patient(request,id):
    drop = request.session['pip']
    print(drop)
    link = Doctors.objects.get(Firstname=drop)
    out_p = Medical_test.objects.filter(doctors=link, id=id)
    out_p.delete()
    messages.info(request, "Successfully Deleted Report")
    return redirect('create:view_accepted_appointment_list')

def admin_declined_appointment_list_view(request):
    #-----------------------------------------
    user=request.user
    pat_count = patients.objects.all().count()
    doc = Doctors.objects.all().count()
    ph=Pham_model.objects.all().count()
    book_count = Book_Apointment_model.objects.filter(accepts="Accepted").count()
    book_declined_c = Book_Apointment_model.objects.filter(accepts="Declined").count()
    book_pending_c = Book_Apointment_model.objects.filter(accepts="Pending").count()
    sed_i = confirm_drug.objects.filter(confirm="Unavailable").count()
    sed_w = confirm_drug.objects.filter(confirm="Confirm").count()
    #---------------------------------------------------------------

    Dec = Decline_note.objects.all()
    cont_v={
        'Dec':Dec,
        'user': user,
        'pat_count': pat_count,
        'doc': doc,
        'ph': ph,
        'book_c': book_count,
        'book_declined_c': book_declined_c,
        'book_pending_c': book_pending_c,
        'sed_i': sed_i,
        'sed_w': sed_w,
    }
    return render(request,'declined-patient-list.html',cont_v)




'''this is the view that displays accepted appointment from user'''

def pentience_send_view(request):
    us = request.session['name']
    patie = patients.objects.get(Firstname=us)
    book = Book_Apointment_model.objects.filter(patients=patie)
    userr= patients.objects.get(Firstname=us)
    bokd = Book_Apointment_model.objects.filter(patients=patie, accepts="Accepted")
    #bok = Book_Apointment_model.objects.get(patients=patie, accepts="Accepted")
    #met = Medical_test.objects.get(Book_Apointment_mo=bokd.id)


    print("print this out :",bokd)
    tes = Medical_test.objects.filter(patient=patie)
    print("Test :",tes)

    for i in bokd:
        print("Display This :",i)


    #This is An update on the template side
    userr = patients.objects.get(Firstname=us)
    count_t = Book_Apointment_model.objects.filter(patients=userr, accepts="Declined").count()
    count_a = Book_Apointment_model.objects.filter(patients=userr, accepts="Accepted").count()
    Medd = Medical_test.objects.filter(patient=userr).count()
    pre_up = confirm_drug.objects.filter(Send_pharmacy__patient=userr, confirm="Confirm").count()
    pre_up1 = confirm_drug.objects.filter(Send_pharmacy__patient=userr, confirm="Unavailable").count()
    #=================================================================================================

    contex_view={
        'book': book,
        'bokd':bokd,
        'tes':tes,
        'userr':userr,

        'count_t': count_t,
        'Medd': Medd,
        'count_a': count_a,
        'pre_up': pre_up,
        'pre_up1': pre_up1,

    }
    return render(request,'patient-accepted-appointment.html',contex_view)

'''this view displays the pentience appointment'''

def pentience_view_prescription(request,id):
    us = request.session['name']
    patie = patients.objects.get(Firstname=us)
    B=Book_Apointment_model.objects.get(patients=patie,id=id)
    print("all Out :",B)
    med = Medical_test.objects.get(patient=B.patients,Book_Apointment_mo=B)
    print("med",med)

    #This is An update on the template side
    userr = patients.objects.get(Firstname=us)
    count_t = Book_Apointment_model.objects.filter(patients=userr, accepts="Declined").count()
    count_a = Book_Apointment_model.objects.filter(patients=userr, accepts="Accepted").count()
    Medd = Medical_test.objects.filter(patient=userr).count()
    pre_up = confirm_drug.objects.filter(Send_pharmacy__patient=userr, confirm="Confirm").count()
    pre_up1 = confirm_drug.objects.filter(Send_pharmacy__patient=userr, confirm="Unavailable").count()
    #=================================================================================================

    con_v={
        'userr': userr,

        'count_t': count_t,
        'Medd': Medd,
        'count_a': count_a,
        'pre_up': pre_up,
        'pre_up1': pre_up1,
        'med':med,
    }
    return render(request,'patient-prescription.html',con_v)

'''This is the view that controls the pentience sending of prescription'''

def pentience_send_prescription_list(request,id):
    us = request.session['name']
    patie = patients.objects.get(Firstname=us)
    ser = Pham_model.objects.all()
    B=Book_Apointment_model.objects.get(patients=patie,id=id)
    print("all Out :",B)
    med = Medical_test.objects.get(patient=B.patients,Book_Apointment_mo=B)
    con_v = {
        'ser':ser,
    }
    return render(request,'patient-select-pre.html',con_v)



def pentience_send_prescription_view(request,id):
    us = request.session['name']
    patie = patients.objects.get(Firstname=us)
    Send_m = Medical_test.objects.get(id=id)
    #Medical_tes = Medical_test.objects.get(patient=patie,Book_Apointment_mo=)
    send=Send_report_to_pharmacy.objects.filter(medical__id=Send_m.id)
    if send:
        print("present")
    else:
        print("Not Present")

    userr = patients.objects.get(Firstname=us)
    count_t = Book_Apointment_model.objects.filter(patients=userr, accepts="Declined").count()
    count_a = Book_Apointment_model.objects.filter(patients=userr, accepts="Accepted").count()
    Medd = Medical_test.objects.filter(patient=userr).count()
    pre_up = confirm_drug.objects.filter(Send_pharmacy__patient=userr, confirm="Confirm").count()
    pre_up1 = confirm_drug.objects.filter(Send_pharmacy__patient=userr, confirm="Unavailable").count()
    #=================================================================================================

    if request.method == "POST":
        date = request.POST['date']
        ime = request.POST['ime']
        sen = Send_report_to_pharmacy()
        sen.Date = date
        sen.save()
        sen.Time = ime
        sen.save()
        sen.patient = patie
        sen.save()
        sen.medical =Send_m
        sen.save()
        #python manage,sen.confirm="Confirm"
        messages.info(request, "Prescription Sent Successfully !")
        return redirect('create:pentience-send-prescription-view', id=id)
    con_v={
        'userr':userr,
        'count_t': count_t,
        'Medd': Medd,
        'count_a': count_a,
        'pre_up': pre_up,
        'pre_up1': pre_up1,
        'send':send,
    }
    return render(request,'patient-send-prescrition.html',con_v)


'''This is the view that displays number of sent prescriptions to the Pharmacy '''

def pharmacy_view_patient_prescription(request):
    drop = request.session['pharm']
    print(drop)
    link = Pham_model.objects.get(First_name=drop)
    ser = Send_report_to_pharmacy.objects.all()


    #=================================================================
    sed = confirm_drug.objects.filter(Pham=link,confirm="Pending").count()
    Con_f = confirm_drug.objects.filter(Pham=link, confirm="Confirm").count()
    un_f = confirm_drug.objects.filter(Pham=link, confirm="Unavailable").count()
    #==========================================================================
    con_v = {
        'ser':ser,
        'link':link,
        'sed': sed,
        'Con_f': Con_f,
        'un_f': un_f,

    }
    return render(request,'pharmacy-view-prescription.html',con_v)


'''This is the view that picks a patient who sent a prescription Order '''

def pharmacy_view_id_patient(request,u_id):
    #ser_id = Send_report_to_pharmacy.objects.get(id=id)
    drop = request.session['pharm']
    print(drop)
    link = Pham_model.objects.get(First_name=drop)
    se_id = Send_report_to_pharmacy.objects.get(medical__u_id=u_id)
    print("Work It :",se_id)
    c_drug=confirm_drug.objects.filter(Pham=link,Send_pharmacy__medical__u_id=u_id,confirm="Confirm")
    '''this is the part that checks if it is declined'''
    c_drug2 = confirm_drug.objects.filter(Pham=link, Send_pharmacy__medical__u_id=u_id, confirm="Unavailable")
    print("this is for drug :",c_drug)

    #=================================================================
    sed = confirm_drug.objects.filter(Pham=link,confirm="Pending").count()
    Con_f = confirm_drug.objects.filter(Pham=link, confirm="Confirm").count()
    un_f = confirm_drug.objects.filter(Pham=link, confirm="Unavailable").count()
    #==========================================================================

    Med= Send_report_to_pharmacy.objects.get(medical__u_id=u_id)
    if request.method == 'POST':
        text_in = request.POST['text_in']
        textarea_in = request.POST['textarea_in']
        c_drug = confirm_drug()
        c_drug.confirm = "Confirm"
        c_drug.save()
        c_drug.Pham = link
        c_drug.save()
        c_drug.Send_pharmacy = Med
        c_drug.save()
        c_drug.drug_price = text_in
        c_drug.save()
        c_drug.drug_name =textarea_in
        c_drug.save()
        messages.info(request, "Confirm Successfully !")
        return redirect('create:pharmacy-view-id-patient', u_id=u_id)
    con_v={
        'link':link,
       'se_id':se_id,
       'c_drug':c_drug,
        'c_drug2':c_drug2,
        'sed': sed,
        'Con_f': Con_f,
        'un_f': un_f,

    }
    return render(request,'pharmacy-confirm-prescription.html',con_v)


'''this is the view that confirms drug request'''
'''
def confirm_drug_view(request,u_id):
    drop = request.session['pharm']
    print(drop)
    link = Pham_model.objects.get(First_name=drop)

        return redirect('create:pharmacy-view-id-patient', u_id=u_id)

'''


'''this is th view that decline drug request'''

def declined_drug_view(request,u_id):
    drop = request.session['pharm']
    print(drop)
    link = Pham_model.objects.get(First_name=drop)
    Med= Send_report_to_pharmacy.objects.get(medical__u_id=u_id)
    #print(med)
    c_drug = confirm_drug()
    c_drug.confirm = "Unavailable"
    c_drug.save()
    c_drug.Pham = link
    c_drug.save()
    c_drug.Send_pharmacy = Med
    c_drug.save()
    messages.info(request, "Confirm Successfully !")
    return redirect('create:pharmacy-view-id-patient', u_id=u_id)


'''this is the view that displays all approved prescriptions '''
def phar_view_approved_drug(request):


    drop = request.session['pharm']
    print(drop)
    link = Pham_model.objects.get(First_name=drop)
    sed = confirm_drug.objects.filter(Pham=link, confirm="Confirm")
    #=================================================================
    seds = confirm_drug.objects.filter(Pham=link,confirm="Pending").count()
    Con_f = confirm_drug.objects.filter(Pham=link, confirm="Confirm").count()
    un_f = confirm_drug.objects.filter(Pham=link, confirm="Unavailable").count()
    #==========================================================================
    contex_v={
        'seds':seds,
        'sed': sed,
        'link':link,
        'Con_f': Con_f,
        'un_f': un_f,
    }
    return render(request,'pharma-view-approved-drug.html', contex_v)


'''this is the view that displays all Declined prescriptions '''

def phar_view_declined_drug(request):
    drop = request.session['pharm']
    print(drop)
    link = Pham_model.objects.get(First_name=drop)
    sed = confirm_drug.objects.filter(Pham=link, confirm="Unavailable")

    #=================================================================
    seds = confirm_drug.objects.filter(Pham=link,confirm="Pending").count()
    Con_f = confirm_drug.objects.filter(Pham=link, confirm="Confirm").count()
    un_f = confirm_drug.objects.filter(Pham=link, confirm="Unavailable").count()
    #==========================================================================

    contex_v={
        'link':link,
        'sed':sed,
        'seds':seds,
        'Con_f':Con_f,
         'un_f':un_f,
    }
    return render(request,'pharma-view-declined-drug.html', contex_v)

def phar_display_pre_drug(request,id):
    drop = request.session['pharm']
    print(drop)
    link = Pham_model.objects.get(First_name=drop)
    sed = confirm_drug.objects.get(Pham=link, confirm="Confirm",id=id)
    #=================================================================
    seds = confirm_drug.objects.filter(Pham=link,confirm="Pending").count()
    Con_f = confirm_drug.objects.filter(Pham=link, confirm="Confirm").count()
    un_f = confirm_drug.objects.filter(Pham=link, confirm="Unavailable").count()
    #==========================================================================
    cont_v={
        'sed':sed,
        'seds': seds,
        'link': link,
        'Con_f': Con_f,
        'un_f': un_f,
    }
    return render(request,'pharm-pres-con-dru.html',cont_v)


def prescription_update_pa(request):
    us = request.session['name']
    patie = patients.objects.get(Firstname=us)
    userr = patients.objects.get(Firstname=us)
    sed = confirm_drug.objects.filter(Send_pharmacy__patient=patie, confirm="Confirm")
    print("lets get it out :",sed)
    #===========================================
    #template update
    userr = patients.objects.get(Firstname=us)
    count_t = Book_Apointment_model.objects.filter(patients=userr, accepts="Declined").count()
    count_a = Book_Apointment_model.objects.filter(patients=userr, accepts="Accepted").count()
    Medd = Medical_test.objects.filter(patient=userr).count()
    pre_up = confirm_drug.objects.filter(Send_pharmacy__patient=userr, confirm="Confirm").count()
    pre_up1 = confirm_drug.objects.filter(Send_pharmacy__patient=userr, confirm="Unavailable").count()
    #=================================================================================================

    cont_v={
        'sed':sed,

        'userr': userr,
        'count_t': count_t,
        'Medd': Medd,
        'count_a': count_a,
        'pre_up': pre_up,
        'pre_up1': pre_up1,
    }
    return render(request,'patient-prescription-update.html',cont_v)

def prescription_declined_update_pa(request):
    us = request.session['name']
    patie = patients.objects.get(Firstname=us)
    userr = patients.objects.get(Firstname=us)
    sed = confirm_drug.objects.filter(Send_pharmacy__patient=patie, confirm="Unavailable")
    print("lets get it out :",sed)

    #===========================================
    #template update
    userr = patients.objects.get(Firstname=us)
    count_t = Book_Apointment_model.objects.filter(patients=userr, accepts="Declined").count()
    count_a = Book_Apointment_model.objects.filter(patients=userr, accepts="Accepted").count()
    Medd = Medical_test.objects.filter(patient=userr).count()
    pre_up = confirm_drug.objects.filter(Send_pharmacy__patient=userr, confirm="Confirm").count()
    pre_up1 = confirm_drug.objects.filter(Send_pharmacy__patient=userr, confirm="Unavailable").count()
    #=================================================================================================
    cont_v={
        'sed':sed,
        'userr': userr,
        'count_t': count_t,
        'Medd': Medd,
        'count_a': count_a,
        'pre_up': pre_up,
        'pre_up1': pre_up1,
    }
    return render(request,'patient-declined-update.html',cont_v)

def home_qual_view(request):
    return render(request,'home-qualified.html')

def prescription_update_pa_id(request,id):
    us = request.session['name']
    patie = patients.objects.get(Firstname=us)
    rull = confirm_drug.objects.get(Send_pharmacy__patient=patie, confirm="Confirm",id=id)

    #===========================================
    #template update
    userr = patients.objects.get(Firstname=us)
    count_t = Book_Apointment_model.objects.filter(patients=userr, accepts="Declined").count()
    count_a = Book_Apointment_model.objects.filter(patients=userr, accepts="Accepted").count()
    Medd = Medical_test.objects.filter(patient=userr).count()
    pre_up = confirm_drug.objects.filter(Send_pharmacy__patient=userr, confirm="Confirm").count()
    pre_up1 = confirm_drug.objects.filter(Send_pharmacy__patient=userr, confirm="Unavailable").count()
    #=================================================================================================
    cont_v={
        'rull':rull,
        'userr': userr,
        'count_t': count_t,
        'Medd': Medd,
        'count_a': count_a,
        'pre_up': pre_up,
        'pre_up1': pre_up1,
    }
    return render(request,'prescription_up_pa_id.html',cont_v)


'''this view Changes the Doctors password'''

def doctor_change_password_view(request):
    #========================================================
    drop = request.session['pip']
    link = Doctors.objects.get(Firstname=drop)
    count1 = Book_Apointment_model.objects.filter(doctors=link, accepts="Pending").count()
    print("drag ",link)
    #-------------------------------------------------------------------------------
    if request.method == "POST":
        old_pass = request.POST['old_pass']
        new_pass = request.POST['new_pass']
        if not Doctors.objects.filter(password=old_pass):
            messages.info(request, "Password Do Not Match!")
            return redirect('create:doctor-change-password-view')
        elif Doctors.objects.filter(password=old_pass):
            Doctors.objects.filter(password=old_pass).update(password=new_pass)
            messages.info(request, "Password Changed Successfully !")
            return redirect('create:doctor-change-password-view')
    contex_v={
        'user': link,
        'count1': count1,
    }
    return render(request,'doctor-change-password.html',contex_v)


'''this view changes the pharmacy password'''

def pharmacy_change_password(request):
    drop = request.session['pharm']
    link = Pham_model.objects.get(First_name=drop)
    #=================================================================
    seds = confirm_drug.objects.filter(Pham=link,confirm="Pending").count()
    Con_f = confirm_drug.objects.filter(Pham=link, confirm="Confirm").count()
    un_f = confirm_drug.objects.filter(Pham=link, confirm="Unavailable").count()
    #==========================================================================
    if request.method == "POST":
        old_pass = request.POST['old_pass']
        new_pass = request.POST['new_pass']
        if not Pham_model.objects.filter(password=old_pass):
            messages.info(request, "Password Do Not Match!")
            return redirect('create:pharmacy-change-password')
        elif Pham_model.objects.filter(password=old_pass):
            Pham_model.objects.filter(password=old_pass).update(password=new_pass)
            messages.info(request, "Password Changed Successfully !")
            return redirect('create:pharmacy-change-password')
    cont_v={'link':link,'seds':seds,'Con_f':Con_f,'un_f':un_f}
    return render(request,'pharmacy-change-password.html',cont_v)


'''This view Super-admin delete Doctor'''

def super_admin_delete_view(request,id):
    doc = Doctors.objects.get(id=id)
    doc.delete()
    messages.info(request, "Deleted Successfully !")
    return redirect('create:doctors-list')

'''this view deletes the patient '''

def admin_delete_studdent_view(request,id):
    pat=patients.objects.get(id=id)
    pat.delete()
    messages.info(request, "Deleted Successfully !")
    return redirect('create:patients-list-view')

'''this is the view that views the  patient from the admin'''

def admin_view_patient(request,id):
    #------------------------------
    user=request.user
    pat_count = patients.objects.all().count()
    doc = Doctors.objects.all().count()
    ph=Pham_model.objects.all().count()
    book_count = Book_Apointment_model.objects.filter(accepts="Accepted").count()
    book_declined_c = Book_Apointment_model.objects.filter(accepts="Declined").count()
    book_pending_c = Book_Apointment_model.objects.filter(accepts="Pending").count()
    sed_i = confirm_drug.objects.filter(confirm="Unavailable").count()
    sed_w = confirm_drug.objects.filter(confirm="Confirm").count()
    #----------------------------------------------------------

    pat = patients.objects.get(id=id)
    context_view={
        'pat':pat,
        'user': user,
        'pat_count': pat_count,
        'doc': doc,
        'ph': ph,
        'book_c': book_count,
        'book_declined_c': book_declined_c,
        'book_pending_c': book_pending_c,
        'sed_i': sed_i,
        'sed_w': sed_w,
    }
    return render(request,'admin-view-patient.html',context_view)


def displays_pharmacy_to_admin_edit(request,id):
    #------------------------------
    user=request.user
    pat_count = patients.objects.all().count()
    doc = Doctors.objects.all().count()
    ph=Pham_model.objects.all().count()
    book_count = Book_Apointment_model.objects.filter(accepts="Accepted").count()
    book_declined_c = Book_Apointment_model.objects.filter(accepts="Declined").count()
    book_pending_c = Book_Apointment_model.objects.filter(accepts="Pending").count()
    sed_i = confirm_drug.objects.filter(confirm="Unavailable").count()
    sed_w = confirm_drug.objects.filter(confirm="Confirm").count()
    #----------------------------------------------------------
    if request.method == "POST":
        firstname = request.POST['firstname']
        othername = request.POST['othername']
        email = request.POST['email']
        Pham_model.objects.filter(id=id).update(First_name=firstname,Other_name=othername,email=email)
        messages.info(request, "Edited Successfully !")
        return redirect('create:displays-pharmacy-to-admin')
    context_view={
        'user': user,
        'pat_count': pat_count,
        'doc': doc,
        'ph': ph,
        'book_c': book_count,
        'book_declined_c': book_declined_c,
        'book_pending_c': book_pending_c,
        'sed_i': sed_i,
        'sed_w': sed_w,
    }
    return render(request,'edit-phamacy.html',context_view)


'''patience Adding profile pictures to a profile'''

def pharmac_pro_pic_view(request):
    drop = request.session['pharm']
    link = Pham_model.objects.get(First_name=drop)
    #=================================================================
    seds = confirm_drug.objects.filter(Pham=link,confirm="Pending").count()
    Con_f = confirm_drug.objects.filter(Pham=link, confirm="Confirm").count()
    un_f = confirm_drug.objects.filter(Pham=link, confirm="Unavailable").count()
    #==========================================================================
    pham_model=Pham_model.objects.get(First_name=link)
    if request.method == "POST":
        u_form = pharm_image_form(request.POST, request.FILES, instance=link)
        if u_form.is_valid():
            u_form.save()
            messages.info(request, "Uploaded Successfully !")
            return redirect('create:pharmac-pro-pic-view')
    else:
        u_form = pharm_image_form(instance=link)

    cont_v={
        'link':link,
        'seds':seds,
        'Con_f':Con_f,
        'un_f':un_f,
        'u_form':u_form,
        'pham_model':pham_model,
    }
    return render(request,'pharmac-pro-pic.html',cont_v)


'''doctor Adding profile pictures to a profile'''


def doctor_pro_pic_view(request):
    #========================================================
    drop = request.session['pip']
    link = Doctors.objects.get(Firstname=drop)
    count1 = Book_Apointment_model.objects.filter(doctors=link, accepts="Pending").count()
    print("drag ",link)
    #-------------------------------------------------------------------------------
    doctors = Doctors.objects.get(Firstname=link)
    if request.method == "POST":
        u_form = Doctor_image_form(request.POST, request.FILES, instance=link)
        if u_form.is_valid():
            u_form.save()
            messages.info(request, "Uploaded Successfully !")
            return redirect('create:doctor-pro-pic-view')
    else:
        u_form = pharm_image_form(instance=link)

    cont_v={
        'user': link,
        'count1': count1,
        'u_form':u_form,
        'doctor':doctors,
    }
    return render(request,'doctor-pro-pic.html',cont_v)


'''patient adding profile pictures to profile'''


def patient_pro_pic_view(request):
    us = request.session['name']
    userr = patients.objects.get(Firstname=us)
    count_t = Book_Apointment_model.objects.filter(patients=userr, accepts="Declined").count()
    count_a = Book_Apointment_model.objects.filter(patients=userr, accepts="Accepted").count()
    Medd = Medical_test.objects.filter(patient=userr).count()
    pre_up = confirm_drug.objects.filter(Send_pharmacy__patient=userr, confirm="Confirm").count()
    pre_up1 = confirm_drug.objects.filter(Send_pharmacy__patient=userr, confirm="Unavailable").count()
    #=================================================================================================

    Patients = patients.objects.get(Firstname=userr)
    if request.method == "POST":
        u_form = patient_image_form(request.POST, request.FILES, instance=userr)
        if u_form.is_valid():
            u_form.save()
            messages.info(request, "Uploaded Successfully !")
            return redirect('create:patient-pro-pic-view')
    else:
        u_form = pharm_image_form(instance=userr)

    cont_v={
        'u_form':u_form,
        'userr': userr,
        'count_t': count_t,
        'Medd': Medd,
        'count_a': count_a,
        'pre_up': pre_up,
        'pre_up1': pre_up1,
        'Patients':Patients,
    }
    return render(request,'patient-pro-pic.html',cont_v)

'''this is the view that displays Accepted Appointment'''
def admin_view_appointment_ap(request):
    #-------------------------------------------
    user=request.user
    pat_count = patients.objects.all().count()
    doc = Doctors.objects.all().count()
    ph=Pham_model.objects.all().count()
    book_count1 = Book_Apointment_model.objects.filter(accepts="Accepted").count()
    book_declined_c = Book_Apointment_model.objects.filter(accepts="Declined").count()
    book_pending_c = Book_Apointment_model.objects.filter(accepts="Pending").count()
    sed_i = confirm_drug.objects.filter(confirm="Unavailable").count()
    sed_w = confirm_drug.objects.filter(confirm="Confirm").count()
    #---------------------------------------------------------

    book = Book_Apointment_model.objects.filter(accepts="Accepted")
    book_count = Book_Apointment_model.objects.filter(accepts="Accepted").count()
    con_v={
        'book':book,
        'book_c1':book_count1,
        'user': user,
        'pat_count': pat_count,
        'doc': doc,
        'ph': ph,
        'book_c': book_count,
        'book_declined_c': book_declined_c,
        'book_pending_c': book_pending_c,
        'sed_i': sed_i,
        'sed_w': sed_w,

    }
    return render(request,'admin-view-accepted-ap.html',con_v)


'''this is the view that displays Declined Appointment to the Admin'''
def admin_view_declined_appointment_ap(request):
    #-------------------------------------------
    user=request.user
    pat_count = patients.objects.all().count()
    doc = Doctors.objects.all().count()
    ph=Pham_model.objects.all().count()
    book_count = Book_Apointment_model.objects.filter(accepts="Accepted").count()
    book_declined_c = Book_Apointment_model.objects.filter(accepts="Declined").count()
    book_pending_c = Book_Apointment_model.objects.filter(accepts="Pending").count()
    sed_i = confirm_drug.objects.filter(confirm="Unavailable").count()
    sed_w = confirm_drug.objects.filter(confirm="Confirm").count()
    #----------------------------------------------------
    book = Book_Apointment_model.objects.filter(accepts="Declined")
    con_v={
        'book':book,
        'user': user,
        'pat_count': pat_count,
        'doc': doc,
        'ph': ph,
        'book_c': book_count,
        'book_declined_c': book_declined_c,
        'book_pending_c': book_pending_c,
        'sed_i': sed_i,
        'sed_w': sed_w,

     }
    return render(request,'admin-view-declined-ap.html',con_v)

'''this the view that displays Approved prescriptions'''

def admin_view_accepted_prescription_ap(request):
    #---------------------------------------------------------
    user=request.user
    pat_count = patients.objects.all().count()
    doc = Doctors.objects.all().count()
    ph=Pham_model.objects.all().count()
    book_count = Book_Apointment_model.objects.filter(accepts="Accepted").count()
    book_declined_c = Book_Apointment_model.objects.filter(accepts="Declined").count()
    book_pending_c = Book_Apointment_model.objects.filter(accepts="Pending").count()
    sed_i = confirm_drug.objects.filter(confirm="Unavailable").count()
    sed_w = confirm_drug.objects.filter(confirm="Confirm").count()
    #---------------------------------------------------------------
    sed = confirm_drug.objects.filter(confirm="Confirm")
    con_v={
        'sed':sed,

        'user': user,
        'pat_count': pat_count,
        'doc': doc,
        'ph': ph,
        'book_c': book_count,
        'book_declined_c': book_declined_c,
        'book_pending_c': book_pending_c,
        'sed_i': sed_i,
        'sed_w': sed_w,

     }
    return render(request,'admin_view_accepted_pre.html',con_v)


'''this the view that displays Approved prescriptions'''

def admin_view_declined_prescription_ap(request):
    #----------------------------------------------
    user=request.user
    pat_count = patients.objects.all().count()
    doc = Doctors.objects.all().count()
    ph=Pham_model.objects.all().count()
    book_count = Book_Apointment_model.objects.filter(accepts="Accepted").count()
    book_declined_c = Book_Apointment_model.objects.filter(accepts="Declined").count()
    book_pending_c = Book_Apointment_model.objects.filter(accepts="Pending").count()
    sed_i = confirm_drug.objects.filter(confirm="Unavailable").count()
    sed_w = confirm_drug.objects.filter(confirm="Confirm").count()
    #-------------------------------------------------------------
    sed = confirm_drug.objects.filter(confirm="Unavailable")
    con_v={
        'sed':sed,
        'user': user,
        'pat_count': pat_count,
        'doc': doc,
        'ph': ph,
        'book_c': book_count,
        'book_declined_c': book_declined_c,
        'book_pending_c': book_pending_c,
        'sed_i': sed_i,
        'sed_w': sed_w,

     }
    return render(request,'admin-view-declined_accepted.html',con_v)


'''this the view that displays pending prescriptions'''

def admin_view_pending_appointment_ap(request):
    #--------------------------------------
    #template
    user=request.user
    pat_count = patients.objects.all().count()
    doc = Doctors.objects.all().count()
    ph=Pham_model.objects.all().count()
    book_count = Book_Apointment_model.objects.filter(accepts="Accepted").count()
    book_declined_c = Book_Apointment_model.objects.filter(accepts="Declined").count()
    book_pending_c = Book_Apointment_model.objects.filter(accepts="Pending").count()
    sed_i = confirm_drug.objects.filter(confirm="Unavailable").count()
    sed_w = confirm_drug.objects.filter(confirm="Confirm").count()
    boo_p = Book_Apointment_model.objects.filter(accepts="Pending")
    con_v={
        'boo_p':boo_p,
        'user': user,
        'pat_count': pat_count,
        'doc': doc,
        'ph': ph,
        'book_c': book_count,
        'book_declined_c': book_declined_c,
        'book_pending_c': book_pending_c,
        'sed_i': sed_i,
        'sed_w': sed_w,

     }
    return render(request,'admin-view-pending-appointment_ap.html',con_v)
@csrf_exempt
def dr_chat(request):
    drop = request.session['pip']
    D = Doctors.objects.get(Firstname=drop)

    noti = Notification.objects.filter(Dr_notify=D)
    Notification.objects.filter(Dr_notify=D).update(viewed=True)
    if request.is_ajax():
        pk = request.POST.get('pk')
        noti = Notification.objects.get(pq_message=pk)
        print("I saw it :",pk)
        context_ajax={
            'hello':'hello',
            'firstname':noti.pq_message.Firstname,
            'Othername':noti.pq_message.Othername,
            'image': noti.pq_message.image.url,
            'id': noti.pq_message.id
        }
        return JsonResponse(context_ajax)
    contex_view ={
        'chat':noti,

    }

    return render(request,'chat.html',contex_view)
def dr_send_chat(request):
    drop = request.session['pip']
    D = Doctors.objects.get(Firstname=drop)
    if request.is_ajax():
        id = request.POST.get('pk')
        message_c = request.POST.get('message_c')
        pc = patients.objects.get(id=id)
        print("All Went Well",pc)
        print("message content :",message_c)
        print("Id of patient:",id)

        chat = chat_model()
        chat.message = message_c
        chat.save()
        chat.user=pc
        chat.save()
        chat.other_user = D
        chat.save()
        chat.reciever_back = True
        chat.save()

        context_ajax = {
            #"hello":"hello",
            'id':id,
            'message_c':message_c,
            'D':D.id,
        }
        return JsonResponse(context_ajax)



def reload_chat_dr(request,id):
    drop = request.session['pip']
    D = Doctors.objects.get(Firstname=drop)
    #print("the user id",userr)


    #chat = chat_model.objects.filter(sender=userr)
    PA = patients.objects.get(id=id)
    #print("the Dr id", D)
    chat = chat_model.objects.filter(Q(user=PA,other_user=D))
    dr = Doctors.objects.filter(Firstname=drop)

    class_name=None
    #all_chat = None
    all_chat = None
    for i in chat:
        #print(i.message)
        if i.reciever_back == "True":
            class_name = "client-chat"
            all_chat = i.message
            print(class_name,all_chat,i.other_user)

        if i.Sender_back == "True":
            class_name = "my-chat"
            all_chat = i.message
            print(class_name,all_chat,i.user)

    #pye = userr

    #if chat_all is userr:
    #    print("hello")

    return JsonResponse({'chat':list(chat.values()),'id':PA.id,'class_name':class_name,'all_chat':all_chat}, safe=False)



