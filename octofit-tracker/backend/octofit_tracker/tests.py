from django.test import TestCase
from .models import Team, OctoFitUser, Activity, Workout, Leaderboard


class TeamModelTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team', description='A test team')
        self.assertEqual(team.name, 'Test Team')


class OctoFitUserModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')

    def test_user_creation(self):
        user = OctoFitUser.objects.create(
            email='test@example.com',
            name='Test User',
            team=self.team
        )
        self.assertEqual(user.name, 'Test User')


class ActivityModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = OctoFitUser.objects.create(
            email='test@example.com',
            name='Test User',
            team=self.team
        )

    def test_activity_creation(self):
        activity = Activity.objects.create(
            user=self.user,
            activity_type='running',
            duration_minutes=30
        )
        self.assertEqual(activity.activity_type, 'running')


class WorkoutModelTest(TestCase):
    def test_workout_creation(self):
        workout = Workout.objects.create(
            name='Test Workout',
            description='A test workout',
            difficulty='beginner',
            duration_minutes=30
        )
        self.assertEqual(workout.name, 'Test Workout')


class LeaderboardModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = OctoFitUser.objects.create(
            email='test@example.com',
            name='Test User',
            team=self.team
        )

    def test_leaderboard_creation(self):
        leaderboard = Leaderboard.objects.create(
            user=self.user,
            team=self.team,
            total_calories_burned=100
        )
        self.assertEqual(leaderboard.total_calories_burned, 100)