from django.shortcuts import render

# Create your views here.
def signupfunc(request):
    if request.method=="POST":
        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password"]
        print(request.POST)
    return render(request, "signup.html", {"some":100})