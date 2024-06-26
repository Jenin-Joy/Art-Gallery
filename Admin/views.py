from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from User.models import *
from datetime import date,datetime
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

def LoadingHomePage(request):
    usercount = tbl_user.objects.all().count()
    artistcount = tbl_artist.objects.filter(artist_status=1).count()
    userdata = tbl_artist.objects.filter(artist_status=1)
    return render(request,"Admin/HomePage.html",{"user":usercount,"artist":artistcount,"userdata":userdata})

def logout(request):
    del request.session["aid"]
    return redirect("Guest:Login")

def districtInsertSelect(request):
    flage = 0
    dis=tbl_district.objects.all()
    if request.method=="POST":
        disName=request.POST.get('txtname')
        lowercase = disName.lower()
        for i in dis:
            lower = i.district_name.lower()
            # print(lower)
            if lower == lowercase:
                flage = flage + 1
        # print(flage)
        if flage > 0:
            return render(request,"Admin/District.html",{'msg':"Data Already Added"})
        else:
            tbl_district.objects.create(district_name=disName)
            return render(request,"Admin/District.html",{'data':dis})
    else:
        return render(request,"Admin/District.html",{'data':dis})

def delDistrict(request,did):
    tbl_district.objects.get(id=did).delete()
    return redirect("WebAdmin:districtInsertSelect")

def districtupdate(request,eid):
    editdata=tbl_district.objects.get(id=eid)
    if request.method=="POST":
        editdata.district_name=request.POST.get("txtname")
        editdata.save()
        return redirect("WebAdmin:districtInsertSelect")
    else:
        return render(request,"Admin\District.html",{"editdata":editdata})

def arttype(request):
    flage = 0
    dis=tbl_arttype.objects.all()
    if request.method=="POST":
        disName=request.POST.get('txtname')
        lowercase = disName.lower()
        for i in dis:
            lower = i.arttype_name.lower()
            # print(lower)
            if lower == lowercase:
                flage = flage + 1
        # print(flage)
        if flage > 0:
            return render(request,"Admin/Art_type.html",{'msg':"Data Already Added"})
        else:
            tbl_arttype.objects.create(arttype_name=disName)
            return redirect("WebAdmin:arttype")
    else:
        return render(request,"Admin/Art_type.html",{'data':dis})

def delarttype(request,did):
    tbl_arttype.objects.get(id=did).delete()
    return redirect("WebAdmin:arttype")

def editarttype(request,eid):
    editdata=tbl_arttype.objects.get(id=eid)
    if request.method=="POST":
        editdata.arttype_name=request.POST.get("txtname")
        editdata.save()
        return redirect("WebAdmin:arttype")
    else:
        return render(request,"Admin\Art_type.html",{"editdata":editdata})
        

def programtype(request):
    flage = 0
    dis=tbl_programtype.objects.all()
    if request.method=="POST":
        disName=request.POST.get('txtname')
        lowercase = disName.lower()
        for i in dis:
            lower = i.programtype_name.lower()
            # print(lower)
            if lower == lowercase:
                flage = flage + 1
        # print(flage)
        if flage > 0:
            return render(request,"Admin/Program_type.html",{'msg':"Data Already Added"})
        else:
            tbl_programtype.objects.create(programtype_name=disName)
            return redirect("WebAdmin:programtype")
    else:
        return render(request,"Admin/Program_type.html",{'data':dis})

def delprogramtype(request,did):
    tbl_programtype.objects.get(id=did).delete()
    return redirect("WebAdmin:programtype")

def editprogramtype(request,eid):
    editdata=tbl_programtype.objects.get(id=eid)
    if request.method=="POST":
        editdata.programtype_name=request.POST.get("txtname")
        editdata.save()
        return redirect("WebAdmin:programtype")
    else:
        return render(request,"Admin\Program_type.html",{"editdata":editdata})


def placeInsertSelect(request):
    flage = 0
    district = tbl_district.objects.all()
    data=tbl_place.objects.all()
    if request.method=="POST":
        placeName=request.POST.get('txtname')
        lowercase = placeName.lower()
        for i in data:
            lower = i.place_name.lower()
            if ((lower == lowercase) and (i.district.id == int(request.POST.get('sel_district')))):
                flage = flage + 1
        # print(flage)
        if flage > 0:
            return render(request,"Admin/Place.html",{'msg':"Data Already Added"})
        else:
            dis = tbl_district.objects.get(id=request.POST.get('sel_district'))
            tbl_place.objects.create(place_name=placeName,district=dis)
        return render(request,"Admin/Place.html",{'data':data})
    else:
        return render(request,"Admin/Place.html",{'data':data,"districtdata":district})

def delPlace(request,did):
    tbl_place.objects.get(id=did).delete()
    return redirect("WebAdmin:placeInsertSelect")

def placeupdate(request,eid):
    district = tbl_district.objects.all()
    editdata=tbl_place.objects.get(id=eid)
    if request.method=="POST":
        editdata.place_name=request.POST.get("txtname")
        dis = tbl_district.objects.get(id=request.POST.get('sel_district'))
        editdata.district = dis
        editdata.save()
        return redirect("WebAdmin:placeInsertSelect")
    else:
        return render(request,"Admin\Place.html",{"editdata":editdata,"districtdata":district})


def adminInsertSelect(request):
    data=tbl_admin.objects.all()
    if request.method=="POST":
        name=request.POST.get('txtname')
        contact=request.POST.get('txtcontact')
        email=request.POST.get('txtemail')
        pwd=request.POST.get('txtpwd')
        tbl_admin.objects.create(admin_name=name,admin_contact=contact,admin_email=email,admin_password=pwd)
        return render(request,"Admin/AdminRegistration.html",{'data':data})
    else:
        return render(request,"Admin/AdminRegistration.html",{'data':data})

def delAdminReg(request,did):
    tbl_admin.objects.get(id=did).delete()
    return redirect("WebAdmin:adminInsertSelect")

def adminRegUpdate(request,eid):
    editdata=tbl_admin.objects.get(id=eid)
    if request.method=="POST":
        editdata.admin_name=request.POST.get("txtname")
        editdata.admin_contact=request.POST.get("txtcontact")
        editdata.admin_email=request.POST.get("txtemail")
        editdata.admin_password=request.POST.get("txtpwd")
        editdata.save()
        return redirect("WebAdmin:adminInsertSelect")
    else:
        return render(request,"Admin\AdminRegistration.html",{"editdata":editdata})


def userListNew(request):
    userdata = tbl_user.objects.all()
    return render(request,"Admin/UserListNew.html",{"userdata":userdata})

def acceptuser(request,aid):
    user = tbl_user.objects.get(id=aid)
    user.user_status = 1
    user.save()
    return redirect("WebAdmin:LoadingHomePage")

def rejectuser(request,rid):
    user = tbl_user.objects.get(id=rid)
    user.user_status = 2
    user.save()
    return redirect("WebAdmin:LoadingHomePage")

def userListAccepted(request):
    userdata = tbl_user.objects.filter(user_status=1)
    return render(request,"Admin/UserListAccepted.html",{"userdata":userdata})

def userListRejected(request):
    userdata = tbl_user.objects.filter(user_status=2)
    return render(request,"Admin/UserListRejected.html",{"userdata":userdata})


#Artist

def ArtistListNew(request):
    userdata = tbl_artist.objects.filter(artist_status=0)
    accepted = tbl_artist.objects.filter(artist_status=1)
    rejected = tbl_artist.objects.filter(artist_status=2)
    return render(request,"Admin/ArtistListNew.html",{"userdata":userdata,"accepted":accepted,"rejected":rejected})

def acceptartist(request,aid):
    user = tbl_artist.objects.get(id=aid)
    email = user.artist_email
    user.artist_status = 1
    user.save()
    send_mail(
        'Respected Sir/Madam ',#subject
        "\rYour Registration is Accepted. Now you can login and use our site. " ,#body
        settings.EMAIL_HOST_USER,
        [email],
    )
    return redirect("WebAdmin:LoadingHomePage")

def rejectartist(request,rid):
    user = tbl_artist.objects.get(id=rid)
    email = user.artist_email
    user.artist_status = 2
    user.save()
    send_mail(
        'Respected Sir/Madam ',#subject
        "\rYour Registration is Rejected due to some issue. " ,#body
        settings.EMAIL_HOST_USER,
        [email],
    )
    return redirect("WebAdmin:LoadingHomePage")

def ArtistListAccepted(request):
    userdata = tbl_artist.objects.filter(artist_status=1)
    return render(request,"Admin/ArtistListAccepted.html",{"userdata":userdata})

def ArtistListRejected(request):
    userdata = tbl_artist.objects.filter(artist_status=2)
    return render(request,"Admin/ArtistListRejected.html",{"userdata":userdata})


#Master Entry
def CategoryInsertSelect(request):
    data=tbl_category.objects.all()
    if request.method=="POST":
        catName=request.POST.get('txtname')
        tbl_category.objects.create(category_name=catName)
        return redirect("WebAdmin:CategoryInsertSelect")
    else:
        return render(request,"Admin/Category.html",{'data':data})

def delCategory(request,did):
    tbl_category.objects.get(id=did).delete()
    return redirect("WebAdmin:CategoryInsertSelect")

def Categoryupdate(request,eid):
    editdata=tbl_category.objects.get(id=eid)
    if request.method=="POST":
        editdata.category_name=request.POST.get("txtname")
        editdata.save()
        return redirect("WebAdmin:CategoryInsertSelect")
    else:
        return render(request,"Admin\Category.html",{"editdata":editdata})



def SubCatInsertSelect(request):
    Category = tbl_category.objects.all()
    data=tbl_subcategory.objects.all()
    if request.method=="POST":
        subcatname=request.POST.get('txtname')
        cat = tbl_category.objects.get(id=request.POST.get('sel_cat'))
        tbl_subcategory.objects.create(subcat_name=subcatname,category=cat)
        return redirect("WebAdmin:SubCatInsertSelect")
    else:
        return render(request,"Admin/SubCategory.html",{'data':data,"catdata":Category})

def delSubCategory(request,did):
    tbl_subcategory.objects.get(id=did).delete()
    return redirect("WebAdmin:SubCatInsertSelect")

def SubCategoryupdate(request,eid):
    catdata = tbl_category.objects.all()
    editdata=tbl_subcategory.objects.get(id=eid)
    if request.method=="POST":
        editdata.subcat_name=request.POST.get("txtname")
        cat = tbl_category.objects.get(id=request.POST.get('sel_cat'))
        editdata.category = cat
        editdata.save()
        return redirect("WebAdmin:SubCatInsertSelect")
    else:
        return render(request,"Admin\SubCategory.html",{"editdata":editdata,"catdata":catdata})


def ComplaintListNew(request):
    userdata=tbl_user.objects.all()
    userComplaint=tbl_complaint.objects.filter(complaint_status=0,user__in=userdata)
    solved=tbl_complaint.objects.filter(complaint_status=1,user__in=userdata)
    return render(request,"Admin/ComplaintListNew.html",{'userComplaint':userComplaint,"solved":solved})

def ComplaintReply(request,cid):
    complaint = tbl_complaint.objects.get(id=cid)
    if request.method=="POST":
        complaint.complaint_replydate = date.today()
        complaint.complaint_reply=request.POST.get('txtreply')
        complaint.complaint_status=1
        complaint.save()
        return redirect("WebAdmin:LoadingHomePage")
    else:
        return render(request,"Admin/ComplaintListReply.html",{'complaint':complaint})
    
def ComplaintSolved(request):
    userdata=tbl_user.objects.all()
    userComplaint=tbl_complaint.objects.filter(complaint_status=1,user__in=userdata)
    return render(request,"Admin/ComplaintListSolved.html",{'userComplaint':userComplaint})
    

def viewfeedback(request):
    artist = tbl_artist.objects.all()
    user = tbl_user.objects.all()
    userdata=tbl_feedback.objects.filter(user__in=user)
    artistdata=tbl_feedback.objects.filter(artist__in=artist)
    return render(request,"Admin/View_Feedback.html",{'artist':artistdata,"user":userdata})

def addevent(request):
    event = tbl_event.objects.all()
    if request.method == "POST":
        tbl_event.objects.create(event_name=request.POST.get("txt_name"),
                                event_start_date=request.POST.get("txt_sdate"),
                                event_end_date=request.POST.get("txt_edate"),
                                event_details=request.POST.get("txt_details"),
                                event_seat=request.POST.get("txt_seat"),
                                event_amount=request.POST.get("txt_seat_amt"),
                                event_image=request.FILES.get("txt_image"))
        return render(request,"Admin/Add_Events.html",{"msg":"Event Added Sucessfully.."})
    else:
        return render(request,"Admin/Add_Events.html",{"data":event})

def delevent(request,id):
    tbl_event.objects.get(id=id).delete()
    return redirect("WebAdmin:addevent")

def viewticketbooking(request,id):
    book = tbl_ticket_booking.objects.filter(event=id)
    event = tbl_event.objects.get(id=id)
    bookcount = tbl_tickets.objects.filter(booking__event=id,booking__booking_status=1,status=0).count()
    remain = int(event.event_seat) - int(bookcount)
    return render(request,"Admin/View_Ticket_Booking.html",{"data":book,"booking":bookcount,"remain":remain})