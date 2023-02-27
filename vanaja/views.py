from django.http import HttpResponse
from django.shortcuts import render, redirect

def homepage(request):
   # data = {
    #    'title':'home page',
     #   'bdata':'ba guru yAn samachata',
      #  'clist':['php','python','django'],
       # 'student' : [{'name':'khgowda','number':9036528550},
        #{'name':'monish','number':9741832381}],
        #'class':[],
        


    #}
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def products(request):
    return render(request,"products.html")

def cont(request):
    return render(request,"cont.html")

def account(request):
    return render(request,"account.html")



def course(request):
    return HttpResponse('AWS CLOUD PRACTNIER ')

def courseDetails(request,courseid):
    return HttpResponse(courseid)