from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from remind.models import SubjectModel

line_notify_token="Au0ZoMVcud0qyHZzV8vJ3apJywFO5EqwiI6olYfWS9b"
line_notify_api = 'https://notify-api.line.me/api/notify'

headers = {'Authorization': 'Bearer ' + line_notify_token}  # 発行したトークン


# msg_class=SubjectModel.objects.get(user=request.user, timetable=timetable,weekday=day).remind_class
# msg_task =SubjectModel.objects.get(user=request.user, timetable=timetable,weekday=day).remind_task

class LineMessage():
    def __init__(self, msg):
        self.msg_class=msg[0]
        self.msg_task=msg[1]

    def reply(self):
        payload = {
            "msg_class":self.msg_class,
            "msg_task" :self.msg_task
        }
        print(payload)


def message_create(data):
    return [data.remind_class, data.remind_task]


def LineNotifyMessage():
    line_notify_token="Au0ZoMVcud0qyHZzV8vJ3apJywFO5EqwiI6olYfWS9b"
    line_notify_api = 'https://notify-api.line.me/api/notify'
    message="\nthis is test notify"
    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + line_notify_token}  # 発行したトークン
    line_notify = requests.post(line_notify_api, data=payload, headers=headers)
