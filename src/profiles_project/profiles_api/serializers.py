from rest_framework import serializers
from . import models

class HelloSerializer(serializers.Serializer):
    '''
    Serializes a name field for testing our APIView.
    '''

    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    '''
    A serializer for our profile objects
    '''
    class Meta:
        model = models.UserProfiles
        fields = ('id','email','name','password')
        extra_kwargs = {'password':{'write_only':True}}

    def create(self,validated_data):
        '''
        Creates and return a new user
        '''
        user = models.UserProfiles(email=validated_data['email'],name=validated_data['name'])

        user.set_password(validated_data['password'])
        user.save()

        return user

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    '''
    A Serializer for profile feed items.
    '''
    class Meta:
        model = models.ProfileFeedItem
        fields = ('id','user_profile','status_text','created_on')
        extra_kwargs={'user_profile':{'read_only':True}}
