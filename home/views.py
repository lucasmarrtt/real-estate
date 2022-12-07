from django.shortcuts import render
from . models import *
from django.http import Http404

# Filter 
from . filters import PropertyFilter

# Create your views here.

def index(request):

	context = {}

	property = Property.objects.all()
	agent = Agent.objects.all()

	property_filter = PropertyFilter(
		request.GET,
		queryset=Property.objects.all()
	)

	context = {
		'property_list': property,
		'gent_list': agent, 
		'property_filter': property_filter
		}
		
	return render(request, 'index.html', context)


def property_list(request):
	property = Property.objects.all()

	context = {
		'property_list': property

	}
	return render(request, 'lista-de-propriedades.html', context)


def property_detail(request, slug=None):
	property_list = Property.objects.all()
	property_obj = None 
	if slug is not None:
		property_obj = Property.objects.get(slug=slug)
		try:
		    property_obj = Property.objects.get(slug=slug)
		except Property.DoesNotExist:
			raise Http404
		except Property.MultipleObjectsReturned:
		    property_obj = Property.objects.filter(slug=slug).first()	
		except:
			raise Http404
		    	        
	context = {
	    'property_obj': property_obj,
	    'property_list': property_list,
	}
	return render(request, 'detalhes-do-imovel.html', context)
