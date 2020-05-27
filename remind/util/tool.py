from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from remind.models import SubjectModel,Profile
import datetime
import requests

def job(username):
    # line_notify_token="Au0ZoMVcud0qyHZzV8vJ3apJywFO5EqwiI6olYfWS9b"
    line_notify_api = 'https://notify-api.line.me/api/notify'
    class_msg, task_msg = get_message(username)
    try:
        line_notify_token = get_token(username)
        headers = {'Authorization': 'Bearer ' + line_notify_token}  # 発行したトークン
        toUser = str(username)+"さん\n"
        if len(class_msg)>1:
            for c,t in zip(class_msg, task_msg):
                payload = {'message': toUser+"講義のリマインドです\n"+c}
                line_notify = requests.post(line_notify_api, data=payload, headers=headers)
                payload = {'message': toUser+"課題のリマインドです\n"+t}
                line_notify = requests.post(line_notify_api, data=payload, headers=headers)
        else:
                payload = {'message': toUser+"今日の講義はありません\n他の日の課題を終わらせてしまいましょう！"}
                line_notify = requests.post(line_notify_api, data=payload, headers=headers)
        print(payload)
    except:
        print()


def get_message(username):
    week=["月","火","水","木","金","土","日"]
    weekday=week[datetime.date.today().weekday()]
    remind_classes=[]
    remind_tasks=[]
    for i in range(6):
        try:
            data = SubjectModel.objects.get(user=username, weekday=weekday, timetable=str(format(i+1)))
            remind_classes.append(str(weekday+"曜日 "+str(i+1)+"時限目"+data.remind_class))
            remind_tasks.append(str(weekday+"曜日"+str(i+1)+"時限目"+data.remind_task))
        except:
            pass
    # data = SubjectModel.objects.get(user=username, weekday="月", timetable=3)
    # remind_classes.append(data.remind_class)
    # remind_tasks.append(data.remind_task)
    return remind_classes,remind_tasks


def get_token(username):
    token = Profile.objects.get(user=username).sns_id
    return token