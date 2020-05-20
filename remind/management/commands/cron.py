from django.core.management.base import BaseCommand
from remind.util.tool import job
from remind.models import SubjectModel
from django.contrib.auth.models import User

 
class Command(BaseCommand):
    def handle(self, *args, **options):
        users = User.objects.all()
        for u in users:
            print(u)
            job(u)