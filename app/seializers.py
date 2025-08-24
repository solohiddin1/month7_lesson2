from rest_framework import serializers
from .models import *


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        # fields = "__all__"
        fields = ["id","name"]

class MovieSerializer(serializers.ModelSerializer):
    actor = ActorSerializer(many=True,read_only=True)
    actor_id = serializers.PrimaryKeyRelatedField(
        many=True,queryset=Actor.objects.all(),write_only=True,source='actor'
    )

    class Meta:
        model = Movie
        fields = "__all__"