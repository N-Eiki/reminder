from django.db import models

# Create your models here.
class SubjectModel(models.Model):
    user = models.CharField(max_length=100)#投稿者名
    title=models.CharField(max_length=100, blank=False)#科目名
    created_at = models.DateTimeField(auto_now_add=True)#作成日
    weekday = models.CharField(max_length=3)#時間割の曜日
    timetable=models.IntegerField()#時間割の時限
    remind = models.BooleanField(default=True)#通知をするか否か
    sns_id = models.CharField(max_length=100, blank=False)#通知を送るためのtoken
    remind_class = models.TextField()#リマインドするときの言葉
    remind_task = models.TextField()
