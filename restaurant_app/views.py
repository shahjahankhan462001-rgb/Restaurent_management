from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from restaurant_app.models import Table, MenuItem, MenuCategory, Order, OrderItem, Bill
from .forms import TableForm
# User Registration

def register_user(request):
    if request.method == 'POST':
        
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        email = request.POST.get('email')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return render(request, 'register.html')

        User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        messages.success(request, "User registered successfully! Login now.")
        return redirect('login')
    return render(request, 'register.html')

# User Login

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid username or password")
            return render(request, "login.html")
    else:
        return render(request, "login.html")
    
# Dashboard Page

# @login_required(login_url='login')
# def dashboard(request):
    # return render(request, 'dashboard.html')


# Home Page (after login)
@login_required(login_url='login')
def home(request):
    table = Table.objects.all()
    menucategory = MenuCategory.objects.all()
    menuitem = MenuItem.objects.all()
    order = Order.objects.all()
    orderitem = OrderItem.objects.all()
    bill = Bill.objects.all()
    context = {
        "table": table,
        "menucategory": menucategory,
        "menuitem": menuitem,
        "order": order,
        "orderitem": orderitem,
        "bill": bill
    }
    return render(request, 'home.html', context)



# User Logout

@login_required(login_url='login')
def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect("login")



#table
# def table(request):
#     all_tables=Table.objects.all()
#     return render(request,'addtable.html',{'table':all_tables})

# def table(request):
#     if request.method=='POST':
#         form=TableForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('dashboard')
#     else:
#         form=TableForm()
#     return render(request,'addtable.html',{'form':form})

@login_required(login_url='login')
def dashboard(request):
    tables = Table.objects.all()

    total_tables = tables.count()
    available = tables.filter(status='available').count()
    occupied = tables.filter(status='occupied').count()
    reserved = tables.filter(status='reserved').count()

    context = {
        "total_tables": total_tables,
        "available": available,
        "occupied": occupied,
        "reserved": reserved,
    }
    return render(request, 'dashboard.html', context)


def table(request):
    if request.method == "POST":
        form = TableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TableForm()
    
    return render(request, 'addtable.html', {'form': form})



#order
def order(request):
    all_orders=Order.objects.all()
    return render(request,'order.html',{'order':all_orders})



#menucategory

def menu_categories(request):
    categories=MenuCategory.objects.all()
    items=MenuItem.objects.all()
    return render(request,'addmenucategory.html',{'categories':categories,'items':items})

# menuitem

def menu_item(request):
    items=MenuItem.objects.all()
    return render(request,'addmenuitem.html',{'items':items})

#order item

def order_item(request):
    allorderitems=OrderItem.objects.all()
    return render(request,'orderitem.html',{'allorderitems':allorderitems})

#bill

def bill(request):
    billing=Bill.objects.all()
    return render(request,'bill.html',{'billing':billing})