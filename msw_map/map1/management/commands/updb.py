from django.core.management.base import BaseCommand, CommandError
from map1.models import User
import time
import map1.msw_twitter_trends
import re
import sys
reload(sys)
sys.setdefaultencoding("utf8")
import django.utils.encoding
import unicodedata

class Command(BaseCommand):
    args = '<poll_id poll_id ...>'
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        for poll_id in args:
            try:
                poll = User.objects.get(pk=poll_id)
            except User.DoesNotExist:
                raise CommandError('User "%s" does not exist' % poll_id)

            #poll.opened = False
            #poll.save()

            self.stdout.write('Successfully found "%s"' % poll_id)

        while True:
            time.sleep(3)
            mt = map1.msw_twitter_trends.MyTrends()
            mt.authApi()
            res = mt.api.GetSearch('Christmas', count=100)
            #coor = False
            coors = []
            for r in res:
                #print json.dumps(r.AsDict(), indent=2) + '\n'
                #print('++++++++++++++++++++++++\n++++++++++++++++++++\n+++++++ COORDINATES ++++++++\n+++++++++++++++++\n+++++++++++')
                #print(r.coordinates)
                if(r.coordinates != None):
                    coors.append(r)
                    name = ''
                    mes = ''
                    print type(r.text)
                    print type(r.user.name)
                    
                    print(r.coordinates)
                    name = unicodedata.normalize('NFKD', r.user.name).encode('ascii','ignore')
                    mes = unicodedata.normalize('NFKD', r.text).encode('ascii','ignore')
                    print (name)
                    print (mes)
                    p = []
                    p = re.findall(r"[-+]?\d*\.\d+|\d+", str(r.coordinates))
                    new_tweet = User(name=name, message=name, latitude= 55, longtitude= 55)
                    new_tweet.save()
                    print(new_tweet.id)
            print len(coors)
            self.stdout.write('TEST')




