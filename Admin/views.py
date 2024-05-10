from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from User.models import *
from datetime import date
# Create your views here.

def LoadingHomePage(request):
    return render(request,"Admin/HomePage.html")

def logout(request):
    del request.session["aid"]
    return redirect("Guest:Login")

def districtInsertSelect(request):
    dis=tbl_district.objects.all()
    if request.method=="POST":
        disName=request.POST.get('txtname')
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
    dis=tbl_arttype.objects.all()
    if request.method=="POST":
        disName=request.POST.get('txtname')
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
    dis=tbl_programtype.objects.all()
    if request.method=="POST":
        disName=request.POST.get('txtname')
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
    district = tbl_district.objects.all()
    data=tbl_place.objects.all()
    if request.method=="POST":
        placeName=request.POST.get('txtname')
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
    return render(request,"Admin/ArtistListNew.html",{"userdata":userdata})

def acceptartist(request,aid):
    user = tbl_artist.objects.get(id=aid)
    user.artist_status = 1
    user.save()
    return redirect("WebAdmin:LoadingHomePage")

def rejectartist(request,rid):
    user = tbl_artist.objects.get(id=rid)
    user.artist_status = 2
    user.save()
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
    return render(request,"Admin/ComplaintListNew.html",{'userComplaint':userComplaint})

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
    

def UserFeedbackNew(request):
    data=tbl_feedback.objects.filter(feedback_status=0)
    return render(request,"Admin/UserFeedBack.html",{'data':data})