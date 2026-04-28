from django.core.management.base import BaseCommand
from django.utils import timezone
from django.db import models
from octofit_tracker.models import Team, OctoFitUser, Activity, Workout, Leaderboard


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        self.stdout.write(self.style.WARNING('Clearing existing data...'))
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        OctoFitUser.objects.all().delete()
        Workout.objects.all().delete()
        Team.objects.all().delete()

        # Create teams
        self.stdout.write(self.style.SUCCESS('Creating teams...'))
        team_marvel = Team.objects.create(
            name='Team Marvel',
            description='Marvel superheroes pushing their fitness limits'
        )
        team_dc = Team.objects.create(
            name='Team DC',
            description='DC superheroes on their fitness journey'
        )

        # Create superhero users
        self.stdout.write(self.style.SUCCESS('Creating superheroes...'))
        
        # Marvel Team
        iron_man = OctoFitUser.objects.create(
            email='tony.stark@marvel.com',
            name='Iron Man',
            team=team_marvel,
            age=48,
            fitness_goal='Maintain peak physical condition for suit operations'
        )
        captain_america = OctoFitUser.objects.create(
            email='steve.rogers@marvel.com',
            name='Captain America',
            team=team_marvel,
            age=100,
            fitness_goal='Super soldier fitness maintenance'
        )
        spider_man = OctoFitUser.objects.create(
            email='peter.parker@marvel.com',
            name='Spider-Man',
            team=team_marvel,
            age=18,
            fitness_goal='Enhance agility and strength'
        )
        thor = OctoFitUser.objects.create(
            email='thor.odinson@marvel.com',
            name='Thor',
            team=team_marvel,
            age=1500,
            fitness_goal='Maintain Asgardian strength'
        )

        # DC Team
        batman = OctoFitUser.objects.create(
            email='bruce.wayne@dc.com',
            name='Batman',
            team=team_dc,
            age=35,
            fitness_goal='Peak detective and combat readiness'
        )
        superman = OctoFitUser.objects.create(
            email='clark.kent@dc.com',
            name='Superman',
            team=team_dc,
            age=35,
            fitness_goal='Maintain Kryptonian physiology'
        )
        wonder_woman = OctoFitUser.objects.create(
            email='diana.prince@dc.com',
            name='Wonder Woman',
            team=team_dc,
            age=2500,
            fitness_goal='Amazonian warrior fitness'
        )
        flash = OctoFitUser.objects.create(
            email='barry.allen@dc.com',
            name='The Flash',
            team=team_dc,
            age=28,
            fitness_goal='Speed force conditioning'
        )

        superheroes = [iron_man, captain_america, spider_man, thor, batman, superman, wonder_woman, flash]

        # Create sample workouts
        self.stdout.write(self.style.SUCCESS('Creating workouts...'))
        
        strength_workout = Workout.objects.create(
            name='Superhero Strength Training',
            description='Full body strength training for superheroes',
            difficulty='advanced',
            duration_minutes=90,
            target_muscle_groups='Chest, Back, Shoulders, Legs',
            exercises='Bench Press, Deadlifts, Squats, Pull-ups, Dumbbell Rows'
        )
        
        cardio_workout = Workout.objects.create(
            name='Speed and Endurance',
            description='High-intensity cardio workout',
            difficulty='intermediate',
            duration_minutes=60,
            target_muscle_groups='Full Body',
            exercises='Running, HIIT, Burpees, Mountain Climbers, Jump Rope'
        )
        
        agility_workout = Workout.objects.create(
            name='Agility Drills',
            description='Improve speed and agility',
            difficulty='intermediate',
            duration_minutes=45,
            target_muscle_groups='Legs, Core',
            exercises='Ladder Drills, Cone Drills, Box Jumps, Lateral Movements'
        )

        # Create sample activities for each superhero
        self.stdout.write(self.style.SUCCESS('Creating activities...'))
        
        activities_data = [
            {'type': 'running', 'duration': 60, 'calories': 600, 'distance': 10, 'intensity': 'high'},
            {'type': 'cycling', 'duration': 90, 'calories': 750, 'distance': 35, 'intensity': 'high'},
            {'type': 'weightlifting', 'duration': 75, 'calories': 500, 'distance': None, 'intensity': 'high'},
            {'type': 'swimming', 'duration': 60, 'calories': 550, 'distance': 2, 'intensity': 'medium'},
            {'type': 'hiit', 'duration': 45, 'calories': 600, 'distance': None, 'intensity': 'high'},
            {'type': 'yoga', 'duration': 90, 'calories': 300, 'distance': None, 'intensity': 'low'},
        ]

        for superhero in superheroes:
            for i, activity_data in enumerate(activities_data):
                Activity.objects.create(
                    user=superhero,
                    activity_type=activity_data['type'],
                    duration_minutes=activity_data['duration'],
                    calories_burned=activity_data['calories'],
                    distance_km=activity_data['distance'],
                    intensity=activity_data['intensity'],
                    date=timezone.now(),
                    description=f'{superhero.name} performing {activity_data["type"]} training'
                )

        # Create leaderboard entries
        self.stdout.write(self.style.SUCCESS('Creating leaderboard entries...'))
        
        rank = 1
        for superhero in superheroes:
            total_calories = Activity.objects.filter(user=superhero).aggregate(
                total=models.Sum('calories_burned')
            )['total'] or 0
            total_activities = Activity.objects.filter(user=superhero).count()
            total_minutes = Activity.objects.filter(user=superhero).aggregate(
                total=models.Sum('duration_minutes')
            )['total'] or 0

            Leaderboard.objects.create(
                user=superhero,
                team=superhero.team,
                total_calories_burned=total_calories,
                total_activities=total_activities,
                total_workout_minutes=total_minutes,
                rank=rank
            )
            rank += 1

        self.stdout.write(self.style.SUCCESS(f'Successfully populated database with {len(superheroes)} superheroes and their activities!'))
