from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import registermodel

# def homepage(request):
#    return render(request,"index.html")
#    return HttpResponseRedirect('/thanku.html/')
# def aboutus(request):
#    return HttpResponse("hello students welcome for admission")
#
# def submitform(request):
#    return HttpResponse(request)
def post(request):
   print('nidhi sharma')
   # if request.method=="POST":
   #    username=request.POST['fullname']
   #    email = request.POST["email"]
   #    dob = request.POST["dob"]
   #    gender = request.POST["gender"]
   #    form_field=registermodel(
   #       username=username,
   #       email=email,
   #       dob=dob,
   #       gender=gender
   #    )
   #    form_field.save()
   #    return HttpResponse("form successfully submitted")
   return render(request,'index.html')
def add(request):
   print("heloo")
   if request.method == 'POST':
      name = request.POST['name']
      mail = request.POST['emailid']
      dob = request.POST['dob']
      gender = request.POST['gender']



      new_emp = registermodel(username=name, email=mail, dob=dob, gender=gender)
      new_emp.save()
      return HttpResponse('Employee Added Successfully')

   elif request.method == 'GET':
      return render(request, 'add.html')
   else:
      return HttpResponse('An Exception Occured Employee has not  Been Added')

def all(request):
   emps = registermodel.objects.all()
   context = {
      'emps': emps
   }
   print(context)
   return render(request, 'view.html', context)

def filter(request):
   print("hey")
   if request.method == 'POST':
      name = request.POST['name']
      email = request.POST['emailid']
      dob = request.POST['dob']
      gender = request.POST['gender']
      emps = registermodel.objects.all()
      if name:
         emps = emps.filter(username__icontains=name)

      if email:
         emps = emps.filter(email__icontains=email)

      if dob:
         emps = emps.filter(dob__icontains=dob)
      if gender:
         emps = emps.filter(gender__icontains=gender)
      context = {
         'emps': emps
      }
      return render(request, 'view.html', context)
   elif request.method == 'GET':
      return render(request, 'filter.html')
   else:
      return HttpResponse('An Exception Occured')


def get(request):


   # print(emp_id)
   # value=registermodel.objects.get(pk=id)
   #
   # value.delete()
   # return redirect("/remove")
   #
   # if emp_id:
   #    try:
   #       emp_to_be_removed = registermodel.objects.get(id=emp_id)
   #       emp_to_be_removed.delete()
   #       return HttpResponse('Employee removed successfully')
   #    except:
   #       return HttpResponse('please enter a valid employee id')
   emps = registermodel.objects.all()
   context = {
      'emps': emps
   }
   return render(request, 'remove.html', context)

def delete(request, id):


   # print(emp_id)
   value=registermodel.objects.get(pk=id)

   value.delete()
   return redirect("/remove")

def viewalldataupdatepage(request):
   var1=registermodel.objects.all()
   for i in var1:
      return render(request,"update.html",{'var1':var1})

def update(request,id):
   var1=registermodel.objects.get(id=id)
   return render(request,"formupdate.html",{'var1':var1})

def updatedata(request,id):
   username = request.POST['name']
   email = request.POST['emailid']
   dob = request.POST['dob']
   gender = request.POST['gender']
   member=registermodel.objects.get(id=id)
   member.username=username
   member.email = email
   member.dob = dob
   member.gender = gender
   member.save()
   return HttpResponseRedirect('/Register-View')
