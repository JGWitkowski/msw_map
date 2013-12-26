from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from map1.models import User

def index(request):
	trend_list = User.objects.all()
	template = loader.get_template('map1/index.html')
	context = RequestContext(request, {'trend_list': trend_list,})
	return HttpResponse(template.render(context))

def ajaxtest(request):
	#trend_list = User.objects.all()
	template = loader.get_template('map1/ajaxtest.html')
	context = RequestContext(request, {'trend_list': trend_list,})
	return HttpResponse(template.render(context))



