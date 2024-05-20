from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

def index(request):
    return render(request,"Guest/index.html")

def userRegistration(request):
    district = tbl_district.objects.all()
    if request.method=="POST":
        place = tbl_place.objects.get(id=request.POST.get('sel_place'))
        tbl_user.objects.create(user_name=request.POST.get("txtname"),user_gender=request.POST.get("gender"),user_contact=request.POST.get("txtcontact"),user_email=request.POST.get("txtemail"),user_photo=request.FILES.get("fileImage"),user_password=request.POST.get("txtpwd"),user_address=request.POST.get("txt_address"),place=place)
        email = request.POST.get("txtemail")
        send_mail(
            'Respected Sir/Madam ',#subject
            "\rWelcome to Amaze Artsy. Your Registration is sucessfully completed." ,#body
            settings.EMAIL_HOST_USER,
            [email],
        )
        return redirect("Guest:userRegistration")
    else:
        return render(request,"Guest/NewUser.html",{"districtdata":district})

def artistRegistration(request):
    district = tbl_district.objects.all()
    if request.method=="POST":
        place = tbl_place.objects.get(id=request.POST.get('sel_place'))
        tbl_artist.objects.create(artist_address=request.POST.get("txtadd"),artist_about=request.POST.get("txtabout"),artist_name=request.POST.get("txtname"),artist_contact=request.POST.get("txtcontact"),artist_email=request.POST.get("txtemail"),artist_photo=request.FILES.get("fileImage"),artist_proof=request.FILES.get("fileProof"),artist_password=request.POST.get("txtpwd"),place=place)
        email = request.POST.get("txtemail")
        send_mail(
            'Respected Sir/Madam ',#subject
            "\rWelcome to Amaze Artsy. Your Registration is sucessfully completed. " ,#body
            settings.EMAIL_HOST_USER,
            [email],
        )
        return redirect("Guest:artistRegistration")
    else:
        return render(request,"Guest/NewArtist.html",{"districtdata":district})

def ajaxplace(request):
    dis = tbl_district.objects.get(id=request.GET.get("did"))
    place = tbl_place.objects.filter(district=dis)
    return render(request,"Guest/AjaxPlace.html",{"placedata":place})

def Login(request):
    if request.method == "POST":
        admincount = tbl_admin.objects.filter(admin_email=request.POST.get("txt_email"),admin_password=request.POST.get("txt_password")).count()
        usercount = tbl_user.objects.filter(user_email=request.POST.get("txt_email"),user_password=request.POST.get("txt_password")).count()
        artcount = tbl_artist.objects.filter(artist_status='1',artist_email=request.POST.get("txt_email"),artist_password=request.POST.get("txt_password")).count()
        if usercount > 0:
            user = tbl_user.objects.get(user_email=request.POST.get("txt_email"),user_password=request.POST.get("txt_password"))
            request.session["uid"] = user.id
            request.session["uname"] = user.user_name
            return redirect("User:homepage")
        elif admincount > 0:
            admin = tbl_admin.objects.get(admin_email=request.POST.get("txt_email"),admin_password=request.POST.get("txt_password"))
            request.session["aid"] = admin.id
            request.session["aname"] = admin.admin_name
            return redirect("WebAdmin:LoadingHomePage")
        elif artcount > 0:
            art = tbl_artist.objects.get(artist_email=request.POST.get("txt_email"),artist_password=request.POST.get("txt_password"))
            request.session["artid"] = art.id
            request.session["artname"] = art.artist_name
            return redirect("Artist:homepage")
        else:
            return render(request,"Guest/Login.html",{"msg":"Invalid Email Or Password"})
    else:
        return render(request,"Guest/Login.html")