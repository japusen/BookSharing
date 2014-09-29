from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.core.context_processors import csrf
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
import urllib
from datetime import datetime
from login.models import UserInfo, Recently_Submitted, Department, Course, Books

def index(request):
    return render(request, 'login/login.html')

def checklogin(request):
	if request.method == 'POST':
		umail = request.POST.get('umail', '')
		#check if valid user
		try:
			user = UserInfo.objects.get(pk=umail)
		except ObjectDoesNotExist:
			response = {'success': 'false', 'umail': '', 'password': ''}
			return JsonResponse(response)
		response = {'success': 'true', 'umail': user.umail, 'password': user.password}
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

def home(request):
	recent_list = Recently_Submitted.objects.order_by('-date')[:10]
	return render(request, 'login/home.html', {'recent_list': recent_list})

def deptlist(request):
	depts = Department.objects.order_by('deptName')
	return render(request, 'login/dept.html', {'depts': depts})

def classlist(request, department):
	classlist = Course.objects.filter(dept=department).order_by('courseNo')
	return render(request, 'login/classlist.html', {'classlist': classlist})

def course(request, department, code):
	try:
		course = Course.objects.get(pk="%s %s" % (department, code))
	except ObjectDoesNotExist:
		return render(request, 'login/course.html', {'course': [], 'books': []})
	books = Books.objects.filter(course=course)
	return render(request, 'login/course.html', {'course': course, 'books': books})

def addBook(request):
	if request.method == 'POST':
		courseCode = request.POST.get('courseCode', '')
		title = request.POST.get('title', '')
		author = request.POST.get('author', '')
		edition = request.POST.get('edition', '')
		link = request.POST.get('link', '')
		try:
			course = Course.objects.get(pk=courseCode)
		except ObjectDoesNotExist:
			return JsonResponse({'success': 'fail'})
		newBook = Books(course=course, title=title, author=author, edition=edition, dLink=link)
		newBook.save()
		recent = Recently_Submitted(book=newBook)
		recent.save()
		return JsonResponse({'success': 'pass'})

def search(request):
	if request.method == 'GET':
		sinput = request.GET.get('course')
		try:
			department = sinput.split(" ", 1)[0].upper()
			code = sinput.split(" ", 1)[1].upper()
		except IndexError: #invalid input
			return render(request, 'login/course.html', {'course': [], 'books': []})
		try:
			course = Course.objects.get(pk="%s %s" % (department, code))
		except ObjectDoesNotExist:
			return render(request, 'login/course.html', {'course': [], 'books': []})
		books = Books.objects.filter(course=course)
		return render(request, 'login/course.html', {'course': course, 'books': books})