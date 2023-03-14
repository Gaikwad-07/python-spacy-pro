from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import employee,department
from django.urls import reverse
# Create your views here.
def login(request):
    return render(request,"login.html",{"msg":"Enter Your Information"})

def sign_up(request):
    temp_dep=department.objects.all()
    return render(request,"regi.html",{"data":temp_dep})

def add(request):
    if (request.method == "POST"):
        a=request.POST['ename']
        b=request.POST['empid']
        c=request.POST['email']
        d=request.POST['pass']
        e=request.POST['mobile']
        f=int(request.POST['dep'])
        
        data=employee.objects.all()
        temp_dep=department.objects.get(id=f)
        print(temp_dep)
    
        
        emp=employee(ename=a,empid=b,email=c,password=d,mobile=e,dep=temp_dep)
        employee.save(emp)
        return HttpResponseRedirect(reverse('login'))

    else:
        temp_dep=department.objects.all()
        return render(request, "regi.html",{"data":temp_dep})



def sign_in(request):
    if (request.method == "POST"):
        e=request.POST['iemail']
        p=request.POST['ipassword']
        data=employee.objects.all()
        l=[]
        l1=[]
        for i in data:
            l.append(i.email)
            l1.append(i.password)
        for j in range(len(l)):
            if(l[j]==e and l1[j]==p):
                return HttpResponseRedirect(reverse('home')) 
        return render(request,"login.html",{"msg":"Incorrect User Information"})   
    else:
        return render(request,"login.html",{"msg":"Enter Your Information"})
    
    
def home(request):
    data=employee.objects.all()
    return render(request,"home.html",{'employee':data}) 

def update(request,id):
    member=employee.objects.get(id=id)
    temp_dep=department.objects.all()
    return render(request,"update.html",{"employee":member,"department":temp_dep})

def uprecord(request,id):
    a=request.POST['ename']
    b=request.POST['empid']
    c=request.POST['email']
    d=request.POST['pass']
    e=request.POST['mobile']
    f=int(request.POST['dep'])
    temp_dep=department.objects.get(id=f)
    member=employee.objects.get(id=id)
    member.ename=a
    member.empid=b
    member.email=c
    member.password=d
    member.mobile=e
    member.dep=temp_dep
    member.save()
    return HttpResponseRedirect(reverse("home"))


def delete(request,id):
    member=employee.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse("home"))
    