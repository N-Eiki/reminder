from django.core.management.base import BaseCommand
from remind.util.tool import message_create, job
from remind.models import SubjectModel
 
class Command(BaseCommand):
    def handle(self, *args, **options):
        job()