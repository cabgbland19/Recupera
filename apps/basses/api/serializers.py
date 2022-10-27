from rest_framework import serializers
from apps.basses.models import *


class recoverBaseSerializers(serializers.ModelSerializer):
    class Meta:
        model=recoverBase
        fields='__all__'

class finalBase(serializers.ModelSerializer):
    class Meta:
        model=finalBase
        fields='__all__'

class NamesSerializers(serializers.ModelSerializer):
    class Meta:
        model=Names
        fields='__all__'

class RolsSerializers(serializers.ModelSerializer):
    class Meta:
        model=Rols
        fields='__all__'

class CampaignSerializers(serializers.ModelSerializer):
    class Meta:
        model=Campaign
        fields='__all__'