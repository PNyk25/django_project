from rest_framework import serializers
from details_app.models import Userdetail

class UserdetailSerializer(serializers.ModelSerializer):
 
      
      class Meta:
        model=Userdetail
        fields="__all__"
        
    