from django.urls import path
from Artist import views
app_name="Artist"
urlpatterns = [
    path('homepage/',views.homepage,name="homepage"),
    path('My_profile/',views.my_pro,name="my_pro"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('changepassword/',views.changepassword,name="changepassword"),
    path('addwork/',views.addwork,name="addwork"),
    path('delwork/<int:id>',views.delwork,name="delwork"),

    path('addprogram/',views.addprogram,name="addprogram"),
    path('delprogram/<int:id>',views.delprogram,name="delprogram"),

    path('program_verification/<int:id>/<int:val>',views.program_verification,name="program_verification"),


    path('viewbooking/',views.viewbooking,name="viewbooking"),
    path('viewproduct/<int:id>', views.viewproduct, name='viewproduct'),
    path('delivered/<int:id>',views.delivered,name="delivered"),
    path('logout/',views.logout,name="logout"),

]