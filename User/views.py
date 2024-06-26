from django.shortcuts import render,redirect
from Guest.models import *
from User.models import *
from Artist.models import *
from django.http import JsonResponse 
from django.conf import settings
from django.core.mail import send_mail
from datetime import datetime
# Create your views here.

def homepage(request):
    user = tbl_user.objects.get(id=request.session["uid"])
    return render(request,"User/HomePage.html",{"user":user})

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
        prodata.user_address=request.POST.get('txttext')
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
        details=request.POST.get('txtfeedback')
        tbl_feedback.objects.create(feedback=details,user=userID)
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
    artist = tbl_artist.objects.all()
    if request.method == "POST":
        if ((request.POST.get("sel_program")!="") and (request.POST.get("sel_artist")!="")):
            data = tbl_artistprogram.objects.filter(programtype=request.POST.get("sel_program"),artist=request.POST.get("sel_artist"))
            return render(request,"User/View_Program.html",{"data":data,"pgm":pgm,"artist":artist})
        elif request.POST.get("sel_program")!="":
            data = tbl_artistprogram.objects.filter(programtype=request.POST.get("sel_program"))
            return render(request,"User/View_Program.html",{"data":data,"pgm":pgm,"artist":artist})
        elif request.POST.get("sel_artist")!="":
            data = tbl_artistprogram.objects.filter(artist=request.POST.get("sel_artist"))
            return render(request,"User/View_Program.html",{"data":data,"pgm":pgm,"artist":artist})
        else:
            return render(request,"User/View_Program.html",{"data":data,"pgm":pgm,"artist":artist})
    else:
        return render(request,"User/View_Program.html",{"data":data,"pgm":pgm,"artist":artist})

def viewprogramvideo(request,id):
    data = tbl_artistprogram_video.objects.filter(program=id)
    return render(request,"User/View_program_video.html",{"data":data})

def bookprogram(request,id):
    if request.method == "POST":
        user = tbl_user.objects.get(id=request.session["uid"])
        user_email = user.user_email
        pgm = tbl_artistprogram.objects.get(id=id)
        artist_email = pgm.artist.artist_email
        tbl_programbooking.objects.create(user=tbl_user.objects.get(id=request.session["uid"]),
                                        program=tbl_artistprogram.objects.get(id=id),
                                        booking_fordate=request.POST.get("txt_fdate"),
                                        booking_description=request.POST.get("txt_bdetails"))
        send_mail(
            'Respected Sir/Madam ',#subject
            "\rYour Booking Is Sucessfully Completed." ,#body
            settings.EMAIL_HOST_USER,
            [user_email],
        )
        send_mail(
            'Respected Sir/Madam ',#subject
            "\rYou Have A Booking." ,#body
            settings.EMAIL_HOST_USER,
            [artist_email],
        )
        return render(request,"User/Book_programs.html",{"msg":"Program Booked"})
    else:
        return render(request,"User/Book_programs.html")

def buynow(request,id):
    work = tbl_artistwork.objects.get(id=id)
    total = work.work_price
    stock = work.work_stock
    if request.method == "POST":
        balance = int(stock) - 1
        work.work_stock = balance
        work.save()
        user = tbl_user.objects.get(id=request.session["uid"])
        user_email = user.user_email
        pgm = tbl_artistwork.objects.get(id=id)
        artist_email = pgm.artist.artist_email
        tbl_booking.objects.create(user=tbl_user.objects.get(id=request.session["uid"]),
                                    work=tbl_artistwork.objects.get(id=id))
        send_mail(
            'Respected Sir/Madam ',#subject
            "\rYour Booking Is Sucessfully Completed." ,#body
            settings.EMAIL_HOST_USER,
            [user_email],
        )
        send_mail(
            'Respected Sir/Madam ',#subject
            "\rYou Have A Booking." ,#body
            settings.EMAIL_HOST_USER,
            [artist_email],
        )
        return redirect("User:loader")
    else:
        return render(request,"User/Payment.html",{"total":total})

def program_payment(request,id):
    pg = tbl_programbooking.objects.get(id=id)
    total = (int(pg.program.program_price ) * 10) / 100
    if request.method == "POST":
        user = tbl_user.objects.get(id=request.session["uid"])
        user_email = user.user_email
        pgm = tbl_programbooking.objects.get(id=id)
        artist_email = pgm.program.artist.artist_email
        pg.booking_status = 3
        pg.save()
        send_mail(
            'Respected Sir/Madam ',#subject
            "\rYour Payment Is Sucessfully Completed." ,#body
            settings.EMAIL_HOST_USER,
            [user_email],
        )
        send_mail(
            'Respected Sir/Madam ',#subject
            "\rPayment is Completed." ,#body
            settings.EMAIL_HOST_USER,
            [artist_email],
        )
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
    return render(request,"User/View_booking.html",{"data":bk,"book":book})

def viewproduct(request,id):
    cart = tbl_cart.objects.filter(booking=id)
    return render(request,"User/View_product.html",{"data":cart})

def cancel_booking(request,id):
    user = tbl_user.objects.get(id=request.session["uid"])
    user_email = user.user_email
    pgm = tbl_programbooking.objects.get(id=id)
    artist_email = pgm.artist.artist_email
    data = tbl_programbooking.objects.get(id=id)
    data.booking_status = 4
    data.save()
    send_mail(
        'Respected Sir/Madam ',#subject
        "\rYour Booking is Cancelled Completed." ,#body
        settings.EMAIL_HOST_USER,
        [user_email],
    )
    send_mail(
        'Respected Sir/Madam ',#subject
        "\rBooking is Cancelled." ,#body
        settings.EMAIL_HOST_USER,
        [artist_email],
    )
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
        cartdata = tbl_cart.objects.filter(booking=request.session["bookingid"]).last()
        user = tbl_user.objects.get(id=request.session["uid"])
        user_email = user.user_email
        cdata = tbl_cart.objects.filter(booking=request.session["bookingid"]).last()
        artist_email = cartdata.product.artist.artist_email
        for i in cart:
            product = tbl_artistwork.objects.get(id=i.product.id)
            qty = i.cart_qty
            stock = product.work_stock
            product.work_stock = int(stock) - int(qty)
            product.save()
        bk.booking_status = 2
        bk.save()
        send_mail(
            'Respected Sir/Madam ',#subject
            "\rYour Payment Is Sucessfully Completed." ,#body
            settings.EMAIL_HOST_USER,
            [user_email],
        )
        send_mail(
            'Respected Sir/Madam ',#subject
            "\rPayment is Completed." ,#body
            settings.EMAIL_HOST_USER,
            [artist_email],
        )
        return redirect("User:loader")
    else:
        return render(request,"User/Payment.html",{"book":bk})

def viewevent(request):
    flage = 0
    data = tbl_event.objects.all()
    for i in data:
        count = tbl_tickets.objects.filter(booking__event=i.id,status=0).count()
        if count >= int(i.event_seat):
            i.flage = flage + 1
        else:
            i.flage = 0
    return render(request,"User/View_Events.html",{"data":data})

def viewevent_seat(request,id):
    event = tbl_event.objects.get(id=id)
    event_seat = range(1,int(event.event_seat)+1)
    arr = []
    j=1
    for i in event_seat:
        if i/10 == j:
            arr.append(i) 
            j=j+1
    ticketbook = tbl_tickets.objects.filter(booking__booking_status=1,status=0,booking__event=id)
    # print(arr)
    if request.method == "POST":
        ticket_count = tbl_ticket_booking.objects.filter(user=request.session["uid"],booking_status=0).count()
        seat_count = len(request.POST.getlist("txtseat[]"))
        if seat_count > 0:
            seat = request.POST.getlist("txtseat[]")
            event_amt = event.event_amount
            total = int(event_amt) * seat_count
            # print(seat)
            if ticket_count > 0:
                bk = tbl_ticket_booking.objects.get(user=request.session["uid"],booking_status=0)
                for s in seat:
                    tic_count = tbl_tickets.objects.filter(booking=bk.id,seat_no=s).count()
                    if tic_count > 0:
                        return render(request,"User/View_Event_Seats.html",{"msg1":"You Already Booked Seat "+s,"id":id})
                    else:
                        tbl_tickets.objects.create(seat_no=s,booking=tbl_ticket_booking.objects.get(id=bk.id))
                bk_amt = bk.booking_totalamount
                tot = int(bk_amt) + total
                bk.booking_totalamount = tot
                bk.save()
                return render(request,"User/View_Event_Seats.html",{"msg":"Booked","id":bk.id})
            else:
                bkid = tbl_ticket_booking.objects.create(user=tbl_user.objects.get(id=request.session["uid"]),booking_totalamount=total,booking_time=datetime.now(),event=tbl_event.objects.get(id=id))
                for s in seat:
                    tbl_tickets.objects.create(seat_no=s,booking=tbl_ticket_booking.objects.get(id=bkid.id))
                return render(request,"User/View_Event_Seats.html",{"msg":"Booked","id":bkid.id})
        else:
            return render(request,"User/View_Event_Seats.html",{"msg1":"No Seat Booked","id":id})   
    else:
        return render(request,"User/View_Event_Seats.html",{"event":event,"event_seat":event_seat,"gap":arr,"book":ticketbook})

def ticketbooking(request):
    tbook = tbl_ticket_booking.objects.filter(user=request.session["uid"])
    return render(request,"User/Ticket_booking.html",{"data":tbook})

def tickets(request,id):
    tic = tbl_tickets.objects.filter(booking=id,status=0)
    return render(request,"User/Tickets.html",{"data":tic})

def bookchecking(request):
    # print("hai")
    min = request.GET.get("min")
    # print(min)
    tbook = tbl_ticket_booking.objects.filter(booking_status=0)
    for  t in tbook:
        time = t.booking_time.minute
        diff = int(min) - time
        # print(diff)
        if diff > 5:
            tickets = tbl_tickets.objects.filter(booking=t.id)
            for ti in tickets:
                tbl_tickets.objects.get(id=ti.id).delete()
            tbl_ticket_booking.objects.get(id=t.id).delete()
    # print(datetime.now().minute)
    return JsonResponse({"msg":"hai Hello"})

def ticketpayment(request,id):
    book = tbl_ticket_booking.objects.get(id=id)
    total = book.booking_totalamount
    if request.method == "POST":
        book.booking_status=1
        book.save()
        return redirect("User:loader")
    else:
        return render(request,"User/Payment.html",{"total":total})

def cancelbooking(request):
    bk = tbl_tickets.objects.get(id=request.GET.get("tid"))
    ticket = tbl_tickets.objects.filter(booking=bk.booking.id,status=0).count()
    if ticket > 1:
        bk.status = 1
        bk.save()
        return JsonResponse({"msg":"Ticket Cancelled.."})
    else:
        bk.status=1
        bk.save()
        book = tbl_ticket_booking.objects.get(id=bk.booking.id)
        book.booking_status=2
        book.save()
        return JsonResponse({"msg1":"Ticket Cancelled.."})
    
def programbooking(request):
    program = tbl_programbooking.objects.filter(user=request.session["uid"])
    return render(request,"User/View_Program_Booking.html",{"program":program})