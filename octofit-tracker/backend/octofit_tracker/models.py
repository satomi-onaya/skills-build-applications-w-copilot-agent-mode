from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    """Model for superhero teams"""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Teams"


class OctoFitUser(models.Model):
    """Model for OctoFit users"""
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    fitness_goal = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "OctoFit Users"


class Activity(models.Model):
    """Model for user activities"""
    ACTIVITY_TYPES = [
        ('running', 'Running'),
        ('cycling', 'Cycling'),
        ('swimming', 'Swimming'),
        ('weightlifting', 'Weightlifting'),
        ('yoga', 'Yoga'),
        ('hiit', 'HIIT'),
    ]

    user = models.ForeignKey(OctoFitUser, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=50, choices=ACTIVITY_TYPES)
    duration_minutes = models.IntegerField()
    calories_burned = models.IntegerField(null=True, blank=True)
    distance_km = models.FloatField(null=True, blank=True)
    intensity = models.CharField(max_length=50, default='moderate')
    date = models.DateTimeField()
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.name} - {self.activity_type} on {self.date}"

    class Meta:
        verbose_name_plural = "Activities"


class Workout(models.Model):
    """Model for workout plans"""
    name = models.CharField(max_length=255)
    description = models.TextField()
    difficulty = models.CharField(max_length=50, choices=[
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ])
    duration_minutes = models.IntegerField()
    target_muscle_groups = models.CharField(max_length=255)
    exercises = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Workouts"


class Leaderboard(models.Model):
    """Model for leaderboard rankings"""
    user = models.OneToOneField(OctoFitUser, on_delete=models.CASCADE, related_name='leaderboard')
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)
    total_calories_burned = models.IntegerField(default=0)
    total_activities = models.IntegerField(default=0)
    total_workout_minutes = models.IntegerField(default=0)
    rank = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.name} - Rank {self.rank}"

    class Meta:
        verbose_name_plural = "Leaderboards"
