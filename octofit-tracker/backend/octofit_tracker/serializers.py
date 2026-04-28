from rest_framework import serializers
from .models import Team, OctoFitUser, Activity, Workout, Leaderboard


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class OctoFitUserSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)
    team_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = OctoFitUser
        fields = '__all__'


class ActivitySerializer(serializers.ModelSerializer):
    user = OctoFitUserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Activity
        fields = '__all__'


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = '__all__'


class LeaderboardSerializer(serializers.ModelSerializer):
    user = OctoFitUserSerializer(read_only=True)
    team = TeamSerializer(read_only=True)

    class Meta:
        model = Leaderboard
        fields = '__all__'