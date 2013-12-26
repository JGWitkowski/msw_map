from django.core.management.base import BaseCommand, CommandError
from map1.models import User
import time

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
            self.stdout.write('TEST')

