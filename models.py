from  django.db import models

class Users(models.Model):
    userName = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)

    def __str__(self):
        return self.Email + ' ' + self.userName
    

class Trains(models.Model):
    Train_name = models.CharField(max_length=100)
    From_Station = models.CharField(max_length=100)
    To_station = models.CharField(max_length=100)
    seat_Capacity = models.IntegerField()
    Depatured_Time_And_Date = models.DateTimeField()
    Arrival_Time_And_Date = models.DateTimeField()

    def __str__(self):
        return self.Train_name + " " + self.From_Station