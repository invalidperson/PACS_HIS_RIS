from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def register_request(request):
    # return HttpResponse("Connected!")
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("home_app:home")
    messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request,"accounts/register.html",{"register_form":form})



def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				# return redirect("patient:patient_dashboard")
				return redirect(request.GET.get('next'))
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="accounts/login.html", context={"login_form":form,"message":messages})



def account_nav(request):
	if request.method == "POST":
		patient_form = AuthenticationForm(request, data=request.POST)
		if patient_form.is_valid():
			
			username = patient_form.cleaned_data.get('username')
			password = patient_form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")

				if 'patient_login' in request.POST:
					return redirect("patient:patient_dashboard")
				elif 'doctor_login' in request.POST:
					return redirect("doctor:doctor_dashboard")
				elif 'operator_login' in request.POST:
					return redirect("lab_operator:labop_dashboard")



				# return redirect("patient:patient_dashboard")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	else:
		patient_form = AuthenticationForm()
		return render(request,"accounts/account_nav.html",{"patient_form":patient_form,"message":messages})


def logout_request(request):
    logout(request)

    messages.info(request, "You have successfully logged out.") 
    return redirect("home_app:home")