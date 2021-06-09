from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.
from form.forms import SubmitForm


def home(request):
	#return HttpResponse("<h1>hey home page</h1>")
	form=SubmitForm()
	if request.method=="POST":
		form=SubmitForm(request.POST)
		if form.is_valid():
			form.save()
			name=form.cleaned_data.get('first_name')
			messages.success(request, f'Hi {name} congratulations!, your firm is submitted')
			return redirect('about')

	else:
		context={
		'form':form
		}
		return render(request,'form/home.html', context)

def about(request):
	return render(request, 'form/about.html')
