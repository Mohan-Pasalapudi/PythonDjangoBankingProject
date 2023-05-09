from django.db.models import Q
from .forms import EmployeeRegistrationForm, AccountHolderRegistrationForm, TransferForm
from .models import Employee, Admin, AccountHolder, Transaction
from django.contrib import messages
from decimal import Decimal
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import AccountHolder, Transaction
from django.shortcuts import render


def index(request):
    return render(request,"index.html")


def empregistration(request):
    form = EmployeeRegistrationForm()
    if request.method == "POST":
        formdata = EmployeeRegistrationForm(request.POST)
        if formdata.is_valid():
            formdata.save()
            msg="Employee Registered Successfully"
            return render(request, "empregistration.html", {"empform": form,"msg":msg})
        else:
            msg = "Failed to Register Employee"
            return render(request, "empregistration.html", {"empform": form, "msg": msg})
    return render(request,"empregistration.html",{"empform":form})


def emplogin(request):
    return render(request,"emplogin.html")


def about(request):
    return render(request,"aboutus.html")


def checkemplogin(request):
    uname = request.POST["username"]
    pwd = request.POST["password"]

    flag = Employee.objects.filter(Q(username=uname) & Q(password=pwd))

    print(flag)

    if flag:
        emp = Employee.objects.get(username=uname)
        print(emp)
        request.session["eid"] = emp.id
        request.session["ename"] = emp.fullname
        return render(request, "emphome.html", {"eid": emp.id, "ename": emp.fullname})
    else:
        msg = "Login Failed"
        return render(request, "emplogin.html", {"msg": msg})


def emphome(request):
    eid=request.session["eid"]
    ename=request.session["ename"]
    return render(request,"emphome.html",{"eid":eid,"ename":ename})


def viewemployees(request):
    auname=request.session["auname"]
    emplist = Employee.objects.all()
    count = Employee.objects.count()
    return render(request,"viewemps.html",{"auname":auname,"emplist":emplist,"count":count})


def emplogout(request):
    return render(request,"emplogin.html")


def empaddmoney(request):
    account_list = AccountHolder.objects.all()
    if request.method == 'POST':
        account_no = request.POST['account_no']
        amount = request.POST['amount']
        if not account_no:
            messages.error(request, 'Please enter the account no')
            return render(request, 'empaddmoney.html',{'account_list': account_list, 'success_message': 'Please enter the account no'})
        if not amount:
            messages.error(request, 'Please enter the amount')
            return render(request, 'empaddmoney.html',{'account_list': account_list, 'success_message': 'Please enter the amount'})
        else:
            amount = Decimal(amount)
            try:
                account = AccountHolder.objects.get(account_no=account_no)
                account.balance += amount
                account.save()
                messages.success(request, 'Money added successfully!')
                return render(request, 'empaddmoney.html',
                              {'account_list': account_list, 'success_message': 'Money added successfully!'})
            except AccountHolder.DoesNotExist:
                messages.error(request, 'Invalid account number')
                return render(request, 'empaddmoney.html',{'account_list': account_list, 'error_message': 'Invalid account number'})
    return render(request, 'empaddmoney.html', {'account_list': account_list})


def cusregistration(request):
    form = AccountHolderRegistrationForm()
    if request.method == "POST":
        formdata = AccountHolderRegistrationForm(request.POST)
        if formdata.is_valid():
            formdata.save()
            msg="Customer Registered Successfully"
            return render(request, "cuslogin.html", {"cusform": form,"msg":msg})
        else:
            msg = "Failed to Register Employee"
            return render(request, "cusregistration.html", {"cusform": form, "msg": msg})
    return render(request,"cusregistration.html",{"cusform":form})


def cuslogin(request):
    return render(request,"cuslogin.html")


def checkcuslogin(request):
    uname = request.POST["cusername"]
    pwd = request.POST["cpassword"]
    flag = AccountHolder.objects.filter(Q(username=uname) & Q(password=pwd))
    print(flag)
    if flag:

        cus = AccountHolder.objects.get(username=uname)
        print(cus)
        request.session["cid"] = cus.account_no
        request.session["cname"] = cus.fullname
        account_holder = AccountHolder.objects.get(account_no=request.session['cid'])
        return render(request, "cushome.html", {'account_holder': account_holder})
    else:
        msg = "Login Failed"
        return render(request, "cuslogin.html", {"msg": msg})


def cushome(request):
    eid = request.session["cid"]
    ename = request.session["cname"]
    return render(request, "cushome.html", {"eid":eid, "ename":ename})


def viewcustomers(request):
    emplist = AccountHolder.objects.all()
    count = AccountHolder.objects.count()
    return render(request,"viewcus.html",{"emplist":emplist,"count":count})


def cuslogout(request):
    return render(request,"cuslogin.html")


def adminlogin(request):
    return render(request,"adminlogin.html")


def checkadminlogin(request):
    uname = request.POST["ausername"]
    pwd = request.POST["apassword"]
    flag = Admin.objects.filter(Q(username__exact=uname) & Q(password__exact=pwd))
    print(flag)
    if flag:
        admin = Admin.objects.get(username=uname)
        print(admin)
        request.session["auname"] = admin.username
        return render(request, "adminhome.html", {"auname": admin.username})
    else:
        msg = "Login Failed"
        return render(request, "adminlogin.html", {"msg": msg})


def adminhome(request):
    auname=request.session["auname"]
    return render(request,"adminhome.html",{"auname":auname})


def adminlogout(request):
    auth.logout(request)
    return render(request,"adminlogin.html")


# Create your views here.

def newcustomer(request):
    if request.method == 'POST':
        form = AccountHolderRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AccountHolderRegistrationForm()
    return render(request, 'addcus.html', {'form': form})


def transfer(request):
    if request.method == 'POST':
        form = TransferForm(request.POST)
        if form.is_valid():
            sender_account = form.cleaned_data['sender_account']
            receiver_account = form.cleaned_data['receiver_account']
            amount = form.cleaned_data['amount']
            if sender_account.balance >= amount:
                sender_account.balance -= amount
                receiver_account.balance += amount
                sender_account.save()
                receiver_account.save()
                transaction = Transaction(from_account=sender_account, to_account=receiver_account, amount=amount)
                transaction.save()
                messages.success(request, 'Money added successfully!')

                return render(request, 'cushome.html',
                          {'success_message': 'Money added successfully!'})
            else:
                messages.error(request, 'Insufficient balance')
    else:
        form = TransferForm()
    return render(request, 'transfer.html', {'form': form})


def transactions(request):
    transactions = Transaction.objects.all()
    return render(request, 'transactions.html', {'transactions': transactions})
