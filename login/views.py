from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
import urllib
from django.contrib.auth.models import User
from login.models import UserProfile, Recently_Submitted, Department, Course, Books
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
import hashlib, random



def index(request):
    return render(request, 'login/login.html')

def checklogin(request):
	if request.method == 'POST':
		umail = request.POST.get('umail', '')
		password = request.POST.get('password', '')
		#check if valid user
		try:
			user = User.objects.get(email=umail)
		except ObjectDoesNotExist:
			response = {'exist': 'false', 'password': ''}
			return JsonResponse(response)
		valid = authenticate(username=user.username, email=umail, password=password)
		if valid is not None:
			if user.is_active:
				login(request, valid)
				response = {'exist': 'true', 'password': 'valid'}
				return JsonResponse(response)
			else:
				response = {'exist': 'true', 'password': 'not verified'}
				return JsonResponse(response)
		else:
			response = {'exist': 'true', 'password': 'invalid'}
		return JsonResponse(response)

def checkValue(request):
	c = {}
	c.update(csrf(request))
	if request.method == 'GET':
		if(request.GET.get('type') == 'umail'): #check umail
			umail = request.GET.get('umail', '')
			try:
				user = User.objects.get(email=umail)
			except ObjectDoesNotExist:
				return JsonResponse({'taken': 'no'})
			return JsonResponse({'taken': 'yes'})
		else:
			username = request.GET.get('userName', '')
			try:
				user = User.objects.get(username=username)
			except ObjectDoesNotExist:
				return JsonResponse({'taken': 'no'})
			return JsonResponse({'taken': 'yes'})

def register(request):
	if request.method == 'POST':
		umail = request.POST.get('regUmail', '')
		password = request.POST.get('regPassword', '')
		username = request.POST.get('userName', '')
		salt = hashlib.sha1(str(random.random())).hexdigest()[:5]            
        activation_key = hashlib.sha1(salt+umail).hexdigest()
        user = User.objects.create_user(username, umail, password)
        user.is_active = False
        user.save()
        new_profile = UserProfile(user=user, activation_key=activation_key)
        new_profile.save()
        email_subject = 'SBB Account confirmation'
        email_body = "Hey %s, thanks for signing up. To activate your account, click this link http://127.0.0.1:8000/confirm/%s" % (username, activation_key)
        send_mail(email_subject, email_body, 'sbb.ucsb@gmail.com', [umail], fail_silently=False)
        return HttpResponse()

def confirm(request, key):
	user_profile = get_object_or_404(UserProfile, activation_key=key)
	user = user_profile.user
	user.is_active = True
	user.save()
	return HttpResponseRedirect('/')

@login_required
def home(request):
	recent_list = Recently_Submitted.objects.order_by('-date')[:10]
	return render(request, 'login/home.html', {'recent_list': recent_list})

@login_required
def deptlist(request):
	depts = Department.objects.order_by('deptName')
	return render(request, 'login/dept.html', {'depts': depts})

@login_required
def classlist(request, department):
	classlist = Course.objects.filter(dept=department).order_by('courseNo')
	return render(request, 'login/classlist.html', {'classlist': classlist})

@login_required
def course(request, department, code):
	try:
		course = Course.objects.get(pk="%s %s" % (department, code))
	except ObjectDoesNotExist:
		return render(request, 'login/course.html', {'course': [], 'books': []})
	books = Books.objects.filter(course=course).order_by('-date')
	return render(request, 'login/course.html', {'course': course, 'books': books})

@login_required
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
		newBook = Books(course=course, title=title, author=author, edition=edition, dLink=link, uploader=request.user.username)
		newBook.save()
		recent = Recently_Submitted(book=newBook)
		recent.save()
		return JsonResponse({'success': 'pass'})

@login_required
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

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))