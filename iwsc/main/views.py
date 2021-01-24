from django.shortcuts import render, redirect
from .models import Blog 
from django.contrib import messages
from django.core.mail import send_mail
from .form import ContactForm
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse_lazy
from django.core.paginator import Page,Paginator,PageNotAnInteger,EmptyPage

def home(request):
	return render(request = request,
		 		  template_name = "home.html",
				  
				  )
def about(request):
	return render(request = request,
		 		  template_name = "about.html",
				  # context = {"blogs" : blog.objects.all}
				  )



def contact(request):
	if request.method=='POST':
		message_name = request.POST['name']
		message_email = request.POST['mail']
		# message_contact = request.POST['contact']
		message = request.POST['message']

		send_mail(
			'Message from '+message_name, #subject
			message +' Send a reply to this query at : '+message_email,  #message
			message_email ,  # from emails
			['iwsc.igdtuw@gmail.com'],
		)
		messages.info(request , message_name)
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			messages.info(request,'Thanks ,We have recieved your email and will respond shortly...') 

		else :
			messages.error(request,'Enter Correct Data') 

	form = ContactForm()
	return render(request,'contact.html',{'form':form} )
	

def blog(request):
	blogArr= Blog.objects.all()
	page = request.GET.get('page', 1)
	paginator = Paginator(blogArr, 18)
	try:
		bblog = paginator.page(page)
	except PageNotAnInteger:
		bblog = paginator.page(1)
	except EmptyPage:
		bblog = paginator.page(paginator.num_pages)
	blogArr1=Blog.objects.order_by().values('opportunity_type').distinct()
	
	opp_val = request.GET.get('role')
	city_val = request.GET.get('city')
	district_val = request.GET.get('role')
	if opp_val !='' and opp_val is not None :
		bblog = blogArr.filter(opportunity_type__icontains = opp_val)
	elif city_val !='' and city_val is not None :

		bblog = blogArr.filter(city__icontains = city_val) 

	if not blogArr :
		messages.error(request,'Currently there are 0 blogs')
	context = {
		'blogArr' : blogArr,
		'blogArr1' : blogArr1,
		'bblog' : bblog
	}
	return render(request= request, 
				  template_name = "blog.html",
				  context = context)

