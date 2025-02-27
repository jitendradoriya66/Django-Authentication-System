from django.shortcuts import render,HttpResponse,redirect
from toapp.models import *
from django.core.mail import send_mail


# Create your views here.

def register(request):
    if 'email' not in request.session:
        return render(request,'login.html')
    if request.POST:
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        password=request.POST['password']
        c_password=request.POST['c_password']
        # name=request.POST['name']
        # print(name,email,phone,password,c_password)
        uid=registeration.objects.filter(fullname=name).exists()
        if uid:
            context={
                'msg':"User found"
            }
            return render(request,'login.html',context)
        if password!=c_password:
            context={
                'msg':"password not matched"
            }
            return render(request,'registration.html',context)
            
        else:
            context={
                'msg':"Created successfully"
            }
            registeration.objects.create(fullname=name,email=email,phone=phone,password=password,c_password=c_password)
            return render(request,'registration.html',context)
        
    return render(request,'login.html')


def login(request):
    if 'email' not in request.session:
        return render(request,'login.html')
    if request.POST:
        email=request.POST['email']
        password=request.POST['password']
        print(email,password)
        uid=registeration.objects.filter(email=email).exists()
        if uid:
            user=registeration.objects.get(email=email)
            if user.password == password:
                request.session['email']=email
                return render(request,'home.html')
            else:
                context={
                    'msg':'Wrong password '
                }
                return render(request,'login.html',context)
                
        # return render(request,'login.html')
        
        else:
            context={
                'msg':"User not found"
            }
        return render(request,'registration.html',context)
        
    return render(request,'login.html')




            # send_mail("Django",f"your OTP is {otp} ","jitendradoriya92@gmail.com",[email])

import random
def forget(request):
    if request.POST:
        email=request.POST['email']
        uid=registeration.objects.filter(email=email).exists()
        otp=random.randint(1000,9999)
        print(otp)
        if uid:
            user=registeration.objects.get(email=email)
            user.otp=otp
            user.save()
            send_mail('For Testing',f'Yout OTP is : {otp}',"Enter Your Email here ex joe@gmail.com",[email])
            print(user.email)
            context={
                'user':user
            }
            return render(request,'confirm.html',context)
        else:
            context={
                "msg":'Email does not Exists'
            }
            return render(request,'forget.html',context)
    return render(request,'forget.html')


def c_forget(request):
    if request.POST:
        email=request.POST['email']
        otp=request.POST['otp']
        new_password=request.POST['new_password']
        c_password=request.POST['confirm_password']
        uid=registeration.objects.get(email=email)
        print(uid.otp)
        if uid.otp==int(otp):
            uid=registeration.objects.get(email=email)
            uid.password=new_password
            uid.c_password=c_password
            uid.save()
            return redirect(login)
        else:
            context={
                'msg':'Check OTP ( Wrong OTP )'
            }
            return render(request,'confirm.html',context)
        # print(email,otp,new_password,c_password)  
    return render(request,'confirm.html')


    
