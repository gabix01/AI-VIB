from django.shortcuts import render
from django.contrib import messages
import re
from django.contrib.auth.models import User
# Create your views here.
from django.shortcuts import redirect, render, HttpResponse, HttpResponseRedirect
from django.contrib.auth  import authenticate,  login, logout
from mainapp.models import   addapartment
# Create your views here.
def home(request):
    app = addapartment.objects.all()
    context = {'app': app}
    return render(request, 'home.html', context)

def features(request):
    return render(request, 'features.html')

def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')

def ulogin(request):
   
    if request.method == "POST":
            # Get the post parameters
      
        username = request.POST['uname']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)  
        if user is not None:
            login(request, user)
            return redirect('/dashboard')

        else:
            messages.error(request, "Invalid credentials! Please try again")
            return render(request, "login.html")
    return render(request, 'login.html' )
  

def signup(request):
    
          
    if request.method == "POST":
            # Get the post parameters
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        checkemail = User.objects.filter(email=email)
        checkuser = User.objects.filter(username=username)
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if len(checkemail)>0:
            messages.error(request, "Email is already exits.")
            return render(request, 'signup.html')
        if len(checkuser)>0:
            messages.error(request, "User Name is already exits.")
            return render(request, 'signup.html')

        if len(username) > 10:
            messages.error(request, " Your user name must be under 10 characters")
            return render(request, 'signup.html')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return render(request, 'signup.html')
        if password != cpassword:
            messages.error(request, " Passwords do not match")
            return render(request, 'signup.html')
        
        if(re.search(regex,email)):   
           print("Valid Email")   
        else:   
           messages.error(request, " invalid email")
           return render(request, 'signup.html') 
         
        # Create the user
        user = User.objects.create_user(username, email, password)
        user.save()
        
        messages.success(request, "You have succesfully Registerd.")
        return redirect('/login')
    return render(request, 'signup.html')


def dashboard(request):
    return render(request, 'dashboard.html')
def addappartment(request):
    if request.method == "POST":
        # Get the post parameters
        appname1 = request.POST['appname']
        oname1 = request.POST['oname']
        ophone = request.POST['ophone']
        renter1 = request.POST['renter']
        rphone = request.POST['rphone']
        share1 = request.POST['share']
        sno = request.POST['sno']
        startdate1 = request.POST['sdate']
        expiredate1 = request.POST['edate']
        file = request.FILES['file']
        user1 = User.objects.get(username=request.user.username)
        # Create the job
        Add = addapartment( user = user1 ,appname = appname1 , owner= oname1 , OPhone = ophone,renter = renter1,  RPhone=rphone ,share = share1 , image= file, stno=sno, startdate = startdate1, expiredate = expiredate1 )
        Add.save()
        messages.success(request, "Your appartment add successfully.")
        return redirect('/addappartment')
    return render(request, 'addappartment.html')
def ulogout(request):
    logout(request)
    return redirect('/')

def appartmentlist(request):
     user1 = User.objects.get(username=request.user.username)
     app = addapartment.objects.filter(user=user1)
     context = {'app': app}
     return render(request, 'appartmentlist.html', context)

def delete(request,id):
    subdistrict = addapartment.objects.get(pk=id)
    messages.success(request, "Your data is successfully Deleted.")
    subdistrict.delete()
    return redirect('/appartmentlist')
def update(request,id):
    if request.method == "POST":
        # Get the post parameters
        appname1 = request.POST['appname']
        oname1 = request.POST['oname']
        ophone = request.POST['ophone']
        renter1 = request.POST['renter']
        rphone = request.POST['rphone']
        share1 = request.POST['share']
        sno = request.POST['sno']
        startdate1 = request.POST['sdate']
        expiredate1 = request.POST['edate']
        file = request.FILES['file']
        
        # Create the job
        ujob = addapartment.objects.get(id=id)
        ujob.stno = sno
        ujob.appname = appname1
        ujob.owner = oname1
        ujob.OPhone = ophone
        ujob.renter = renter1
        ujob.RPhone = rphone
        ujob.sahre = share1
        ujob.image = file
        ujob.startdate = startdate1
        ujob.expiredate = expiredate1
        ujob.save()
        
        
        messages.success(request, "Record is updated successfully.")
        return redirect('/appartmentlist')
        #return render(request, 'company/jobs.html')

    user = User.objects.get(username=request.user.username)
    app = addapartment.objects.filter(user=user, id=id)
    #print(ujob)
    context = {'app':app}
    #print(alljobs)
    return render(request, 'addappartment.html', context)