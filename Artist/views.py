from django.shortcuts import render,redirect
from Guest.models import *
from Artist.models import *
from User.models import *
# Create your views here.

def homepage(request):
    return render(request,"Artist/HomePage.html")

def logout(request):
    del request.session["artid"]
    return redirect("Guest:Login")

def my_pro(request):
    data=tbl_artist.objects.get(id=request.session["artid"])
    return render(request,"Artist/MyProfile.html",{'data':data})

def editprofile(request):
    prodata=tbl_artist.objects.get(id=request.session["artid"])
    if request.method=="POST":
        prodata.artist_name=request.POST.get('txtname')
        prodata.artist_contact=request.POST.get('txtcon')
        prodata.artist_email=request.POST.get('txtemail')
        prodata.save()
        return render(request,"Artist/EditProfile.html",{'msg':"Profile Updated"})
    else:
        return render(request,"Artist/EditProfile.html",{'prodata':prodata})

def editprofilephoto(request):
    prodata=tbl_artist.objects.get(id=request.session["artid"])
    if request.method == "POST":
        prodata.artist_photo = request.FILES.get("txt_photo")
        prodata.save()
        return render(request,"Artist/EditProfile.html",{'msg':"Profile Photo Updated"})
    else:
        return render(request,"Artist/EditProfilePhoto.html",{"photo":prodata})

def changepassword(request):
    if request.method=="POST":
        ccount=tbl_artist.objects.filter(id=request.session["artid"],artist_password=request.POST.get('txtcurpass')).count()
        if ccount>0:
            if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                userdata=tbl_artist.objects.get(id=request.session["artid"],artist_password=request.POST.get('txtcurpass'))
                userdata.artist_password=request.POST.get('txtnewpass')
                userdata.save()
                return render(request,"Artist/ChangePassword.html",{'msg':"Password Updated"})
            else:
                return render(request,"Artist/ChangePassword.html",{'msg1':"Error in confirm Password"})
        else:
            return render(request,"Artist/ChangePassword.html",{'msg1':"Error in current password"})
    else:
        return render(request,"Artist/ChangePassword.html")

def addwork(request):
    atype = tbl_arttype.objects.all()
    work = tbl_artistwork.objects.filter(artist=request.session["artid"])
    if request.method=="POST":
        tbl_artistwork.objects.create(artist=tbl_artist.objects.get(id=request.session["artid"]),
                                    arttype=tbl_arttype.objects.get(id=request.POST.get("sel_arttype")),
                                    work_caption=request.POST.get("txt_caption"),
                                    work_details=request.POST.get("txt_details"),
                                    work_image=request.FILES.get("txt_image"),
                                    work_price=request.POST.get("txt_price"))
        return redirect("Artist:addwork")
    else:
        return render(request,"Artist/Add_works.html",{"data":work,"arttype":atype})

def editwork(request,id):
    atype = tbl_arttype.objects.all()
    work = tbl_artistwork.objects.get(id=id)
    if request.method == "POST":
        if request.FILES.get("txt_image"):
            work.arttype = tbl_arttype.objects.get(id=request.POST.get("sel_arttype"))
            work.work_caption = request.POST.get("txt_caption")
            work.work_details = request.POST.get("txt_details")
            work.work_image = request.FILES.get("txt_image")
            work.work_price = request.POST.get("txt_price")
            work.save()
            return render(request,"Artist/Add_works.html",{"msg":"Data Updated"})
        else:
            work.arttype = tbl_arttype.objects.get(id=request.POST.get("sel_arttype"))
            work.work_caption = request.POST.get("txt_caption")
            work.work_details = request.POST.get("txt_details")
            work.work_price = request.POST.get("txt_price")
            work.save()
            return render(request,"Artist/Add_works.html",{"msg":"Data Updated"})
    else:
        return render(request,"Artist/Add_works.html",{"work":work,"arttype":atype})

def updatestock(request,id):
    if request.method == "POST":
        data = tbl_artistwork.objects.get(id=id)
        old_stock = data.work_stock
        new_stock = request.POST.get("txt_stock")
        total = int(old_stock) + int(new_stock)
        data.work_stock = total
        data.save()
        return render(request,"Artist/Update_stock.html",{"msg":"Stock Updated.."})
    else:
        return render(request,"Artist/Update_stock.html")

def delwork(request,id):
    tbl_artistwork.objects.get(id=id).delete()
    return redirect("Artist:addwork")

def addprogram(request):
    atype = tbl_programtype.objects.all()
    work = tbl_artistprogram.objects.filter(artist=request.session["artid"])
    if request.method=="POST":
        tbl_artistprogram.objects.create(artist=tbl_artist.objects.get(id=request.session["artid"]),
                                    programtype=tbl_programtype.objects.get(id=request.POST.get("sel_arttype")),
                                    program_caption=request.POST.get("txt_caption"),
                                    program_details=request.POST.get("txt_details"),
                                    program_image=request.FILES.get("txt_image"),
                                    program_price=request.POST.get("txt_price"))
        return redirect("Artist:addprogram")
    else:
        return render(request,"Artist/Add_Programs.html",{"data":work,"programtype":atype})

def editprogram(request,id):
    atype = tbl_programtype.objects.all()
    work = tbl_artistprogram.objects.get(id=id)
    if request.method == "POST":
        if request.FILES.get("txt_image"):
            work.programtype=tbl_programtype.objects.get(id=request.POST.get("sel_arttype"))
            work.program_caption=request.POST.get("txt_caption")
            work.program_details=request.POST.get("txt_details")
            work.program_image=request.FILES.get("txt_image")
            work.program_price=request.POST.get("txt_price")
            work.save()
            return render(request,"Artist/Add_Programs.html",{"msg":"Data Updated"})
        else:
            work.programtype=tbl_programtype.objects.get(id=request.POST.get("sel_arttype"))
            work.program_caption=request.POST.get("txt_caption")
            work.program_details=request.POST.get("txt_details")
            work.program_price=request.POST.get("txt_price")
            work.save()
            return render(request,"Artist/Add_Programs.html",{"msg":"Data Updated"})
    else:
        return render(request,"Artist/Add_Programs.html",{"work":work,"programtype":atype})

def addprogramvideo(request,id):
    data = tbl_artistprogram_video.objects.filter(program=id)
    if request.method == "POST":
        tbl_artistprogram_video.objects.create(program_video=request.FILES.get("txt_program"),program=tbl_artistprogram.objects.get(id=id))
        return render(request,"Artist/Add_program_video.html",{"msg":"Program Video is added..","id":id})
    else:
        return render(request,"Artist/Add_program_video.html",{"data":data})

def delete_program_video(request,id):
    data = tbl_artistprogram_video.objects.get(id=id)
    pgm = data.program.id
    data.delete()
    return redirect("Artist:addprogramvideo",pgm)

def delprogram(request,id):
    data = tbl_artistprogram.objects.get(id=id)
    vid = tbl_artistprogram_video.objects.filter(program=data.id)
    for i in vid:
        i.delete()
    data.delete()
    return redirect("Artist:addprogram")

def viewbooking(request):
    bk = tbl_booking.objects.filter(work__artist=request.session["artid"])
    book = tbl_cart.objects.filter(product__artist=request.session["artid"])
    bks = []
    for b in book:
        bks.append(b.booking_id)
    books = tbl_new_booking.objects.filter(id__in=bks)
    program = tbl_programbooking.objects.filter(program__artist=request.session["artid"])
    return render(request,"Artist/View_booking.html",{"data":bk,"book":books,"program":program})

def viewproduct(request,id):
    cart = tbl_cart.objects.filter(booking=id)
    return render(request,"Artist/View_product.html",{"data":cart})

def delivered(request,id):
    bk = tbl_booking.objects.get(id=id)
    bk.booking_status = 1
    bk.save()
    return redirect("Artist:viewbooking")

def multidelivered(request,id):
    bk = tbl_new_booking.objects.get(id=id)
    bk.booking_status = 3
    bk.save()
    return redirect("Artist:viewbooking")

def program_verification(request,id,val):
    pg = tbl_programbooking.objects.get(id=id)
    pg.booking_status = val
    pg.save()
    return redirect("Artist:viewbooking")