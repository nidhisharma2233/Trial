from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
   # data={
   #    "title":"trial",
   #    "list3":["yes","me"],
   #    "number":[10,20,30,40],
   #    "detail":[
   #       {'name':'nidhi','phoneno':9828834689},
   #       {'name':'sumit','phoneno':7345698288}
   #      ]


   # }
   return render(request,"index.html")

def aboutus(request):
   return HttpResponse("hello wscube")

def courses(request,courseid):
   return HttpResponse(courseid)