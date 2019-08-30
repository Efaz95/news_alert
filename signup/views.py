from django.shortcuts import render
from django.http import HttpResponse
from .models import User


# Create your views here.
def signup(request):
	if request.method == 'POST':
		if request.POST.get('fname') and request.POST.get('lname') and request.POST.get('email'):
			user=User()
			user.first_name= request.POST.get('fname')
			user.last_name= request.POST.get('lname')
			user.email= request.POST.get('email')
			user.save()

			return HttpResponse("Success") 

		else:
			return HttpResponse('Failed')

	return render(request, 'signup/signup.html')