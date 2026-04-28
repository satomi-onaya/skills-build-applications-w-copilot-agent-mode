from django.contrib import admin
from .models import Team, OctoFitUser, Activity, Workout, Leaderboard


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_at']
    search_fields = ['name']


@admin.register(OctoFitUser)
class OctoFitUserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'team', 'age', 'fitness_goal']
    search_fields = ['name', 'email']
    list_filter = ['team']


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['user', 'activity_type', 'duration_minutes', 'calories_burned', 'date']
    search_fields = ['user__name', 'activity_type']
    list_filter = ['activity_type', 'intensity']


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['name', 'difficulty', 'duration_minutes', 'target_muscle_groups']
    search_fields = ['name']
    list_filter = ['difficulty']


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ['user', 'team', 'total_calories_burned', 'total_activities', 'rank']
    search_fields = ['user__name']
    list_filter = ['team']