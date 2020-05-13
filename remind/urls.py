from django.urls import path
from .views import signupfunc,loginfunc, homefunc, logoutfunc, detailfunc,dataDelete

urlpatterns = [
    path('signup/', signupfunc, name="signup"),
    path('login/', loginfunc, name="login"),
    path('home/', homefunc, name="home"),
    path("logout/", logoutfunc, name="logout"),
    path('detail/<day>/<int:timetable>', detailfunc, name="detail"),
    path('delete/<int:pk>', dataDelete.as_view(), name="delete"),
]