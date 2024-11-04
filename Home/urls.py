from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="Home Page"),
    path('about.html',views.about,name="about page"),
    path('Home.html',views.index,name="Home Page"),
    path('contact.html',views.contact,name="Contact Page"),
    path('login.html',views.login,name="Login Page"),
    path('register.html',views.register,name="Register Page"),
    path('Admin_login.html',views.admin,name="Admin Page"),
    path('services.html',views.services,name="Login Page"),
    path('Mybookings.html',views.booking_history,name="Login Page"),
    path('userpage.html',views.user_dashboard,name="Login Page"),
    path('rooms.html',views.rooms,name="Login Page"),
    path('Staff.html',views.staff,name="Login Page"),
    path('admin_dash.html',views.admin_dash,name="Login Page"),
    path('Complain_rec.html',views.complain_rec,name="complain"),
    path('complain_send.html',views.complain_user,name="user complain"),
    path('new_booking.html',views.booking,name="booking"),
    path('Add_room.html',views.addroom,name="add room"),
    path('Payment.html',views.payment,name="payment"),
    path('receipt.html',views.receipt,name="payment"),
    path('Getservice.html',views.order,name="order"),
    path('lastbooking.html',views.last,name="order"),
    path('admin_service.html',views.admin_service,name="order")


]