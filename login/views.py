from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.core.context_processors import csrf
from login.models import UserInfo


def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'login/home.html')

def login(request):
	if request.method == 'POST':
		umail = request.POST.get('umail', '')
		#check if valid user
		try:
			user = UserInfo.objects.get(pk=umail)
			password = user.password
		except ObjectDoesNotExist:
			umail = ''
			password = ''
		response = {'umail': umail, 'password': password}
		return JsonResponse(response)

def checkValue(request):
	c = {}
	c.update(csrf(request))
	if request.method == 'GET':
		if(request.GET.get('type') == 'umail'): #check umail
			umail = request.GET.get('umail', '')
			try:
				user = UserInfo.objects.get(umail=umail)
			except ObjectDoesNotExist:
				return JsonResponse({'taken': 'no'})
			return JsonResponse({'taken': 'yes'})
		else:
			username = request.GET.get('userName', '')
			try:
				user = UserInfo.objects.get(username=username)
			except ObjectDoesNotExist:
				return JsonResponse({'taken': 'no'})
			return JsonResponse({'taken': 'yes'})

def register(request):
	if request.method == 'POST':
		umail = request.POST.get('regUmail', '')
		password = request.POST.get('regPassword', '')
		verify = request.POST.get('finalPassword', '')
		username = request.POST.get('userName', '')

		insert = UserInfo(umail=umail, password=password, username=username)
		insert.save()
		return HttpResponse()