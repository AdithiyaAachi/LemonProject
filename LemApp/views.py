from django.shortcuts import render,redirect
from LemApp.models import CategoryDb,ProductDb
from Frontend.models import contactdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import  authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages



# Create your views here.
def indexpage(request):
    return render(request,"Index.html")
def categorypage(request):
    return render(request,"AddCategory.html")
def save_category(request):
    if request.method=="POST":
        na=request.POST.get('name')
        des=request.POST.get('description')
        img=request.FILES['image']
        obj=CategoryDb(Name=na,Description=des,Image=img)
        obj.save()
        messages.success(request, "Category save successfully....!")
        return redirect(categorypage)
def display_category(request):
    data=CategoryDb.objects.all()
    return render(request,"DisplayCategory.html",{'data':data})
def edit_category(request,dataid):
    cat=CategoryDb.objects.get(id=dataid)
    return render(request,"EditCategory.html",{'cat':cat})
def Update_category(request, dataid):
    if request.method=="POST":
        cna=request.POST.get('name')
        desc= request.POST.get('description')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file=CategoryDb.objects.get(id=dataid).Image
        CategoryDb.objects.filter(id=dataid).update(Name=cna,Description=desc,Image=file)
        return redirect(display_category)
def remv_category(request,dataid):
    rem=CategoryDb.objects.filter(id=dataid)
    rem.delete()
    messages.error(request, "Category delete successfully....!")
    return redirect(display_category)
def product_page(request):
    category=CategoryDb.objects.all()
    return render(request,"AddProduct.html",{'category':category})
def save_product(request):
    if request.method=="POST":
        cna=request.POST.get('cat')
        pna=request.POST.get('pname')
        decp = request.POST.get('description')
        price= request.POST.get('price')
        img=request.FILES['pimage']
        obj=ProductDb(Category_Name=cna,Product_Name=pna,Description=decp,Price=price,Product_Image=img)
        obj.save()
        messages.success(request, "product save successfully....!")
        return redirect(product_page)

def display_product(request):
    show=ProductDb.objects.all()
    return render(request,"DisplayProduct.html",{'show':show})
def edit_product(request,pro_id):
    cat=CategoryDb.objects.all()
    product=ProductDb.objects.get(id=pro_id)
    return render(request,"EditProduct.html",{'cat':cat,'product':product})
def Update_product(request,dataid):
    if request.method == "POST":
        cana= request.POST.get('cat')
        pnam= request.POST.get('pname')
        desc = request.POST.get('description')
        price= request.POST.get('price')
        try:
            img = request.FILES['pimage']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = ProductDb.objects.get(id=dataid).Product_Image
        ProductDb.objects.filter(id=dataid).update(Category_Name=cana,Product_Name=pnam,Description=desc,Price=price,Product_Image=file)
        return redirect(display_product)
def remv_product(request,dataid):
    rem=ProductDb.objects.filter(id=dataid)
    rem.delete()
    messages.error(request, "product delete successfully....!")
    return redirect(display_product)
def adminlogin(request):
    return render(request,"AdminLogin.html")
def admin_login(request):
    if request.method=="POST":
        un=request.POST.get('user_name')
        pwd=request.POST.get('pass_word')

        if User.objects.filter(username__contains=un).exists():
            x=authenticate(username=un,password=pwd)
            if x is not None:
                login(request,x)
                request.session['username']=un
                request.session['password']=pwd
                messages.success(request, "Welcome")

                return redirect(indexpage)
            else:
                return redirect(adminlogin)
        else:
            return redirect(adminlogin)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(adminlogin)


def display_contact(a):
    data = contactdb.objects.all()
    return render(a,"DisplayContact.html",{'data':data})

def deletecontact(a,dataid):
    data = contactdb.objects.filter(id=dataid)
    data.delete()
    return redirect(display_contact)



