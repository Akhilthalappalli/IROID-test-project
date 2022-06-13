from django.shortcuts import render,redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate,logout 
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import *
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
	print(request.user.id)
	res = Result.objects.filter(id=request.user.id)
	cat = Category.objects.all()
	return render(request,'dashboard.html',{'res':res,'cat':cat})


def quiz(request):
	wrong=0
	correct=0
	score=0
	questions=Quiz.objects.all()
	category=Category.objects.get(id=request.POST.get('category1'))
	print("------",category)
	for q in questions:
		if request.POST.get(q.question) == q.currect_answer:
			score += 1
			correct += 1
		elif request.POST.get(q.question) != q.currect_answer:
			wrong += 1
	obj = Result.objects.create(user_id=request.user,category = category,score=score,correct=correct,wrong=wrong)
	return redirect("app:dashboard")


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("app:dashboard")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})


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
				if user.usertype == 1:
					return redirect("app:admin_dashboard")
				else:
					return redirect("app:dashboard")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})	


def logout_request(request):
	logout(request)
	return redirect("app:login")	


@login_required
def admin_dashboard(request):
	user = GeneralUser.objects.all()
	ques = Quiz.objects.all()
	res = Result.objects.all()
	cat = Category.objects.all()
	return render(request,'admin_dashboard.html',{'user':user,'ques':ques,'res':res,'cat':cat})


@login_required
def category_filter(request):
	if request.method == 'POST':
		id = request.POST.get('select_id')
		cat = Category.objects.get(id=id)
		qus = Quiz.objects.filter(category=cat)
		return render(request,'quiz.html',{'qus':qus,'cat':cat})
		