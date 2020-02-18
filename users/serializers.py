from rest_framework import serializers
from .models import User
from allauth.account.adapter import get_adapter
from rest_auth.registration.serializers import RegisterSerializer
from profiles.serializers import ProfileSerializer
from rest_framework.authtoken.models import Token 


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ('email', 'username', 'password')

class CustomRegisterSerializer(RegisterSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password')

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        # user.save()
        adapter.save_user(request, user, self)
        return user


class TokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Token
        # fields = ('key', 'user', )
        fields = '__all__'


