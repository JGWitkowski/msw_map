from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from map1.models import User

@dajaxice_register
def sayhello(request):
	newest = User.objects.latest('id')
	tweets = {}
	return simplejson.dumps({'name': newest.name, 'message': newest.message, 'latitude': newest.latitude, 'longtitude': newest.longtitude})