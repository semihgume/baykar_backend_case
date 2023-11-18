from rest_framework import serializers
from .models import CustomUser, IHA, RentedIHA


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class IHASerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = IHA
        fields = ['id', 'brand', 'model', 'category', 'weight', 'hourly_wage']
        datatables_always_serialize = ('id')


class RentedIHASerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = RentedIHA
        fields = ['id', 'user', 'iha', 'user_info', 'iha_info', 'start_date', 'end_date', 'wage']
        datatables_always_serialize = ('id')