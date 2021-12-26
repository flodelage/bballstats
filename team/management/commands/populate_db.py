
from django.core.management.base import BaseCommand
from django.core import management


class Command(BaseCommand):
    """
    Command that populates current database
    by calling all fixtures.
    """

    help = "Populate current database"

    def handle(self, *args, **kwargs):
        management.call_command('loaddata', 'profiles')
        management.call_command('loaddata', 'teams')
        management.call_command('loaddata', 'players')
        management.call_command('loaddata', 'games')
        management.call_command('loaddata', 'statistics')
