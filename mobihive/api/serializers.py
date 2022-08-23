from rest_framework import serializers
from .models import  User

# class RegistrationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username','email','password')

#     def validate(self, args):
#         pass
#     def create(self, validated_data):
#         pass

# class UserSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = User
#         fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer):

    # email = serializers.EmailField(max_length=50, min_length=6)
    # username = serializers.CharField(max_length=50, min_length=6)
    # password = serializers.CharField(max_length=150, write_only=True)
    
    class Meta:
        model = User
        fields = '__all__'
        fields = ('username','email','password','profile_photo','address','city','phone_no')

    def validate(self, args):
        email = args.get('email', None)
        username = args.get('username', None)
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': ('email already exists')})
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username': ('username already exists')})

        return super().validate(args)
  

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)