from django.urls import path
# from .views import signupfunc,loginfunc, homefunc, logoutfunc, detailfunc,dataDelete,remindfunc
from django.conf.urls import url
from . import views

urlpatterns = [
    path('signup/', views.signupfunc, name="signup"),
    path('login/', views.loginfunc, name="login"),
    path('home/', views.homefunc, name="home"),
    path('', views.homefunc, name="home"),
    path("logout/", views.logoutfunc, name="logout"),
    path('detail/<day>/<int:timetable>', views.detailfunc, name="detail"),
    path('delete/<int:pk>', views.dataDelete.as_view(), name="delete"),
    path("remind/", views.remindfunc, name="remind"), 
    path('settings', views.settingsfunc, name="settings"),
]