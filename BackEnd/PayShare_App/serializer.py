from rest_framework import serializers

from .models import UserApp


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserApp
        fields = ['code','name','surname', 'password', 'email', 'fiscalCode', 'birthDate', 'birthPlace', 'residence',
                  'smartContractList', 'extensions']