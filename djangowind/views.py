from django.shortcuts import render # type: ignore

def index(request):
	return render(request, 'index.html')
def signin(request):
	return render(request, 'signin.html')
def signup(request):
	return render(request, 'signup.html')
def login(request):
	return render(request, 'login.html')
def error(request):
	return render(request, '404.html')

