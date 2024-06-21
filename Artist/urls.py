from django.urls import path
from Artist import views
app_name="Artist"
urlpatterns = [
    path('homepage/',views.homepage,name="homepage"),
    path('My_profile/',views.my_pro,name="my_pro"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('editprofilephoto/',views.editprofilephoto,name="editprofilephoto"),
    path('changepassword/',views.changepassword,name="changepassword"),

    path('addwork/',views.addwork,name="addwork"),
    path('editwork/<int:id>',views.editwork,name="editwork"),
    path('updatestock/<int:id>',views.updatestock,name="updatestock"),
    path('delwork/<int:id>',views.delwork,name="delwork"),

    path('addprogram/',views.addprogram,name="addprogram"),
    path('editprogram/<int:id>',views.editprogram,name="editprogram"),
    path('addprogramvideo/<int:id>',views.addprogramvideo,name="addprogramvideo"),
    path('delete_program_video/<int:id>',views.delete_program_video,name="delete_program_video"),
    path('delprogram/<int:id>',views.delprogram,name="delprogram"),

    path('program_verification/<int:id>/<int:val>',views.program_verification,name="program_verification"),


    path('viewbooking/',views.viewbooking,name="viewbooking"),
    path('viewproduct/<int:id>', views.viewproduct, name='viewproduct'),
    path('delivered/<int:id>',views.delivered,name="delivered"),
    path('multidelivered/<int:id>',views.multidelivered,name="multidelivered"),

    path('feedback/',views.feedback,name="feedback"),
    path('delFeedback/<int:did>',views.delFeedback,name="delFeedback"),
    path('viewevent/',views.viewevent,name="viewevent"),

    path('viewrating/<int:wid>',views.viewrating,name="viewrating"),
    path('starrating/',views.starrating,name="starrating"),

    path('logout/',views.logout,name="logout"),

]