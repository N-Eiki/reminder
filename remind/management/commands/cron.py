from django.core.management.base import BaseCommand
from remind.util.tool import job
from remind.models import SubjectModel
 
class Command(BaseCommand):
    def handle(self, *args, **options):
        job()