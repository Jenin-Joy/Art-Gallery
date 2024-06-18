from django.urls import path
from Guest import views
app_name="Guest"
urlpatterns = [
    path('NewUser/',views.userRegistration,name="userRegistration"),
    path('NewArtist/',views.artistRegistration,name="artistRegistration"),
    path('AjaxPlace/',views.ajaxplace,name="ajaxplace"),
    path('Login/',views.Login,name="Login"),
    path('',views.index,name="index"),
    path('ajaxemail/',views.ajaxemail,name="ajaxemail"),
]