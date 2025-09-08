from django.shortcuts import render,redirect
from .forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate



# Create your views here.

def home(request):
    return render(request, 'pages/index.html')

def logout(request):
    auth.logout(request)
    return redirect('')

def login(request):
    form = LoginForm()

    if request.method =="POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request,username=username,password = password)

            if user is not None:
                auth.login(request,user)
                return redirect('')
            
    context = {'login_form':form,
               'age': 20}


    return render(request, 'pages/login.html', context = context)


#create a form
def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
    
    context = {'form': form}
    print(context)

    return render(request, 'pages/register.html', context=context)
 
    