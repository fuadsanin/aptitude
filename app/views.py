from ast import Or
from django.db.models import Q
from django.shortcuts import redirect, render
from django.contrib.auth.models import auth, User
from django.contrib.auth import authenticate
from app.models import *
from aptitude.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.views.defaults import page_not_found
from django.contrib import messages
import random
import json
from datetime import datetime

def Register(request):
   if request.method == 'POST':
        fname = request.POST['fname']
        email = request.POST['email']
        contact = request.POST['contact']
        qualification = request.POST['qualifcation']
        passoutyr = request.POST['passoutyr']
        username = fname
        password = random.randint(10000, 99999)
        reference = request.POST['reference']
        dept = request.POST['dept']
        if candidates.objects.filter(email=email).exists():
         messages.warning(request,'Email already exists')
         return redirect('/regdetails')
        else:
         register = candidates(fullname=fname, email=email, contact_no=contact,
                              qualifications=qualification, passout_year=passoutyr,
                              username=username, password=password, reference = reference, deptmnt_id=dept, regdate=datetime.now())
         register.save()
         messages.success(
         request, 'username and password for exam is sent to your registered mail id.........')
         member = candidates.objects.get(id=register.id)
         subject = 'Greetings from iNFOX TECHNOLOGIES'
         message = 'Congratulations,\n' \
            'You have successfully registered with iNFOX TECHNOLOGIES.\n' \
            'following is your login credentials for taking aptitude test\n'\
            'username :'+str(member.username)+'\n' 'password :'+str(member.password) + \
            '\n' 'ALL THE BEST WISHES FOR YOUR TEST ' + \
            '\n' 'Login to test :http://127.0.0.1:8000/'
         recepient = str(email)
         send_mail(subject, message, EMAIL_HOST_USER,
                  [recepient], fail_silently=False)
         msg_success = "Registration completed Check Your Mail"
         return render(request,'user_registration.html',{'msg_success':msg_success})
                  
   else:
      des = designation.objects.get(designation='HR')
      vars = login.objects.filter(designation_id=des.id)
      vars1 = department.objects.all()
      return render(request, 'user_registration.html', {'var': vars, 'vars1': vars1})
   
def regdetails(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        email = request.POST['email']
        contact = request.POST['contact']
        qualification = request.POST['qualifcation']
        passoutyr = request.POST['passoutyr']
        username = fname
        password = random.randint(10000, 99999)
        reference = request.POST['reference']
        dept = request.POST['dept']
        if candidates.objects.filter(email=email).exists():
         messages.warning(request,'Email already exists')
         return redirect('/regdetails')
        else:
         register = candidates(fullname=fname, email=email, contact_no=contact,
                              qualifications=qualification, passout_year=passoutyr,
                              username=username, password=password, reference=reference, deptmnt_id=dept, regdate=datetime.now())
         register.save()
         messages.success(
         request, 'username and password for exam is sent to your registered mail id.........')
         member = candidates.objects.get(id=register.id)
         subject = 'Greetings from iNFOX TECHNOLOGIES'
         message = 'Congratulations,\n' \
            'You have successfully registered with iNFOX TECHNOLOGIES.\n' \
            'following is your login credentials for taking aptitude test\n'\
            'username :'+str(member.username)+'\n' 'password :'+str(member.password) + \
            '\n' 'ALL THE BEST WISHES FOR YOUR TEST ' + \
            '\n' 'Login to test :http://127.0.0.1:8000/'
         recepient = str(email)
         send_mail(subject, message, EMAIL_HOST_USER,
                  [recepient], fail_silently=False)
    else:
        pass
    return render(request, 'user_registration.html')

def Login(request):
    des = designation.objects.get(designation='HR')
    if request.method == 'POST':
        if candidates.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            mem = candidates.objects.get(
                password=request.POST['password'], username=request.POST['username'])
            request.session['username'] = mem.username
            request.session['username1'] = mem.id
            request.session['username2'] = mem.exam_status
            request.session['username3'] = mem.email
            request.session['username4'] = mem.deptmnt_id
            username = request.session['username']
            username1 = request.session['username1']
            username2 = request.session['username2']
            username3 = request.session['username3']
            username4 = request.session['username4']
            sn = 0
            c = catagory.objects.all()
            for i in c:
                sn = sn+i.time_taken
            if username2 == '0':
                return render(request, 'aptitude_instructions.html', {'username': username, 'sn': sn})
            else:
                return redirect('/')
        if login.objects.filter(fullname=request.POST['username'], password=request.POST['password'], designation_id=des.id).exists():
            member = login.objects.get(
                fullname=request.POST['username'], password=request.POST['password'])
            request.session['usernamehr'] = member.designation_id
            request.session['usernamehr1'] = member.fullname
            request.session['usernamehr2'] = member.id   

            return render(request, 'hrsec.html', {'member': member})
        elif request.method == 'POST':
            username = request.POST.get('username', None)
            password = request.POST.get('password', None)
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('admin_dashboard')
        else:
            messages.info(request, 'invalid username')
            return render(request, 'user_login.html')
    else:
        pass
    return render(request, 'user_login.html')  
    
# def aptitude_start(request):
#     if 'username1' in request.session:
#       if request.session.has_key('username'):
#         username = request.session['username']
#       if request.session.has_key('username1'):
#         username1 = request.session['username1']
#       else:
#         username = "dummy"
#       vars = question.objects.all().order_by('?')
#       v = candidates.objects.get(id = username1)
#       m=adminlimit.objects.latest('id')
#       mm = m.time_taken    
#       return render(request,'aptitude_start.html',{'vars':vars,'username':username, 'v':v, 'mm':mm})
#     else:
#       return redirect('/')
    
def aptitude_catagory(request):
    if 'username1' in request.session:
        if request.session.has_key('username'):
            username = request.session['username']
        if request.session.has_key('username1'):
            username1 = request.session['username1']
        if request.session.has_key('username2'):
            username2 = request.session['username2']
        else:
            username = "dummy"
        sn = 0
        c = catagory.objects.all()
        for i in c:
          sn = sn+i.time_taken
        m = catagory.objects.values()
        return render(request, 'aptitude_catagory.html', {'username': username, 'm': m,'sn':sn})
    else:
        return redirect('/')

def start(request,id):
    if 'username1' in request.session:
        if request.session.has_key('username'):
            username = request.session['username']
        if request.session.has_key('username1'):
            username1 = request.session['username1']
        if request.session.has_key('username4'):
            username4 = request.session['username4']
        else:
            username = "dummy"
        var = catagory.objects.get(id=id)
        vars = question.objects.filter(ctgry_id=var.id).order_by('?')
        j = vars.count()
        if int(var.no_of_question) >= j:
            return render(request, 'aptitude_start.html', {'vars': vars,  'username': username,'var': var})
        else:
            return redirect('/aptitude_catagory')
    else:
        return redirect('/')

def saved(request,id):
    print("hai")
    if 'username1' in request.session:
        if request.session.has_key('username1'):
            username1 = request.session['username1']
        if request.session.has_key('username3'):
            username3 = request.session['username3']
        else:
            username1 = "dummy"
        if request.method == 'POST':
            vars = catagory.objects.get(id=id)
            time = vars.id
            user = username1
            x = time_out(category_id=time,user_id=user,exam_status=1)
            x.save()
            ques1 = question.objects.filter(ctgry_id=vars.id).values()
            score = 0
            try:
                    dct = json.loads(request.POST['myval'])
                    flag = True
            except:
                    dct = {}
                    flag = False
            for item in ques1:
                    if flag and item['questions'] in dct['dct'].keys():
                        option = dct['dct'][item['questions']].replace(' ', '')

                    elif request.POST.get(item['questions']):
                        option = request.POST.get(
                            item['questions']).replace(' ', '')
                    else:
                        option = ''

                    if item['correct_option'].replace(' ', '') == option:
                        score = score+10
                        print(score)

                    else:
                        pass
            user = candidates.objects.get(id=username1)
            user.mark = score+user.mark
            user.exam_status = 1
            user.save()
            print(user.mark)
            msg_success = "This section completed"
            return render(request,'aptitude_start.html',{'msg_success':msg_success})
          
def total(request):
    if 'username1' in request.session:
        if request.session.has_key('username'):
            username = request.session['username']
        if request.session.has_key('username1'):
            username1 = request.session['username1']
        if request.session.has_key('username3'):
            username3 = request.session['username3']
        else:
            username = "dummy"
        user = candidates.objects.get(id=username1)
        subject = 'Thankyou For taking Online test'
        message = 'Congratulations,\n' \
                 'You have successfully completed online aptitude test.\n' \
                  'If you got selected you will contacted by Hr shortly.\n' \
                 'All the best !!!'
        send_mail(subject, message, EMAIL_HOST_USER,
                       [username3], fail_silently=False)
    return redirect ('/')

#******************ADMIN AND HR ******************
    
def logout(request):
    auth.logout(request)
    return redirect("/") 

def admin_dashboard(request):
      mem = User.objects.all()
      vars = designation.objects.get(designation='ADMIN')
      var = login.objects.get(designation_id=vars.id)
      return render(request, 'admin_dashboard.html', {'mem': mem,'vars':var})
    
def Dashboard(request):
      mem = User.objects.all()
      return render(request, 'Dashboard.html', {'mem': mem})
   
def add_question(request):
      mem = User.objects.all()
      vars=catagory.objects.all()
      var=department.objects.all()
      z= question()
      if request.method == 'POST':
        z.questions = request.POST['question']
        z.option1 = request.POST['opt1']
        z.option2 = request.POST['opt2']
        z.option3 = request.POST['opt3']
        z.option4 = request.POST['opt4']
        z.correct_option = request.POST['answer']
        a= request.POST['form_select']
        ab=catagory.objects.get(name=a) 
        c= request.POST['Categorysel']
        print(a)
        print(c)
        abc=department.objects.get(name=c)
        z.ctgry_id=ab.id  
        z.dept_id=abc.id
        z.save()
        return redirect('Dashboard')
      return render(request, 'add_question.html', {'mem': mem ,'z': z,'vars': vars,'var':var,})
  
def admin_add_limit(request):
      mem = User.objects.all()
      z= adminlimit()
      if request.method == 'POST':
        z.no_of_question = request.POST['noqstn']
        z.time_taken = request.POST['appt']
        z.save()
        return redirect('Dashboard')
      return render(request, 'admin_add_limit.html', {'mem': mem })

def view_questions(request,id1,id2):
      var = department.objects.get(id=id1)
      var1 = catagory.objects.get(id=id2)
      mem = User.objects.all()
      i= question.objects.filter(ctgry_id=var1.id,dept_id=var.id)
      return render(request, 'view_questions.html', {'mem': mem, 'i':i})
  
def view_question_update(request,id):
      mem = User.objects.all()
      if request.method == 'POST':
        vars = question.objects.get(id=id)
        vars.questions = request.POST['question']
        vars.option1 = request.POST['opt1']
        vars.option2 = request.POST['opt2']
        vars.option3 = request.POST['opt3']
        vars.option4 = request.POST['opt4']
        vars.correct_option = request.POST['answer'] 
        vars.save()
        return redirect("Dashboard")
      return render(request, 'view_questions.html', {'mem': mem })
   
def view_question_delete(request,id):
      mem = User.objects.all()
      var = question.objects.filter(id=id)
      var.delete()
      return redirect("Dashboard")
  
def admin_allMembers(request):
      mem = User.objects.all()
      des = designation.objects.get(designation='HR')
      desgn = login.objects.filter(designation_id=des.id)
      var = candidates.objects.all()
      return render(request, 'admin_allMembers.html', {'mem': mem, 'var':var, 'desgn':desgn})
   

def admin_allMembers_reference(request):
      mem = User.objects.all()
      desgn =candidates.objects.all()
      j = request.POST['refer']
      if request.method == 'POST':
            ref = request.POST['refer']
            if request.POST.get('att'):
                  vi=request.POST.get('att')
                  vi=str(vi)
                  l=len(vi)
                  vii=vi[0:l-1]
                  present=vii.split(",")
                  key=[] 
                  for i in present:
                        key.append(i)
                  for i in key:
                        new = candidates.objects.get(id=i)
                        new.reference = ref
                        new.save()
                  return redirect('admin_allMembers')
      return render(request, 'admin_allMembers.html', {'mem': mem, 'desgn':desgn})
  

def NO_ref(request):
      mem = User.objects.all()
      des = designation.objects.get(designation='HR')
      desgn = login.objects.filter(designation_id=des.id)
      var = candidates.objects.filter( Q(reference='no reference') | Q(reference='Select HR'))
      return render(request, 'NO_ref.html', {'mem': mem, 'var':var, 'desgn':desgn})


def BY_ref(request):
      mem = User.objects.all()
      des = designation.objects.get(designation='HR')
      desgn = login.objects.filter(designation_id=des.id)
      var = candidates.objects.all().exclude(reference='no reference')
      return render(request, 'BY_ref.html', {'mem': mem, 'var':var, 'desgn':desgn})


def HR(request):
      mem = User.objects.all()
      return render(request, 'HR.html', {'mem': mem})
   

def HR_view(request):
      mem = User.objects.all()
      des = designation.objects.get(designation='HR')
      m=login.objects.filter(designation_id= des).exclude(fullname='no reference')
      return render(request, 'HR_view.html', {'mem': mem , 'm':m})
  

def  HR_view_update(request,id):
      mem = User.objects.all()
      if request.method == 'POST':
        vars = login.objects.get(id=id)
        vars.fullname = request.POST['hrname']
        vars.email = request.POST['hrmail']
        vars.contact_no = request.POST['hrcontact'] 
        vars.save()
        return redirect("HR_view")
      return render(request, 'HR_view.html', {'mem': mem })
   
def HR_add(request):
      mem = User.objects.all()
      des = designation.objects.get(designation='HR')
      m=login.objects.filter(designation_id= des)
      reg = login()
      if request.method == 'POST':
        reg.fullname = request.POST['name']
        reg.email = request.POST['email']
        reg.contact_no = request.POST['number']
        reg.designation_id =des.id
        reg.image = request.FILES['img']
        random_otp = random.randint(100,10000)
        reg.password = reg.fullname+str(random_otp)
        reg.save()
        lg = login.objects.get(id = reg.id )
        subject = 'Greetings from iNFOX TECHNOLOGIES'
        message = 'Congratulations,\n' \
                   'You have successfully registered with iNFOX TECHNOLOGIES.\n' \
                   'following is your login credentials\n'\
                   'username :'+str(lg.fullname)+'\n' 'password :'+str(lg.password)+'\n' 'Login :https://careerinfoxtechnologies.com/';
        recepient=str(reg.email)
        send_mail(subject,message,EMAIL_HOST_USER,[recepient],fail_silently=False)
        return redirect('HR_view')
      return render(request, 'HR_add.html', {'mem': mem , 'm':m})
  
def HR_view_delete(request,id):
      mem = User.objects.all()
      var = login.objects.filter(id=id)
      var.delete()
      return redirect('HR_view')
    
def hr_dashboard(request):
     if 'usernamehr2' in request.session:
        if request.session.has_key('usernamehr'):
            usernamehr = request.session['usernamehr']
        if request.session.has_key('usernamehr1'):
                  usernamehr1 = request.session['usernamehr1']
        else:
                  usernamehr1 = "dummy"
        mem = login.objects.filter(
                  designation_id=usernamehr) .filter(fullname=usernamehr1)   
        return render(request, 'hr_dashboard.html', {'mem': mem})
     else:
            return redirect('/')

def hr_allMembers(request):
 if 'usernamehr2' in request.session:
      if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
      if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
      else:
        usernamehr1 = "dummy"
      mem = login.objects.filter(
        designation_id=usernamehr) .filter(fullname=usernamehr1)   
      m=candidates.objects.filter(reference=usernamehr1)
      return render(request, 'hr_allMembers.html', {'m':m, 'mem':mem})
 else:
      return redirect('/')

def admin_question_view(request):
      cat=catagory.objects.all()
      mem = User.objects.all()
      return render(request, 'admin_question_view.html', {'mem': mem ,'cat':cat})

def admin_question_view_dep(request,id):
      var = catagory.objects.get(id=id)
      print(var.id)
      mem = User.objects.all()
      dep= department.objects.all()
      return render(request, 'admin_question_view_dep.html', {'mem': mem , 'dep':dep, 'var':var,})

def admin_question_category(request):    
      mem = User.objects.all()
      return render(request, 'admin_question_category.html', {'mem': mem})    

def admin_view_category(request):
      mem = User.objects.all()
      z = catagory.objects.all()
      return render(request, 'admin_view_category.html', {'mem': mem, 'z':z})

def admin_view_update(request,id):
      mem = User.objects.all()
      if request.method == 'POST':
        vars = catagory.objects.get(id=id)
        vars.name = request.POST['namecat']
        vars.no_of_question = request.POST['noqstn']
        vars.time_taken = request.POST['cattime']
        vars.save()
        return redirect("admin_view_category")
      return render(request, 'admin_view_category.html', {'mem': mem })

def admin_view_delete(request,id):
      mem = User.objects.all()
      var = catagory.objects.filter(id=id)
      var.delete()
      return redirect('admin_view_category')
   
def admin_add_question(request):
      mem = User.objects.all()
      z = catagory()
      if request.method == 'POST':
        z.name = request.POST['namecat']
        z.no_of_question = request.POST['noqstn']
        z.time_taken = request.POST['cattime']
        z.save()
        return redirect('admin_question_category')
      return render(request, 'admin_add_question.html', {'mem': mem})



#**********************HR Module****************************************************************

def hr_allMembers_category(request, id):
 if 'usernamehr2' in request.session:
      if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
      if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
      else:
        usernamehr1 = "dummy"
      mem = login.objects.filter(
        designation_id=usernamehr) .filter(fullname=usernamehr1)
      vars = department.objects.get(id=id)

      cnt1 = candidates.objects.filter(reference = usernamehr1, deptmnt_id=vars.id,contact_status=0).count()
      cnt2 = candidates.objects.filter(reference = usernamehr1, deptmnt_id=vars.id,contact_status=1).count()
      cnt3 = candidates.objects.filter(reference = usernamehr1, deptmnt_id=vars.id).exclude(replay_status=0).count()
      cnt4 = candidates.objects.filter(reference = usernamehr1, deptmnt_id=vars.id,replay_status=1).count()    
      cnt5 = candidates.objects.filter(reference = usernamehr1, deptmnt_id=vars.id,replay_status=2).count()

      m = candidates.objects.filter(reference =usernamehr1)
      return render(request, 'hr_allMembers_category.html', {'m':m, 'mem':mem,'cnt1':cnt1,'cnt2':cnt2,'cnt3':cnt3,'cnt4':cnt4, 'cnt5':cnt5, 'vars':vars })
 else:
      return redirect('/')


def hr_department(request): 
 if 'usernamehr2' in request.session:
      if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
      if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
      else:
        usernamehr1 = "dummy"
      mem = login.objects.filter(
        designation_id=usernamehr) .filter(fullname=usernamehr1)      
      des = department.objects.all().exclude(name='Default')      
      mem = User.objects.all()       
      return render(request, 'hr_department.html',{'des': des, 'mem': mem}) 
 else:
      return redirect('/')


def hr_category_newlist(request, id):
 if 'usernamehr2' in request.session:
      if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
      if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
      else:
        usernamehr1 = "dummy"
      mem = login.objects.filter(
        designation_id=usernamehr).filter(fullname=usernamehr1) 
        
      vars = department.objects.get(id=id)  
      m =candidates.objects.filter(reference = usernamehr1,deptmnt_id=vars.id,contact_status=0)
      return render(request, 'hr_category_newlist.html', {'m':m, 'mem':mem, 'vars':vars})
 else:
      return redirect('/')


def contactsave(request):
 if 'usernamehr2' in request.session:
      if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
      if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
      else:
        usernamehr1 = "dummy"
      mem = login.objects.filter(
        designation_id=usernamehr) .filter(fullname=usernamehr1)   
      m=candidates.objects.filter(reference = usernamehr1)
      tid=request.GET.get('tid')
      con=candidates.objects.get(id=tid)
      if request.method=="POST":
            con.contact_status=1
            con.save()
            msg_success = 'contacted'
            return render(request, 'hr_category_newlist.html', {'m':m, 'mem':mem,'msg_success':msg_success})
      return render(request, 'hr_category_newlist.html', {'m':m, 'mem':mem,})
 else:
      return redirect('/')      


def hr_category_contactedlist(request):
 if 'usernamehr2' in request.session:
      if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
      if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
      else:
        usernamehr1 = "dummy"
      mem = login.objects.filter(
        designation_id=usernamehr) .filter(fullname=usernamehr1)   
      m=candidates.objects.filter(reference =usernamehr1,contact_status=1)
      
      return render(request, 'hr_category_contactedlist.html', {'m':m, 'mem':mem})
 else:
      return redirect('/')


def replaysaveintrest(request):
 if 'usernamehr2' in request.session:
      if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
      if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
      else:
        usernamehr1 = "dummy"
      mem = login.objects.filter(
        designation_id=usernamehr) .filter(fullname=usernamehr1)   
      m=candidates.objects.filter(reference =usernamehr1)
      tid=request.GET.get('tid')
      con=candidates.objects.get(id=tid)      
      con.replay_status=1
      con.contact_status=2
      con.save()
      msg_success = 'interested'      
      return render(request, 'hr_category_contactedlist.html', {'m':m, 'mem':mem, 'msg_success':msg_success})
 else:
      return redirect('/')      


def replaysavenotintrest(request):
 if 'usernamehr2' in request.session:
      if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
      if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
      else:
        usernamehr1 = "dummy"
      mem = login.objects.filter(
        designation_id=usernamehr) .filter(fullname=usernamehr1)   
      m=candidates.objects.filter(reference = usernamehr1)
      tid=request.GET.get('tid')
      con=candidates.objects.get(id=tid)      
      con.replay_status=2
      con.contact_status=2
      con.save()
      msg_success = 'not inerested'   
      return render(request, 'hr_category_contactedlist.html', {'m':m, 'mem':mem, 'msg_success':msg_success})
 else:
      return redirect('/')      


def hr_category_intrestedlist(request):
 if 'usernamehr2' in request.session:
      if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
      if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']      
      else:
        usernamehr1 = "dummy"
      mem = login.objects.filter(
        designation_id=usernamehr) .filter(fullname=usernamehr1)   
      m=candidates.objects.filter(reference = usernamehr1,replay_status=1)
      return render(request, 'hr_category_intrestedlist.html', {'m':m, 'mem':mem})
 else:
      return redirect('/')

def hr_category_rejectedlist(request):
 if 'usernamehr2' in request.session:
      if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
      if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
      else:
        usernamehr1 = "dummy"
      mem = login.objects.filter(
        designation_id=usernamehr) .filter(fullname=usernamehr1)   
      m=candidates.objects.filter(reference = usernamehr1,replay_status=2)
      return render(request, 'hr_category_rejectedlist.html', {'m':m, 'mem':mem})
 else:
      return redirect('/')


def hr_category_history(request):
 if 'usernamehr2' in request.session:
      if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
      if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
      else:
        usernamehr1 = "dummy"
      mem = login.objects.filter(
        designation_id=usernamehr) .filter(fullname = usernamehr1)   
      m=candidates.objects.filter(reference = usernamehr1 ).exclude(replay_status=0)      
      return render(request, 'hr_category_history.html', {'m':m, 'mem':mem})
 else:
      return redirect('/')


############# new updations
def admin_hr_depmt(request,id): 
      des = department.objects.all().exclude(name='Default')     
      mm = login.objects.get(id = id)    
      mem = User.objects.all()        
      return render(request, 'admin_hr_depmt.html',{'des': des, 'mem': mem, 'mm':mm, }) 


def admin_allMembers_category(request, pk, id):  
      var = login.objects.get(id=id)    
      cnt1 = candidates.objects.filter(reference = var.fullname,deptmnt_id=pk,contact_status=0).count()
      cnt2 = candidates.objects.filter(reference = var.fullname,deptmnt_id=pk,contact_status=1).count()
      cnt3 = candidates.objects.filter(reference = var.fullname, deptmnt_id=pk).exclude(replay_status=0).count()
      cnt4 = candidates.objects.filter(reference = var.fullname,deptmnt_id=pk,replay_status=1).count()    
      cnt5 = candidates.objects.filter(reference = var.fullname,deptmnt_id=pk,replay_status=2).count()
      mm = department.objects.get(id=pk)    
      mem = User.objects.all()
      return render(request,'admin_allMembers_category.html',{'mem':mem ,'var':var,'mm':mm, 'cnt1':cnt1,'cnt2':cnt2,'cnt3':cnt3,'cnt4':cnt4, 'cnt5':cnt5})  


def admin_category_newlist(request,pk, id):
      var = login.objects.get(id=id) 
      mem = User.objects.all()              
      m = candidates.objects.filter(reference = var.fullname, deptmnt_id=pk, contact_status=0)
      return render(request,'admin_category_newlist.html',{'mem':mem, 'm':m })


def admin_contactsave(request):
      tid=request.GET.get('tid')
      con=candidates.objects.get(id=tid)
      mem = User.objects.all()
      if request.method=="POST":
            con.contact_status=1
            con.save()
      msg_success = "contacted"
      return render(request,'admin_category_newlist.html',{'mem':mem,'msg_success':msg_success})

def admin_category_contactedlist(request,id):
      var = login.objects.get(id=id)
      mem = User.objects.all()
      m=candidates.objects.filter(reference = var.fullname, contact_status=1)
      return render(request,'admin_category_contactedlist.html',{'mem':mem , 'm':m})

def admin_contactsave1(request):
      tid=request.GET.get('tid')
      con=candidates.objects.get(id=tid)
      mem = User.objects.all()
      if request.method=="POST":
            con.replay_status=1
            con.contact_status=2
            con.save()
            #return redirect('/HR_view')
      msg_success = "interested"
      return render(request, 'admin_category_contactedlist.html',{'mem':mem,'msg_success':msg_success})

def admin_contactsave2(request):
      tid=request.GET.get('tid')
      con=candidates.objects.get(id=tid)
      mem = User.objects.all()
      if request.method=="POST":
            con.replay_status=2
            con.contact_status=2
            con.save()
            #return redirect('/HR_view')
      msg_success = "not-interested"
      return render(request, 'admin_category_contactedlist.html',{'mem':mem,'msg_success':msg_success})


def admin_category_history(request,id):
      var = login.objects.get(id=id)
      mem = User.objects.all()
      m = candidates.objects.filter(reference = var.fullname).exclude(replay_status=0)
      return render(request,'admin_category_history.html',{'mem':mem , 'm':m})

def admin_category_intrestedlist(request,id):
      var = login.objects.get(id=id)
      mem = User.objects.all()
      m=candidates.objects.filter(reference = var.fullname, replay_status=1)
      return render(request,'admin_category_intrestedlist.html',{'mem':mem ,'m':m})
      
def admin_category_rejectedlist(request,id):
      var = login.objects.get(id=id)
      mem = User.objects.all()
      m=candidates.objects.filter(reference = var.fullname, replay_status=2)
      return render(request,'admin_category_rejectedlist.html',{'mem':mem , 'm':m})

def admin_department(request):
      mem = User.objects.all()
      return render(request, 'admin_department.html', {'mem': mem})

def admin_add_department(request):
      mem = User.objects.all()
      var = department.objects.all()
      if request.method == 'POST':
            z = department()
            z.name = request.POST['form_select']
            z.description = request.POST['desc']
            z.save()
            return redirect('/admin_department/')
      return render(request, 'admin_add_department.html',{'mem': mem, 'var': var})

def admin_department_view(request):
      var = department.objects.all()
      mem = User.objects.all()     
      return render(request, 'admin_department_view.html',{'mem': mem, 'var':var,})


def admin_view_department_delete(request,id):
      var = department.objects.filter(id=id)
      var.delete()
      return redirect('/admin_department_view/')


def admin_view_department_update(request,id):
      mem = User.objects.all()
      z = department.objects.all()
      if request.method == 'POST':
        vars = department.objects.get(id=id)
        vars.name = request.POST['name']
        vars.description = request.POST['desc']        
        vars.save()
        return redirect("/admin_department_view/")
      return render(request, 'admin_department_view.html',{'mem': mem, 'z': z})




