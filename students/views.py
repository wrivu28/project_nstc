from builtins import ValueError, object

from django.contrib.auth.decorators import login_required
from django.forms import ValidationError
from django.shortcuts import render
from django.urls import reverse_lazy

from . import addons
from .models import FormFills, Student
from collections import UserDict
from macpath import pathsep
from students.models import Class10, FormFills


# TODO:
# 1. school 10 and 12

def demo(request):
    return render(request, 'students/details.html/')


@login_required(login_url=reverse_lazy('login'))
def general_details(request):
    if request.method == "POST":
        error = ""
        filled_forms = FormFills.get(id=request.user.username)
        if filled_forms.is_gen_details_filled:
            error = "Can't Overwrite existing data!"
        else:
            stud = Students.objects.get(id=request.user.username)
            dob = request.POST['dob'].split()
            blood_type = request.POST['blood_type'].split()
            # HOUSE DETAILS
            guard = request.POST['guard'].split()
            perm_add = request.POST['perm_add'].split()
            loc_guard = request.POST['loc_guard'].split()
            loc_add = request.POST['loc_add'].split()
            # CONTACT NOs
            land_phone = request.POST['land_phone'].split()
            g_mob_no = request.POST['g_mob_no'].split()
            mob_no = request.POST['mob_no'].split()
            # SCHOOL DETAILS
            # Class 10
            sc10_name = request.POST['sc10_name'].split()
            sc10_med = request.POST['sc10_med'].split()
            sc10_marks = request.POST['sc10_marks'].split()
            sc10_year = request.POST['sc10_year'].split()
            sc10_add = request.POST['sc10_add'].split()
            # Class 12
            sc12_name = request.POST['sc12_name'].split()
            sc12_med = request.POST['sc12_med'].split()
            sc12_marks = request.POST['sc12_marks'].split()
            sc12_year = request.POST['sc12_year'].split()
            sc12_add = request.POST['sc12_add'].split()
            # DIPLOMA SCORE
            if stud.is_lateral:
                dip_score = request.POST['dip_score'].split()
            else:
                dip_score = -1

            if '' in [dob, blood_type, guard, perm_add, g_mob_no, mob_no, sc10_name, sc10_med, sc10_marks, sc10_year, sc10_add, sc12_name, sc12_med, sc12_marks, sc12_year, sc12_add, dip_score]:
                error = "All Compulsory Fields must be filled!"
            
            # land phone no verification
            try:
                land_phone = int(land_phone)
                if len(str(land_phone)) > 11:
                    error = "Land phone number too long!"
                elif len(str(land_phone)) == 8:
                    error = ["Please provide STD code for Land phone.", "example: 03322222222"]
                elif len(str(land_phone)) < 8:
                    error = "Land phone number too short!"
            except ValueError:
                error = "land phone number can't contain charecters!"

            # mobile no verification
            try:
                g_mob_no = int(g_mob_no)
                mob_no = int(mob_no)
                
                if len(str(mob_no)) != 10 or len(str(g_mob_no)) != 10:
                    error = "Mobile Number must be equal to 10 digits!"
            except ValueError:
                error = ["Mobile phone number can't contain characters!", "Tip: No need for country code: (eg. +91 in India)"]

            if sc12_year - sc10_year < 2:
                error = "How did you pass class 10 and 12 in less then 2 years? Magic??"

            elif sc10_marks > 100 or sc12_marks > 100:
                error = "How did you get more than 100 in boards? Good handwriting?"

            elif sc10_marks < 30 or sc12_marks < 30:
                error = "Well, your board marks are fishy! contact Mentor or reCheck!"
            
            if not error:
                stud = Student.object.get(id=request.user.username)
                details = Details.object.create(card_no=request.user.username, dob=dob, blood_grp=blood_type, guardian=guard, perm_add=perm_add, loc_guardian=loc_guard, loc_add=loc_add, land_phone=land_phone, guardian_mobile_no=g_mob_no, mobile_no=mob_no)
                if stud.is_lateral:
                    details.diploma_score = dip_score
                    details.save()
                sc10 = Class10.objects.create(student=request.user.username, medium=sc10_med, school_name=sc10_name, passing_year=sc10_year, school_address=sc10_add, score=sc10_marks)
                sc10 = Class12.objects.create(student=request.user.username, medium=sc12_med, school_name=sc12_name, passing_year=sc12_year, school_address=sc12_add, score=sc12_marks)
                forms = FormFills.objects.get(student=request.user.username)
                form.is_gen_details_filled = True
                form.save()
   
    # for GET request
    else:
        filled_forms = FormFills.get(id=request.user.username)
        stud = Students.objects.get(id=request.user.username)
        details = addons.get_idcard_details(request.user.username)
        details['title'] = 'Student Details'
        details['is_lateral'] = stud.is_lateral

        if filled_forms.is_gen_details_filled:
            details['filled'] = True
        else:
            details['filled'] = False

        return render(request, 'students/details.html/', details)


@login_required(login_url=reverse_lazy('login'))
def univ_details(request):
    if request.method == "POST":
        error = ""
        admin_no = request.POST['admin_no'].strip()
        reg_no = request.POST['reg_no'].strip()

        if admin_no is '' or reg_no is '':
            error = ["Who has blank admission and/or Registration numbers?", "stop fooling arround"]
        try:
            admin_no = int(admin_no)
            reg_no = int(reg_no)
        except ValueError:
            error = "Enter only Whole Numbers"
        
        user = request.user.username
        try:
            stud = Student.objects.get(id=user)
        except:
            error = "ERROR finding the student"

        # If already filled, fail loudly!
        if stud.admission_no or stud.registration_no:
            error = "Can't Overwrite existing data!"

        if not error:
            stud.admission_no = admin_no
            stud.registration_no = reg_no
            stud.save()
            error = "Entry saved successfully!"

        _ = []
        if type(error) != type(_):
            error = [error]
        return render(request, 'accounts/message.html', {'messages': error}) 
        
    else:
        d = {
            'title': '404 Error',
            'cute_img': '<img src="http://www.404notfound.fr/assets/images/pages/img/androiddev101.jpg" />'
        }
        return render(request, 'accounts/message.html', d) 

