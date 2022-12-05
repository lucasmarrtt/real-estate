from django.shortcuts import render
from . models import Agent, Property 
from django.http import Http404

# Create your views here.

def index(request):
	property_list = Property.objects.all()

	context = {
		'property_list': property_list
		}
	return render(request, 'index.html', context)


def detalhes_do_imovel(request, slug=None):
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
