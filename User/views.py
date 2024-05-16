from django.shortcuts import render,redirect
from Guest.models import *
from User.models import *
from Artist.models import *
from django.http import JsonResponse 
# Create your views here.

def homepage(request):
    return render(request,"User/HomePage.html")

def logout(request):
    del request.session["uid"]
    return redirect("Guest:Login")

def my_pro(request):
    data=tbl_user.objects.get(id=request.session["uid"])
    return render(request,"User/MyProfile.html",{'data':data})

def editprofile(request):
    prodata=tbl_user.objects.get(id=request.session["uid"])
    if request.method=="POST":
        prodata.user_name=request.POST.get('txtname')
        prodata.user_contact=request.POST.get('txtcon')
        prodata.user_email=request.POST.get('txtemail')
        prodata.save()
        return render(request,"User/EditProfile.html",{'msg':"Profile Updated"})
    else:
        return render(request,"User/EditProfile.html",{'prodata':prodata})

def changepassword(request):
    if request.method=="POST":
        ccount=tbl_user.objects.filter(id=request.session["uid"],user_password=request.POST.get('txtcurpass')).count()
        if ccount>0:
            if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                userdata=tbl_user.objects.get(id=request.session["uid"],user_password=request.POST.get('txtcurpass'))
                userdata.user_password=request.POST.get('txtnewpass')
                userdata.save()
                return render(request,"User/ChangePassword.html",{'msg':"Password Updated"})
            else:
                return render(request,"User/ChangePassword.html",{'msg1':"Error in confirm Password"})
        else:
            return render(request,"User/ChangePassword.html",{'msg1':"Error in current password"})
    else:
        return render(request,"User/ChangePassword.html")

def POSTComplaint(request):
    data=tbl_complaint.objects.filter(user=request.session["uid"])
    userID=tbl_user.objects.get(id=request.session["uid"])
    if request.method=="POST":
        title=request.POST.get('txttitle')
        details=request.POST.get('txtcomplaint')
        tbl_complaint.objects.create(complaint_title=title,complaint_details=details,user=userID)
        return redirect("User:POSTComplaint")
    else:
        return render(request,"User/POSTComplaint.html",{"data":data})
    
def delComplaint(request,did):
    tbl_complaint.objects.get(id=did).delete()
    return redirect("User:POSTComplaint")


def UserFeedback(request):
    data=tbl_feedback.objects.filter(user=request.session["uid"])
    userID=tbl_user.objects.get(id=request.session["uid"])
    if request.method=="POST":
        subject=request.POST.get('txtsubject')
        details=request.POST.get('txtfeedback')
        tbl_feedback.objects.create(feedback_subject=subject,feedback_details=details,user=userID)
        return redirect("User:UserFeedback")
    else:
        return render(request,"User/UserFeedback.html",{"data":data})
   

def delFeedback(request,did):
    tbl_feedback.objects.get(id=did).delete()
    return redirect("User:UserFeedback")

def ViewWork(request):
    art = tbl_arttype.objects.all()
    ar=[1,2,3,4,5]
    parry=[]
    avg=0
    work=tbl_artistwork.objects.all()
    for i in work:
        tot=0
        ratecount=tbl_rating.objects.filter(work=i.id).count()
        if ratecount>0:
            ratedata=tbl_rating.objects.filter(work=i.id)
            for j in ratedata:
                tot=tot+j.rating_data
                avg=tot//ratecount
                #print(avg)
            parry.append(avg)
        else:
            parry.append(0)
        # print(parry)
    datas=zip(work,parry)
    if request.method == "POST":
        work=tbl_artistwork.objects.filter(arttype=request.POST.get("sel_arttype"))
        for i in work:
            tot=0
            ratecount=tbl_rating.objects.filter(work=i.id).count()
            if ratecount>0:
                ratedata=tbl_rating.objects.filter(work=i.id)
                for j in ratedata:
                    tot=tot+j.rating_data
                    avg=tot//ratecount
                    #print(avg)
                parry.append(avg)
            else:
                parry.append(0)
            # print(parry)
        datas=zip(work,parry)
        return render(request,"User/View_work.html",{"data":datas,"ar":ar,"art":art})
    else:
        return render(request,"User/View_work.html",{"data":datas,"ar":ar,"art":art})    

def viewprogram(request):
    pgm = tbl_programtype.objects.all()
    data = tbl_artistprogram.objects.all()
    if request.method == "POST":
        data = tbl_artistprogram.objects.filter(programtype=request.POST.get("sel_program"))
        return render(request,"User/View_Program.html",{"data":data,"pgm":pgm})
    else:
        return render(request,"User/View_Program.html",{"data":data,"pgm":pgm})

def viewprogramvideo(request,id):
    data = tbl_artistprogram_video.objects.filter(program=id)
    return render(request,"User/View_program_video.html",{"data":data})

def bookprogram(request,id):
    if request.method == "POST":
        tbl_programbooking.objects.create(user=tbl_user.objects.get(id=request.session["uid"]),
                                        program=tbl_artistprogram.objects.get(id=id),
                                        booking_fordate=request.POST.get("txt_fdate"),
                                        booking_description=request.POST.get("txt_bdetails"))
        return render(request,"User/Book_programs.html",{"msg":"Program Booked"})
    else:
        return render(request,"User/Book_programs.html")

def buynow(request,id):
    work = tbl_artistwork.objects.get(id=id)
    total = work.work_price
    if request.method == "POST":
        tbl_booking.objects.create(user=tbl_user.objects.get(id=request.session["uid"]),
                                    work=tbl_artistwork.objects.get(id=id))
        return redirect("User:loader")
    else:
        return render(request,"User/Payment.html",{"total":total})

def program_payment(request,id):
    pg = tbl_programbooking.objects.get(id=id)
    total = (int(pg.program.program_price ) * 10) / 100
    if request.method == "POST":
        pg.booking_status = 3
        pg.save()
        return redirect("User:loader")
    else:
        return render(request,"User/Payment.html",{"total":total})

def loader(request):
    return render(request,"User/Loader.html")

def paymentsuc(request):
    return render(request,"User/Payment_suc.html")

def viewbooking(request):
    bk = tbl_booking.objects.filter(user=request.session["uid"])
    book = tbl_new_booking.objects.filter(user=request.session["uid"],booking_status__gt=0)
    program = tbl_programbooking.objects.filter(user=request.session["uid"])
    return render(request,"User/View_booking.html",{"data":bk,"book":book,"program":program})

def viewproduct(request,id):
    cart = tbl_cart.objects.filter(booking=id)
    return render(request,"User/View_product.html",{"data":cart})

def cancel_booking(request,id):
    data = tbl_programbooking.objects.get(id=id)
    data.booking_status = 4
    data.save()
    return redirect("User:viewbooking")

def rating(request,mid):
    parray=[1,2,3,4,5]
    mid=mid
    wdata=tbl_booking.objects.get(id=mid)
    
    counts=0
    counts=stardata=tbl_rating.objects.filter(work=wdata.work_id).count()
    if counts>0:
        res=0
        stardata=tbl_rating.objects.filter(work=wdata.work_id).order_by('-datetime')
        for i in stardata:
            res=res+i.rating_data
        avg=res//counts
        return render(request,"User/Rating.html",{'mid':mid,'data':stardata,'ar':parray,'avg':avg,'count':counts})
    else:
         return render(request,"User/Rating.html",{'mid':mid})

def ajaxstar(request):
    parray=[1,2,3,4,5]
    rating_data=request.GET.get('rating_data')
    user_name=request.GET.get('user_name')
    user_review=request.GET.get('user_review')
    workid=request.GET.get('workid')
    wdata=tbl_booking.objects.get(id=workid)
    tbl_rating.objects.create(user_name=user_name,user_review=user_review,rating_data=rating_data,work=tbl_artistwork.objects.get(id=wdata.work_id))
    stardata=tbl_rating.objects.filter(work=wdata.work_id).order_by('-datetime')
    return render(request,"User/AjaxRating.html",{'data':stardata,'ar':parray})

def starrating(request):
    r_len = 0
    five = four = three = two = one = 0
    cdata = tbl_booking.objects.get(id=request.GET.get("pdt"))
    rate = tbl_rating.objects.filter(work=cdata.work_id)
    for i in rate:
        if int(i.rating_data) == 5:
            five = five + 1
        elif int(i.rating_data) == 4:
            four = four + 1
        elif int(i.rating_data) == 3:
            three = three + 1
        elif int(i.rating_data) == 2:
            two = two + 1
        elif int(i.rating_data) == 1:
            one = one + 1
        else:
            five = four = three = two = one = 0
        r_len = r_len + int(i.rating_data)
    rlen = r_len // 5
    result = {"five":five,"four":four,"three":three,"two":two,"one":one,"total_review":rlen}
    return JsonResponse(result)

def newrating(request,mid):
    parray=[1,2,3,4,5]
    mid=mid
    wdata=tbl_cart.objects.get(id=mid)
    
    counts=0
    counts=stardata=tbl_rating.objects.filter(work=wdata.product_id).count()
    if counts>0:
        res=0
        stardata=tbl_rating.objects.filter(work=wdata.product_id).order_by('-datetime')
        for i in stardata:
            res=res+i.rating_data
        avg=res//counts
        return render(request,"User/New_Rating.html",{'mid':mid,'data':stardata,'ar':parray,'avg':avg,'count':counts})
    else:
         return render(request,"User/New_Rating.html",{'mid':mid})

def newajaxstar(request):
    parray=[1,2,3,4,5]
    rating_data=request.GET.get('rating_data')
    user_name=request.GET.get('user_name')
    user_review=request.GET.get('user_review')
    workid=request.GET.get('workid')
    wdata=tbl_cart.objects.get(id=workid)
    tbl_rating.objects.create(user_name=user_name,user_review=user_review,rating_data=rating_data,work=tbl_artistwork.objects.get(id=wdata.product_id))
    stardata=tbl_rating.objects.filter(work=wdata.product_id).order_by('-datetime')
    return render(request,"User/AjaxRating.html",{'data':stardata,'ar':parray})

def newstarrating(request):
    r_len = 0
    five = four = three = two = one = 0
    cdata = tbl_cart.objects.get(id=request.GET.get("pdt"))
    rate = tbl_rating.objects.filter(work=cdata.product_id)
    for i in rate:
        if int(i.rating_data) == 5:
            five = five + 1
        elif int(i.rating_data) == 4:
            four = four + 1
        elif int(i.rating_data) == 3:
            three = three + 1
        elif int(i.rating_data) == 2:
            two = two + 1
        elif int(i.rating_data) == 1:
            one = one + 1
        else:
            five = four = three = two = one = 0
        r_len = r_len + int(i.rating_data)
    rlen = r_len // 5
    result = {"five":five,"four":four,"three":three,"two":two,"one":one,"total_review":rlen}
    return JsonResponse(result)

def Addcart(request,pid):
    productdata=tbl_artistwork.objects.get(id=pid)
    custdata=tbl_user.objects.get(id=request.session["uid"])
    bookingcount=tbl_new_booking.objects.filter(user=custdata,booking_status=0).count()
    if bookingcount>0:
        bookingdata=tbl_new_booking.objects.get(user=custdata,booking_status=0)
        cartcount=tbl_cart.objects.filter(booking=bookingdata,product=productdata).count()
        if cartcount>0:
            msg="Already added"
            return render(request,"User/View_work.html",{'msg':msg})
        else:
            tbl_cart.objects.create(booking=bookingdata,product=productdata,cart_qty=1)
            msg="Added To cart"
            return render(request,"User/View_work.html",{'msg':msg})
    else:
        tbl_new_booking.objects.create(user=custdata)
        bookingcount=tbl_new_booking.objects.filter(booking_status=0,user=custdata).count()
        if bookingcount>0:
            bookingdata=tbl_new_booking.objects.get(user=custdata,booking_status=0)
            cartcount=tbl_cart.objects.filter(booking=bookingdata,product=productdata).count()
            if cartcount>0:
                msg="Already added"
                return render(request,"User/View_work.html",{'msg':msg})
            else:
                tbl_cart.objects.create(booking=bookingdata,product=productdata,cart_qty=1)
                msg="Added To cart"
                return render(request,"User/View_work.html",{'msg':msg})

def Mycart(request):
    if request.method=="POST":
        bookingdata=tbl_new_booking.objects.get(id=request.session["bookingid"])
        # cart = tbl_cart.objects.filter(booking=bookingdata)
        # for i in cart:
        #     i.cart_status = 1
        #     i.save()
        bookingdata.booking_totalamount=request.POST.get("carttotalamt")
        bookingdata.booking_status=1
        bookingdata.save()
        return redirect("User:payment")
    else:
        bookcount = tbl_new_booking.objects.filter(user=request.session["uid"],booking_status=0).count()
        if bookcount > 0:
            book = tbl_new_booking.objects.get(user=request.session["uid"],booking_status=0)
            request.session["bookingid"] = book.id
            cart = tbl_cart.objects.filter(booking=book)
            return render(request,"User/MyCart.html",{'cartdata':cart})
        else:
            return render(request,"User/MyCart.html")
        

def DelCart(request,did):
   tbl_cart.objects.get(id=did).delete()
   return redirect("User:mycart")

def CartQty(request):
   qty=request.GET.get('QTY')
   cartid=request.GET.get('ALT')
   cartdata=tbl_cart.objects.get(id=cartid)
   cartdata.cart_qty=qty
   cartdata.save()
   return redirect("User:mycart")   

def payment(request):
    bk = tbl_new_booking.objects.get(id=request.session["bookingid"])
    if request.method == "POST":
        cart = tbl_cart.objects.filter(booking=request.session["bookingid"])
        for i in cart:
            product = tbl_artistwork.objects.get(id=i.product.id)
            qty = i.cart_qty
            stock = product.work_stock
            product.work_stock = int(stock) - int(qty)
            product.save()
        bk.booking_status = 2
        bk.save()
        return redirect("User:loader")
    else:
        return render(request,"User/Payment.html",{"book":bk})

def viewevent(request):
    data = tbl_event.objects.all()
    return render(request,"User/View_Events.html",{"data":data})