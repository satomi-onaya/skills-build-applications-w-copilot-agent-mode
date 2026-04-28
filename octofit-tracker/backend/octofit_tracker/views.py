from rest_framework import viewsets
from .models import Team, OctoFitUser, Activity, Workout, Leaderboard
from .serializers import (
    TeamSerializer, OctoFitUserSerializer, ActivitySerializer,
    WorkoutSerializer, LeaderboardSerializer
)


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class OctoFitUserViewSet(viewsets.ModelViewSet):
    queryset = OctoFitUser.objects.all()
    serializer_class = OctoFitUserSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer


class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer