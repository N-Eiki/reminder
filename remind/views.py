from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import SubjectModel
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
            return redirect('signup')
        else:
            return redirect('login')
    return render(request,"login.html")

def homefunc(request):
    weekdays = ["月", "火", "水", "木", "金"]
    all = SubjectModel.objects.all()
    #forのなかでa.user=ログインユーザー名の場合値を返すような感じ？
    alldata = []
    for all_data in all:
        if all_data.user=="admin":##ここにログインユーザー名を入れる
            sub_list = []
            sub_list.append(all_data.title)
            sub_list.append(all_data.weekday)
            sub_list.append(all_data.timetable)
            alldata.append(sub_list)
    print(len(alldata))
    return render(request, "home.html", {"weekdays":weekdays, "alldata":alldata})