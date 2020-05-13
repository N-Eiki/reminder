from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import SubjectModel
from django.contrib.auth.decorators import login_required
from django.views.generic import DeleteView,CreateView
from django.urls import reverse_lazy
from .forms import RemindRadioForm


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
            return render(request, "sinup.html")
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
    errormsg=""
    try:
        data = SubjectModel.objects.get(user=request.user, timetable=timetable,weekday=day)
    except:
        data={"title":"予定なし", "pk":False}

    #予定なしからのポスト
    if(request.POST.get("newPOST")):
        newPOST(request, day, timetable)

    else:
        print('失敗')
    #更新のポスト
    # updatePOST(request, day, timetable)
    #削除のポスト
    # deletePOST(request, day, timetable)

    params = {
        "data":data,
        "timetable":timetable,
        "day":day,
        "radioForm":RemindRadioForm,
    }
    return render(request, "detail.html", params)


def newPOST(request, day, timetable):
    obj = SubjectModel(
        user=request.user, title=request.POST.get('title'), weekday=request.POST.get("weekday"),
        timetable=request.POST.get('timetable'), sns_id=request.POST.get('sns_id'),
        remind_class=request.POST.get('remind_class'), remind_task=request.POST.get('remind_task'),
        remind=request.POST.get('remind'))
    # obj.save()

    # print(request.POST.get("title"))
    # print(request.POST.get("weekday"))
    # print(request.POST.get("timetable"))
    # print(request.POST.get("sns_id"))
    # print(request.POST.get("remind_class"))
    # print(request.POST.get("remind_task"))
    # print(request.POST.get("remind"))
    # return redirect(to="home")

    # object = SubjectModel.objects.get(user=request.user, weekdays=day, timetabl=timetable)
    # print(object)
    # def updatePOST(request, day, timetable):
    # def deletePOST(request, day, timetable)


class dataDelete(DeleteView):
    model = SubjectModel
    success_url = reverse_lazy("home")



