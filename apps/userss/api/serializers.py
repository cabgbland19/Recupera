from rest_framework import serializers
from apps.userss.models import *



class UserstokenSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('document','username','name','cost_center','campaign','rol')
    
class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        exclude = ('password', )

    def create(self, validated_data):
        user=User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self, instance, validated_data):
        updated_user= super().update(instance, validated_data)
        updated_user.set_password(validated_data['password'])
        updated_user.save()
        return updated_user

class UsersCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

    def create(self, validated_data):
        user=User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class UpdateUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('document','username', 'name','cost_center','campaign','id_rol','rol','is_active')

    
        
class UpdateUserPswdSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('username', 'email', 'name', 'last_name','cost_center','campaign','password','id_rol','rol','is_active')


    def update(self, instance, validated_data):
        updated_user= super().update(instance, validated_data)
        updated_user.set_password(validated_data['password'])
        updated_user.save()
        return updated_user

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=RegistersUsers
        fields='__all__'