from django.contrib import admin
from django.urls import path
from Admin import views

app_name="WebAdmin"

urlpatterns = [
    path('admin/', admin.site.urls),

    path('HomePage/',views.LoadingHomePage,name="LoadingHomePage"),

    path('District/', views.districtInsertSelect,name="districtInsertSelect"),
    path('delDistrict/<int:did>', views.delDistrict,name="delDistrict"),
    path('districtupdate/<int:eid>',views.districtupdate,name="districtupdate"),

    path('arttype/', views.arttype,name="arttype"),
    path('delarttype/<int:did>', views.delarttype,name="delarttype"),
    path('editarttype/<int:eid>',views.editarttype,name="editarttype"),

    path('programtype/', views.programtype,name="programtype"),
    path('delprogramtype/<int:did>', views.delprogramtype,name="delprogramtype"),
    path('editprogramtype/<int:eid>',views.editprogramtype,name="editprogramtype"),

    path('AdminRegistration/', views.adminInsertSelect,name="adminInsertSelect"),
    path('delAdminReg/<int:did>', views.delAdminReg,name="delAdminReg"),
    path('adminRegUpdate/<int:eid>',views.adminRegUpdate,name="adminRegUpdate"),


    path('Place/', views.placeInsertSelect,name="placeInsertSelect"),
    path('delPlace/<int:did>', views.delPlace,name="delPlace"),
    path('placeupdate/<int:eid>',views.placeupdate,name="placeupdate"),

    path('UserListNew/',views.userListNew,name="userListNew"),
    path('acceptuser/<int:aid>',views.acceptuser,name="acceptuser"),
    path('rejectuser/<int:rid>',views.rejectuser,name="rejectuser"),
    path('UserListAccepted/',views.userListAccepted,name="userListAccepted"),
    path('UserListRejected/',views.userListRejected,name="userListRejected"),


    path('ArtistListNew/',views.ArtistListNew,name="ArtistListNew"),
    path('acceptartist/<int:aid>',views.acceptartist,name="acceptartist"),
    path('rejectartist/<int:rid>',views.rejectartist,name="rejectartist"),
    path('ArtistListAccepted/',views.ArtistListAccepted,name="ArtistListAccepted"),
    path('ArtistListRejected/',views.ArtistListRejected,name="ArtistListRejected"),

    path('Category/', views.CategoryInsertSelect,name="CategoryInsertSelect"),
    path('delCategory/<int:did>', views.delCategory,name="delCategory"),
    path('Categoryupdate/<int:eid>',views.Categoryupdate,name="Categoryupdate"),

    path('SubCategory/', views.SubCatInsertSelect,name="SubCatInsertSelect"),
    path('delSubCategory/<int:did>', views.delSubCategory,name="delSubCategory"),
    path('SubCategoryupdate/<int:eid>',views.SubCategoryupdate,name="SubCategoryupdate"),
    
    path('logout/',views.logout,name="logout"),

    path('ComplaintListNew/',views.ComplaintListNew,name="ComplaintListNew"),
    path('ComplaintReply/<int:cid>',views.ComplaintReply,name="ComplaintReply"),
    path('ComplaintSolved/',views.ComplaintSolved,name="ComplaintSolved"),


    path('UserFeedbackNew/',views.UserFeedbackNew,name="UserFeedbackNew"),
]