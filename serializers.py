from rest_framework import serializers
from .models import Users , Trains

class IrctcSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id' , 'userName' , 'password' , 'Email']


class IRCTCADMINList(serializers.ModelSerializer):
    class Meta:
        model = Trains
        fields = ['id' , 'Train_name' , 'From_Station' , 'To_station' , 'seat_Capacity' , 'Depatured_Time_And_Date' , 'Arrival_Time_And_Date']