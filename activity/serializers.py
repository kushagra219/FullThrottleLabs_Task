from rest_framework import serializers
from .models import *
import six


class ActivityPeriodSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ActivityPeriod
        fields = ('start_time', 'end_time')


class UserSerializer(serializers.ModelSerializer):
    activity_periods = ActivityPeriodSerializer(many=True)
    tz = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'real_name', 'tz', 'activity_periods')
        depth = 1

    def get_tz(self, obj):
        return six.text_type(obj.tz)