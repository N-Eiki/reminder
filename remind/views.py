from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import SubjectModel
from django.contrib.auth.decorators import login_required
from django.views.generic import DeleteView,CreateView
from django.urls import reverse_lazy
from .forms import RemindRadioForm,createForm
from django.views.decorators.csrf import csrf_exempt
import json
from .util.tool import LineMessage, message_create
from django.http import HttpResponse
from webpush import send_user_notification

# Create your views here.
def signupfunc(request):
    if request.method=="POST":
        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password"]
        try:
            User.objects.get(username=username)
            return render(request, "signup.html", {"error":"このユーザー名はすでに使用されています。"})
        except:
            user = User.objects.create_user(username, email, password)
            return redirect("home")
    else:
        return render(request, "signup.html")


def loginfunc(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    return render(request,"login.html")

@login_required
def homefunc(request):
    weekdays = ["月", "火", "水", "木", "金"]
    all = SubjectModel.objects.all()
    #forのなかでa.user=ログインユーザー名の場合値を返すような感じ？
    alldata = []
    for all_data in all:
        if all_data.user==str(request.user):##ここにログインユーザー名を入れる
            sub_list = []
            sub_list.append(all_data.title)
            sub_list.append(all_data.weekday)
            sub_list.append(all_data.timetable)
            alldata.append(sub_list)
    
    payload = {"head":"welcom", "body":"hello world"}
    send_user_notification(user=request.user, payload=payload, ttl=1000)
    params = {
        "alldata":alldata,
        "weekdays":weekdays,
    }

    return render(request, "home.html", params)

def logoutfunc(request):
    logout(request)
    return redirect("login")

@login_required
def detailfunc(request, day,timetable):
    remindmsg=""

    try:
        data = SubjectModel.objects.get(user=request.user, timetable=timetable,weekday=day)
        obj = SubjectModel.objects.get(user=request.user, weekday=day, timetable=timetable)
        remindmsg = "リマインド停止中です"
        if obj.remind:
            remindmsg = "リマインドします"
    except:
        data={"title":"予定なし", "pk":False}
    try:
        #予定なしからのポスト
        if "newPOST" in request.POST:
            return newPOST(request)
        elif "updatePOST" in request.POST:
            return updatePOST(request)#ポストの更新
        elif "deletePOST" in request.POST:
            return deletePOST(request)#ポストの削除
        else:
            raise("error")
    except:
        params = {
            "data": data,
            "timetable": timetable,
            "day": day,
            "radioForm": RemindRadioForm,
            "createForm": createForm,
            "remindmsg": remindmsg
        }
        return render(request, "detail.html", params)



def newPOST(request):
    obj = SubjectModel(
        user=request.user, title=request.POST.get('title'), weekday=request.POST.get("weekday"),
        timetable=request.POST.get('timetable'), sns_id=request.POST.get('sns_id'),
        remind_class=request.POST.get('remind_class'), remind_task=request.POST.get('remind_task'),
        remind=request.POST.get('remind'))
    obj.save()
    return redirect(to="home")

def updatePOST(request):
    obj = SubjectModel.objects.get(pk=request.POST.get("pk"))
    obj.title = request.POST.get('title')
    obj.remind = request.POST.get('remind')
    obj.sns_id=request.POST.get('sns_id')
    obj.remind_class = request.POST.get('remind_class')
    obj.remind_task = request.POST.get('remind_task')
    obj.save()
    return redirect(to="home")


def deletePOST(request):
    pk=request.POST.get('deletePk')
    obj = SubjectModel.objects.get(pk=pk)
    obj.delete()

    return redirect(to="home")

class dataDelete(DeleteView):
    model = SubjectModel
    success_url = reverse_lazy("home")




# from datetime import datetime, timedelta

# @csrf_exempt
# def remindfunc(request):
#     if request.method=="POST":
#         req = json.loads(request.body.decode('utf-8'))
#         events = req["events"]
#         day="月"
#         timetable="3"
#         data= msg_class=SubjectModel.objects.get(user="admin", timetable=timetable,weekday=day)
#         for event in events:
#             msg = message_create()
#             line_message = LineMessage(msg)
#             line_message.reply()

#         return HttpResponse('ok')

def remindfunc(req):
    return render(req, "remind.html")