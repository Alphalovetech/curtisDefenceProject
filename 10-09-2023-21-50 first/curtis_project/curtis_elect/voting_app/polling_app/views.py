from django.shortcuts import render, redirect 


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from polling_app.models import voters
from polling_app.forms import votersForm


# Create your views here.
from .forms import CreateUserForm
  
def landing_page(request):
    return render(request, "landing_page.html", {})

# @login_required(login_url='login_page')
# def index(request):
#      return render(request, "adminlte/index.html", {})

#login_page
def login_page(request):
    if request.user.is_authenticated:
        return redirect('timeline')
    else:
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('portfolio')
                    # Redirect to a success page.
            else:
                messages.success(request, ("There was an error logging in, try again..."))
                return redirect('login_page')
        
        else:
            return render(request, "login_page.html", {})


#signup page
def signup(request):
    if request.user.is_authenticated:
        return redirect('timeline')
    else:
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                email = form.cleaned_data['email']
                password = form.cleaned_data['password1']
                user = authenticate(username=username, email=email, password=password)
                login(request, user)
                # return redirect('portfolio')
                messages.success(request, ("Registration Successful"))
                return redirect('portfolio')
        else:
            form = CreateUserForm()

            return render(request, "signup.html", {
                'form':form,
            })

#logout page
def logout_user(request):
    logout(request)
    return redirect('login_page')


def home(request):
     return render(request, "home.html", {})

@login_required(login_url='login_page')
def timeline(request):
    return render(request, "timeline.html", {})

@login_required(login_url='login_page')
def portfolio(request):
    return render(request, "portfolio.html", {})

@login_required(login_url='login_page')
def vote(request):
    return render(request, "vote.html", {})

@login_required(login_url='login_page')
def register(request):
    return render(request, "register.html", {})

#voter request

def voter(request):
     if request.method=="POST":
         form=votersForm(request.POST)
         if form.is_valid():
             try:
                 form.save()
                 return redirect("/adminlte/pages/voting_info/voter.html")
             except:
                 pass
     else:
         form = votersForm()
     return render(request, 'dashboard/index.html', {'form':form})

def show(request):
     voters=voters.objects.all()
     return render(request, 'adminlte/pages/voting_info/voter.html', {'voters':voters})

def edit(request, id):
     voter = voters.objects.get(id=id)
     return render(request, 'adminlte/pages/voting_info/voter_edit.html', {'voter':voter})

def update(request,id):
     voter = voters.objects.get(id=id)
     form=votersForm(request.POST,instance=voter)
     if form.is_valid():
                 form.save()
                 return redirect("/adminlte/pages/voting_info/voter.html")
    
     return render(request, 'adminlte/pages/voting_info/voter_edit.html', {'voter':voter})

def destroy(request,id):
     voter = voters.objects.get(id=id)
     voter.delete()
     return redirect("/adminlte/pages/voting_info/voter.html")
 


# def voter_login(request):
    
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         voter_card_number = request.POST.get('voter_card_number')
#         password = request.POST.get('password')

#         voter = authenticate(username=username, email=email, voter_card_number=voter_card_number, password=password)

#         if voter:
#             if voter.is_active:
#                 login(request,voter)
#                 return HttpResponseRedirect(reverse('index'))
            
#             else:
#                 return HttpResponse("ACCOUNT NOT ACTIVE")
            
#         else:   
#             print("someone tried to login and failed!")
#             print("username: {}  and password {}".format(username,password))
#             return HttpResponse("invalid login details supplied")
        
#     else:
#         return render(request, "login.html", {})



#login
# if request.method =='POST':
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')

    #     user = authenticate(request, username=username, password=password)

    #     if user is not None:
    #         login(request, user)
    #         return redirect('landing_page')
    #     else:
    #         messages.info(request, 'Username or password is incorrect')
            

    # context = {}


    #signup
    # form = CreateUserForm()

    # if request.method == "POST":
    #     form = CreateUserForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         user = form.cleaned_data.get('username')
    #         messages.success(request, 'Account was created for' + user)
    #         return redirect('login')
        
        
    # context = {'form':form}