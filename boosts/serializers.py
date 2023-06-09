from django.db.models import Q
from django.db import IntegrityError
from rest_framework import serializers
from .models import Boost
from profiles.models import Profile


class BoostSerializer(serializers.ModelSerializer):
    profile_name = serializers.ReadOnlyField(source='profile.name')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        user = self.context['request'].user
        return user == obj.profile.owner

    class Meta:
        model = Boost
        fields = [
            'id', 'profile', 'created_at', 'recommendation', 'is_owner',
            'profile_name'
        ]

    def create(self, validated_data):
        """
        override create to handle record duplication error
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError(({
                'detail': 'You cannot boost the same recommendation twice!',
            }))
