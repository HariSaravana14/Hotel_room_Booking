from datetime import timezone
from django.db import models
from django.utils import timezone

# Model for ServiceNonPaid
class ServiceNonPaid(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    timings = models.CharField(max_length=50)

    def _str_(self):
        return self.name

# Model for ServicePaid
class ServicePaid(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)

    def _str_(self):
        return self.name

# Model for Customer
class Customer(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phoneno = models.CharField(max_length=15)
    houseno = models.CharField(max_length=50)
    apartment = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)

    def _str_(self):
        return f'{self.firstname} {self.lastname}'

# Model for Login
class Login(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def _str_(self):
        return self.email

# Model for Room
class Room(models.Model):
    roomid = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100)
    allotment_status = models.CharField(max_length=50, default="Available")
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def _str_(self):
        return f'Room {self.roomid} - {self.type}'

# Model for Allotment
class Allotment(models.Model):
    booked_from = models.DateField()
    booked_till = models.DateField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    bookingid = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def _str_(self):
        return f'Room {self.room.roomid} - {self.booked_from} to {self.booked_till}'

# Model for Complaints
class Complaint(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    description = models.TextField()
    complain_title = models.CharField(max_length=255)

    def _str_(self):
        return self.complain_title


class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    checkin = models.DateTimeField(default=timezone.now)
    checkout = models.DateTimeField()
    num_of_adults = models.IntegerField()
    num_of_children = models.IntegerField()
    num_of_rooms = models.IntegerField()

    def _str_(self):
        return f'Booking by {self.customer.firstname} for Room {self.room.roomid}'
    
class Staff(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    shift = models.CharField(max_length=50)
    timings = models.CharField(max_length=50)

    def _str_(self):
        return f'{self.name} ({self.designation})'