from django.shortcuts import render,redirect
from LemApp.models import CategoryDb,ProductDb
from Frontend.models import contactdb,RegisterDb,CartDb,Checkoutdb
from django.contrib import messages
# Create your views here.
def homepage(request):
    cat=CategoryDb.objects.all()
    return render(request,"Home.html",{'cat':cat})
def productpage(request):
    pro=ProductDb.objects.all()
    return render(request,"Products.html",{'pro':pro})
def product_filtered(request,cat_name):
    data=ProductDb.objects.filter(Category_Name=cat_name)
    return render(request,"Products_Filtered.html",{'data':data})
def single_product(request,proid):
    data=ProductDb.objects.get(id=proid)
    return render(request,"SingleProduct.html",{'data':data})
def aboutpage(request):
    return render(request,"About.html")
def contactpage(request):
    return render(request,"Contact.html")
def save_contact(request):
    if request.method=="POST":
        msg=request.POST.get('message')
        na=request.POST.get('name')
        em=request.POST.get('email')
        sub=request.POST.get('subject')
        obj=contactdb(EnterMessage=msg,Name=na,EmailId=em,Subject=sub)
        obj.save()
        return redirect(contactpage)
def registerpage(request):
    return render(request,"Register.html")
def register_save(request):
    if request.method=="POST":
        na=request.POST.get('name')
        mob=request.POST.get('mobile')
        em=request.POST.get('email')
        un=request.POST.get('username')
        pwd=request.POST.get('password')
        obj=RegisterDb(Name=na,Mobile=mob,Email=em,Username=un,Password=pwd)
        obj.save()
        return redirect(registerpage)
def userlogin(request):
    if request.method=="POST":
        un=request.POST.get('user')
        pwd=request.POST.get('passwrd')
        if RegisterDb.objects.filter(Username=un,Password=pwd).exists():
            request.session['Username']=un
            request.session['Password']=pwd
            messages.success(request, "Welcome")

            return redirect(homepage)
        else:
            messages.error(request, "Invalid username or password....!")

            return redirect(registerpage)
    return redirect(registerpage)

def userlogout(request):
    del request.session['Username']
    del request.session['Password']
    return redirect(registerpage)
def cartpage(request):
    data=CartDb.objects.filter(UserName=request.session['Username'])
    total_price = 0
    for i in data:
        total_price = total_price + i.TotalPrice
    return render(request,"Cart.html",{'data':data,'total_price':total_price})
def save_cart(request):
    if request.method=="POST":
        uname=request.POST.get('uname')
        pname=request.POST.get('pname')
        qety= request.POST.get('quantity')
        tprice = request.POST.get('tprice')
        descp= request.POST.get('description')
        obj=CartDb(UserName=uname,ProductName=pname,Quantity=qety,TotalPrice=tprice,Description=descp)
        obj.save()
        messages.success(request, "Cart save successfully....!")
        return redirect(cartpage)

def cartdelete(request,pro_id):
    pro=CartDb.objects.filter(id=pro_id)
    pro.delete()
    messages.error(request, "Cart delete successfully....!")
    return redirect(cartpage)

def checkoutpage(request):
    data = CartDb.objects.filter(UserName=request.session['Username'])
    total_price = 0
    for i in data:
        total_price = total_price + i.TotalPrice
    return render(request,"Checkout.html",{'data':data,'total_price':total_price})



def save_checkout(request):
    if request.method=="POST":
        fn=request.POST.get('fname')
        ln= request.POST.get('lname')
        ema = request.POST.get('email')
        add = request.POST.get('addr')
        city = request.POST.get('city')
        count = request.POST.get('country')
        tel = request.POST.get('tele')
        obj=Checkoutdb(FirstName=fn,LastName=ln,EmailId=ema,Address=add,City=city,Country=count,Telephone=tel)
        obj.save()
        messages.success(request, "Checkout save successfully....!")
        return redirect(checkoutpage)

def yourorder(request):
    messages.success(request, "Place order has been success....!")
    return redirect(homepage)