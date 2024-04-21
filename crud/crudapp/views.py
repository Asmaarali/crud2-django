from django.shortcuts import render , redirect
from .models import studentinfo , studentclass
from .forms import studentform

# Create your views here.

def index(request):
    q=request.GET.get("q") if request.GET.get("q") != None else ""
    info=studentinfo.objects.filter(s_class__s_class__icontains=q)
    all_class=studentclass.objects.all()
    for i in all_class:
        countstudent=i.studentinfo_set.all()
        if countstudent.count() == 0:
            i.delete()
            return redirect("/")
    return render(request,"index.html",{"info":info,"classes":all_class,"q":q})

def addstudent(request):
    all_class=studentclass.objects.all()
    form=studentform()
    if request.method=="POST":
        getclass=request.POST.get("userclass").lower()
        getclass , created = studentclass.objects.get_or_create(s_class=getclass)
        studentinfo.objects.create(
            name=request.POST.get("name"),
            phone=request.POST.get("phone"),
            address=request.POST.get("address"),
            s_class=getclass,
        )
        return redirect("/")

        # form=studentform(request.POST)
        # if form.is_valid():
        #     form.save()
        #     return redirect('/')
    return render(request,"add.html",{"form":form,"classes":all_class})

def editstudent(request,id):
    all_class=studentclass.objects.all()
    info=studentinfo.objects.get(id=id)
    form=studentform(instance=info)
    if request.method=="POST":
        # form=studentform(request.POST,instance=info)
        # if form.is_valid():
        #     form.save()
        #     return redirect('/')
        getclass=request.POST.get("userclass").lower()
        getclass , created = studentclass.objects.get_or_create(s_class=getclass)
        info.name=request.POST.get("name")
        info.phone=request.POST.get("phone")
        info.address=request.POST.get("address")
        info.s_class=getclass
        info.save()
        return redirect("/")

    return render(request,"edit.html",{"info":info,"form":form,"classes":all_class})

def delstudent(request,id):
    info=studentinfo.objects.get(id=id)
    print(type(info))
    if request.method=="POST":
        info.delete()
        return redirect('/')
    return render(request,"delete.html",{"info":info})
