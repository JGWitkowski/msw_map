from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from map1.models import User

@dajaxice_register
def sayhello(request):
	User.objects.all()
	return simplejson.dumps({'message': User.objects.all()[0].latitude})