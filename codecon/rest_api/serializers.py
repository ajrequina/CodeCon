from rest_framework import serializers
from django.contrib.auth import update_session_auth_hash
from rest_api.models import Account, User

class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=100)
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 
                  'email', 'password', 'confirm_password',)
    def create(self, validated_data):
        user = User(first_name=validated_data['first_name'], 
                    last_name=validated_data[''])
        return User.objects.create(validated_data)

    def to_internal_value(self, data):
       return super(UserSerializer,self).to_internal_value(data)

class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    confirm_password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Account
        fields = ('id', 'email', 'username', 'created_at', 'updated_at',
                  'first_name', 'last_name', 'password',
                  'confirm_password',)
        read_only_fields = ('created_at', 'updated_at',)

        def create(self, validated_data):
            
            return Account.objects.create_user(**validated_data)

        def update(self, instance, validated_data):
            instance.username = validated_data.get('username', instance.username)
            instance.save()

            password = validated_data.get('password', None)
            confirm_password = validated_data.get('confirm_password', None)
            if password and confirm_password and password == confirm_password:
                instance.set_password(password)
                instance.save()
            update_session_auth_hash(self.context.get('request'), instance)
            return instance

        def to_internal_value(self, data):
            username = data['username']
            raise serializers.ValidationError({'_error': 'object must provide pk!'})
            return username