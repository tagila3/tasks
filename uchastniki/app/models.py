from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateField()
    attendees = models.ManyToManyField('Attendee', through='EventAttendee')  # Используем through

    def __str__(self):
        return self.name

class Attendee(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class EventAttendee(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    attendee = models.ForeignKey(Attendee, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('event', 'attendee')

    def __str__(self):
        return f"{self.attendee.name} Зарегестрировался на {self.event.name} {self.registration_date}"