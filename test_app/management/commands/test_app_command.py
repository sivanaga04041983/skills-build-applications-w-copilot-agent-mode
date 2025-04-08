from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Test command in test_app to verify command discovery'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Test app command executed successfully.'))
