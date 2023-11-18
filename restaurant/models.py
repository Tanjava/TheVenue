from django.db import models
from django.contrib.auth.models import User

# Create your models here.

GUESTS = (
    (2, '2 person'),
    (3, '3 person'),
    (4, '4 person'),
    (5, '5 person'),
    (6, '6 person'),
)

TIMESLOTS = (
    ('17:00', '17:00'),
    ('17:30', '17:30'),
    ('18:00', '18:00'),
    ('18:30', '18:30'),
    ('19:00', '19:00'),
    ('19:30', '19:30'),
    ('20:00', '20:00'),
    ('20:30', '20:30'),
)

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_booking")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    date = models.DateField()
    time = models.CharField(max_length=5, choices=TIMESLOTS, default='17:00')
    number_of_guests = models.IntegerField(choices=GUESTS, default=2)

    class Meta:
        ordering = ["date", "time"]

    def __str__(self):
        return f"{self.name}'s booking on {self.date} at {self.time}"
