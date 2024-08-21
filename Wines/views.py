from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponseRedirect
import datetime
from .forms import CustomUserForm
from .forms import CustomContactUsForm
from .models import CustomUser
from .models import Monitor
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.contrib.sessions import *
from .utils import send_email_to_client
from django.contrib import messages

flag = False

#landing page or Home page here
def Landing_page(request):
    print(flag)
    return render(request,"index2.html",{'flag': flag})


def Products_page(request):
    print(flag)
    return render(request,"Products.html",{'flag': flag})

def Login(request):

    if request.method == "POST":
        entered_email = request.POST.get("Useremail")
        entered_password = request.POST.get("password")
        user = CustomUser.objects.get(Useremail = entered_email)
        if check_password(entered_password,user.password):
            request.session['user_id'] = user.id
            request.session['email'] = user.Useremail
            print('Customer Exists')
            global flag 
            flag = True
            
            # global user_timer
            user_timer = Monitor(email=entered_email,Login_time=datetime.datetime.now())
            user_timer.save()

            # usermail= [entered_email]
            # send_email_to_client(usermail)
            return render(request,"Products.html",{'flag': flag})
        else :
            print("Invalid Credentials")

              
    
        
    
    return render(request,"login2.html",{'flag': flag})



def Logout(request):
    # user_email= request.session['user_id']
    user_timer = Monitor.objects.last()
    print(user_timer)
    user_timer.Logout_time = datetime.datetime.now()
    user_timer.save()

    global flag
    flag = False
    request.session.clear()
    return render(request,"index2.html",{'flag': flag})

def Register(request):

    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            password = form.cleaned_data['password']
            customer.password = make_password(password)
            usermail = [customer.Useremail]
            send_email_to_client(usermail)
            
            customer.save()
            print("You are Successfully registered")
            return render(request,"login2.html",)


    print(flag)        
    
    return render(request,"registration2.html",{'flag': flag})

# CONTACT US FUNCTION 
def Contact_Us(request):
    if request.method == 'POST':
        form = CustomContactUsForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.submission_time = datetime.datetime.now()
            instance.save()
            print("Message Sent Successfully")
            messages.success(request,"Your feedback has been recorded")
            return render(request,'ContactUs.html')

    return render(request,"contactUs.html",{'flag':flag})

# CART FUNCTION 

def crate(request):
    if request.session.get('cart') is None:
        print("There is nothing in the cart")
    else:
        cart =  request.session.get('cart')
        keystore = list(cart.keys())
        for i in keystore:
            print(i)
            print(cart[i])
            

    return render(request,"cart.html",{'flag':flag})

# x------------x-------------x-------------x


# All below are the standalone Product pages
def Product_1(request):
    # current_path = request.path
    # print(current_path)   
    print(request.session.get('cart'))

    return render(request,"Product1.html",{"flag":flag})

def Product_2(request):
    
    # print(current_path)    

    return render(request,"Product2.html",{"flag":flag})

def Product_3(request):
    
    # print(current_path)    

    return render(request,"Product3.html",{"flag":flag})

def Product_4(request):
    
    # print(current_path)    

    return render(request,"Product4.html",{"flag":flag})

def Product_5(request):
    
    # print(current_path)    

    return render(request,"Product5.html",{"flag":flag})

def Product_6(request):
    
    # print(current_path)    

    return render(request,"Product6.html",{"flag":flag})


def Product_Processing(request):
    if request.method == 'POST':
        if request.session.get('user_id'):
            productCode = request.POST.get('product')
            productQuantity = request.POST.get('selectedOption')
            print(productCode)
            cart = request.session.get('cart')
            if cart:
                cart[productCode] = productQuantity
            else :
                cart ={}
                cart[productCode] = productQuantity
                
            
            # print(cart)
            request.session['cart'] = cart     
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
        else:
            return render(request, "login2.html")
          
