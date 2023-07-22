from django.shortcuts import render,redirect
from django.forms import inlineformset_factory
from home.models import Product,Customer,Order
from home.forms import *
from django.contrib.auth import authenticate,login,logout 
from home.filters import  OrderFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from home .decorator import *

# admin vishu and vishu@2003
# jerry jerry@1234


# Create your views here.
#INDEX IS DASHBOARD
@login_required(login_url='loginuser')
# @allowed_users(allowed_roles=['admin','staff'])
def home(request):
    customers=Customer.objects.all()
    orders=Order.objects.all()
    totalcustomer=customers.count()
    totalorder=orders.count()
    deliver=orders.filter(status='Delivered').count()
    pending=orders.filter(status='pending').count()
    context={'orders':orders,'customers':customers,'totalcustomer':totalcustomer,'totalorder':totalorder,'deliver':deliver,'pending':pending}
    
    return render(request,'index.html',context)


def product(request):
    products=Product.objects.all()
    return render(request,'product.html',{'products': products})

def customer(request,pk_test):
    customer=Customer.objects.get(id=pk_test)
    orders=customer.order_set.all()
    order_count=orders.count()
    myfilter=OrderFilter(request.GET,queryset=orders)
    orders=myfilter.qs
    context={'customer':customer,'orders':orders,'order_count':order_count,'myfilter':myfilter}
    return render(request,'customer.html',context)

@login_required(login_url='loginuser')
def createOrder(request,pk):
    OrderFormSet=inlineformset_factory(Customer,Order,fields=('product','status'),extra=10)
    
    customer=Customer.objects.get(id=pk)
    formset=OrderFormSet( queryset=Order.objects.none(),instance=customer)
    # form =OrderForm(initial={'customer':customer})
    if request.method =='POST':
        formset =OrderFormSet(request.POST,instance=customer )
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context={'formset':formset}
    return render(request,"order_form.html",context)

@login_required(login_url='loginuser')
def updateOrder(request,pk):
    order=Order.objects.get(id=pk)
    formset =OrderForm(instance=order)
    if request.method =='POST':
        formset =OrderForm(request.POST,instance=order)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    
    context={'formset':formset}
    return render(request,"order_form.html",context)

@login_required(login_url='loginuser')
def deleteOrder(request,pk):
     order=Order.objects.get(id=pk)
     context={'item':order}
     if request.method=="POST":
         order.delete()
         return redirect('/')
     return render(request,'delete.html',context)




@login_required(login_url='loginuser')
def updatecustomer(request,pk):
    customer=Customer.objects.get(id=pk)
    formset=customerForm(instance=customer)
    if request.method=='POST':
        formset =customerForm(request.POST,instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context={'formset':formset}

    return render(request,"customerupdate.html",context)



@login_required(login_url='loginuser')
def deletecustomer(request,pk):
    customer=Customer.objects.get(id=pk)
    
    context={'customer':customer}
    if request.method=="POST":
         customer.delete()
         return redirect('/')
    return render(request,'deletecustomer.html',context)



def loginuser(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        print(username,password)
        if user is not None:
            login(request,user)
            
            userid=request.user.id
            # context={userid:'userid'}
            # return render(request,'user.html',context)
            return redirect('userpage')
            # return HttpResponse("log in")
        else:
            messages.info(request, "username or password is incorrect")
            return render(request,'login.html')
        

    return render(request,'login.html')




def register(request):
    form= createuserForm()
    if request.method=="POST":
        form=createuserForm(request.POST)
        if form.is_valid():
            user=form.save()
            Username=form.cleaned_data.get('username')
            email=form.cleaned_data.get('email')
            phone=form.cleaned_data.get('phone')
            
            messages.success(request,"profile was created for"+ Username)
            Customer.objects.create(user=user,name=Username,email=email,phone=phone)
            return  redirect('loginuser')
    context={'form':form}
    return render(request,'register.html',context)

def logoutuser(request):
    logout(request)
    return redirect('loginuser')


@login_required(login_url='loginuser')
def userpage(request):
    
    orders=request.user.customer.order_set.all()
    totalorder=orders.count()
    deliver=orders.filter(status='Delivered').count()
    pending=orders.filter(status='pending').count()
    
    customer=request.user.customer
    print("ORDER:",orders,)
    context={'orders':orders,'customer':customer,'totalorder':totalorder,'deliver':deliver,'pending':pending}
    return render(request,'user.html',context)

@login_required(login_url='loginuser')
def userprofile(request):
    customer=request.user.customer
    print(customer)
    form=customerForm(instance=customer)
    if request.method=="POST":
        form=customerForm(request.POST,request.FILES,instance=customer)
        if form.is_valid():
            form.save()
        
    context={'form':form}

    return render(request,'profile.html',context)