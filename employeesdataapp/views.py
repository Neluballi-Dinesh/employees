from django.shortcuts import render
from django.http import HttpResponse
from .models import EmployeeData
import faker
fake=faker.Faker()

def generatingData(request):
    for i in range(100):
        EmployeeData(
        first_name=fake.first_name(),
        last_name=fake.first_name(),
        email=fake.email(),
        company=fake.random_element(elements=('TCS','WIRPO','INFOSYS','CTS')),
        location=fake.random_element(elements=('Hyderabad','Bangalore','Chennai','Pune')),
        salary=fake.random_element(elements=(20000,30000,40000,50000,60000)),
        address=fake.address()
        ).save()
    return HttpResponse('Data Saved')


def fetchingData(request):
    emps=EmployeeData.objects.all()
    return render(request,'fetchingData.html',{'emps':emps})

def hyderabad(request):
    if request.method=="GET":
        emps=EmployeeData.objects.filter(location='Hyderabad')
        return render(request,'hyddata.html',{'emps':emps})
    else:
        com=request.POST['data']
        emps=EmployeeData.objects.filter(location='Hyderabad') & EmployeeData.objects.filter(company=com)
        return render(request,'hyddata.html',{'emps':emps})

def bangalore(request):
    if request.method=="GET":
        emps=EmployeeData.objects.filter(location='Bangalore')
        return render(request,'bangdata.html',{'emps':emps})
    else:
        com=request.POST['data']
        emps=EmployeeData.objects.filter(location='Bangalore') & EmployeeData.objects.filter(company=com)
        return render(request,'bangdata.html',{'emps':emps})

def chennai(request):
    if request.method=="GET":
        emps=EmployeeData.objects.filter(location='Chennai')
        return render(request,'chedata.html',{'emps':emps})
    else:
        com=request.POST['data']
        emps=EmployeeData.objects.filter(location='Chennai') & EmployeeData.objects.filter(company=com)
        return render(request,'chedata.html',{'emps':emps})

def pune(request):
    if request.method=="GET":
        emps=EmployeeData.objects.filter(location='Pune')
        return render(request,'punedata.html',{'emps':emps})
    else:
        com=request.POST['data']
        emps=EmployeeData.objects.filter(location='Pune') & EmployeeData.objects.filter(company=com)
        return render(request,'punedata.html',{'emps':emps})

def mainPage(request):
    return render(request,'mainPage.html')
