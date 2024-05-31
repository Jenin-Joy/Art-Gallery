from django.urls import path
from User import views
app_name="User"
urlpatterns = [
    path('homepage/',views.homepage,name="homepage"),
    path('My_profile/',views.my_pro,name="my_pro"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('changepassword/',views.changepassword,name="changepassword"),

    path('POSTComplaint/',views.POSTComplaint,name="POSTComplaint"),
    path('delComplaint/<int:did>',views.delComplaint,name="delComplaint"),

    path('UserFeedback/', views.UserFeedback, name='UserFeedback'),
    path('ViewWork/', views.ViewWork, name='ViewWork'),

    path('viewprogram/', views.viewprogram, name='viewprogram'),
    path('viewprogramvideo/<int:id>', views.viewprogramvideo, name='viewprogramvideo'),
    path('bookprogram/<int:id>', views.bookprogram, name='bookprogram'),
    path('program_payment/<int:id>', views.program_payment, name='program_payment'),

    path('delFeedback/<int:did>',views.delFeedback,name="delFeedback"),
    path('buynow/<int:id>',views.buynow,name="buynow"),
    path('loader/', views.loader, name='loader'),
    path('paymentsuc/', views.paymentsuc, name='paymentsuc'),

    path('viewbooking/', views.viewbooking, name='viewbooking'),
    path('viewproduct/<int:id>', views.viewproduct, name='viewproduct'),
    path('cancel_booking/<int:id>', views.cancel_booking, name='cancel_booking'),

    path('addcart/<int:pid>',views.Addcart,name='addcart'),
    path("Mycart/", views.Mycart,name="mycart"),
    path("DelCart/<int:did>", views.DelCart,name="delcart"),
    path("CartQty/", views.CartQty,name="cartqty"),
    path("payment/", views.payment,name="payment"),

    path('rating/<int:mid>',views.rating,name="rating"),  
    path('ajaxstar/',views.ajaxstar,name="ajaxstar"),
    path('starrating/',views.starrating,name="starrating"),

    path('newrating/<int:mid>',views.newrating,name="newrating"),  
    path('newajaxstar/',views.newajaxstar,name="newajaxstar"),
    path('newstarrating/',views.newstarrating,name="newstarrating"),

    path('viewevent/',views.viewevent,name="viewevent"),
    path('viewevent_seat/<int:id>',views.viewevent_seat,name="viewevent_seat"),

    path('ticketbooking/',views.ticketbooking,name="ticketbooking"),
    path('ticketpayment/<int:id>',views.ticketpayment,name="ticketpayment"),
    path('tickets/<int:id>',views.tickets,name="tickets"),
    path('cancelbooking/',views.cancelbooking,name="cancelbooking"),


    path('bookchecking/',views.bookchecking,name="bookchecking"),
    path('logout/',views.logout,name="logout"),

]