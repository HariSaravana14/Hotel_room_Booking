from django.shortcuts import render, redirect
from .models import Customer, Login, Booking, Room, Complaint, Staff, ServicePaid, ServiceNonPaid
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

def index(request):
    return render(request,'Home.html')

def contact(request):
    return render(request,"contact.html")

def about(request):
    return render(request,"about.html")

def user_dashboard(request):
    # Fetch user data to display in the dashboard
    customer = Customer.objects.get(id=request.session.get('customer_id'))
    data = {"name": customer.firstname}
    return render(request,'userpage.html', data)

def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user = Login.objects.get(email=email)
            if check_password(password, user.password):
                customer = Customer.objects.get(email=email)
                request.session['customer_id'] = customer.id
                return redirect('user_dashboard')
            else:
                return render(request, "error.html")
        except Login.DoesNotExist:
            return render(request, "error.html")
        
    return render(request, "login.html")

def register(request):
    if request.method == "POST":
        fn = request.POST.get('firstname')
        ln = request.POST.get('lastname')
        email = request.POST.get('email')
        password = make_password(request.POST.get('password'))
        mob = request.POST.get('phoneno')
        hno = request.POST.get('houseno')
        apart = request.POST.get('apartment')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pin = request.POST.get('pincode')

        # Create new customer and login entries
        customer = Customer.objects.create(
            firstname=fn, lastname=ln, email=email, phoneno=mob, 
            houseno=hno, apartment=apart, city=city, state=state, pincode=pin
        )
        Login.objects.create(email=email, password=password)

        return redirect('login')

    return render(request, "register.html")

def admin_login(request):
    if request.method == "POST":
        adminid = request.POST.get('adminid')
        admin_pass = request.POST.get('adminpass')
        # Assuming an admin model exists
        if adminid == "admin" and admin_pass == "admin123":
            return redirect('admin_dashboard')
        else:
            return render(request, "error.html")
    return render(request, "Admin_login.html")

def admin_dashboard(request):
    available_rooms = Room.objects.filter(allotment_status="Available").count()
    complaints = Complaint.objects.count()
    rdata = {"rooms": available_rooms, "complain": complaints}
    return render(request, "admin_dash.html", rdata)

def services(request):
    non_paid_services = ServiceNonPaid.objects.all()
    paid_services = ServicePaid.objects.all()
    data = {"non_paid_services": non_paid_services, "paid_services": paid_services}
    return render(request,'services.html', data)

def booking(request):
    if request.method == "POST":
        # Get the data and create the booking
        Booking.objects.create(
            first_name=request.POST['firstname'],
            last_name=request.POST['lastname'],
            mobile=request.POST['mobile'],
            num_of_adult=request.POST['num_of_adult'],
            num_of_child=request.POST['num_of_child'],
            type_of_room=request.POST['type'],
            auth_type=request.POST['verification_type'],
            auth_no=request.POST['verification_id'],
            num_of_rooms=request.POST['num_of_rooms'],
            booking_from=request.POST['checkin'],
            booking_till=request.POST['checkout'],
            customer_id=request.session.get('customer_id')
        )
        return redirect('user_dashboard')

    return render(request, "new_booking.html")

def complain_user(request):
    if request.method == "POST":
        Complaint.objects.create(
            roomno=request.POST['room'], 
            description=request.POST['description'], 
            complain_title=request.POST['title']
        )
    return render(request, "complain_send.html")

def staff(request):
    staff_members = Staff.objects.all()
    data = {"staff_members": staff_members}
    return render(request, "Staff.html", data)

def add_room(request):
    if request.method == "POST":
        Room.objects.create(
            roomid=request.POST['roomid'],
            type=request.POST['type'],
            price=request.POST['price']
        )
    return render(request, "Add_room.html")