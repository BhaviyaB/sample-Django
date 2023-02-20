from rest_framework import serializers
from .models import Students

class StudentSerializer(serializers.ModelSerializer):
    first_name=serializers.CharField(max_length=200)
    last_name=serializers.CharField(max_length=200)
    address=serializers.CharField(max_length=200)
    roll_number=serializers.IntegerField()
    mobile=serializers.CharField(max_length=10)

    class Meta:  
        model = Students  
        fields = ('__all__')  
