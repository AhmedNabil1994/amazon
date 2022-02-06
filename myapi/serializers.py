from rest_framework import serializers
from pages.models import Myusers



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Myusers
        fields = '__all__'
        # ['userId', 'userName', 'userEmail', 'userPassword']

