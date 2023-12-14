
from django.core.management.base import BaseCommand, CommandError
from app.models import Zno


class Command(BaseCommand):
    help = "Delete all data from ZNO DB table"
    
    def handle(self, *args, **options):
            try:
                self.stdout.write(
                    self.style.SUCCESS('Started deleting all data from ZNO DB table')
                )
                Zno.objects.all().delete()
            except Exception as e:
                raise CommandError(f'Error while deleting all data to ZNO DB table: {e}')

            self.stdout.write(
                self.style.SUCCESS('Successfully deleted data to ZNO DB table')
            )
