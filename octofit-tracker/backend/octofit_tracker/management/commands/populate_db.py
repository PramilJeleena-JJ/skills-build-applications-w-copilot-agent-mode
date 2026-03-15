from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Create users
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel.name)
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel.name)
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc.name)
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc.name)

        # Create activities
        Activity.objects.create(user=tony, type='Running', duration=30, date='2026-03-15')
        Activity.objects.create(user=steve, type='Cycling', duration=45, date='2026-03-14')
        Activity.objects.create(user=bruce, type='Swimming', duration=25, date='2026-03-13')
        Activity.objects.create(user=clark, type='Walking', duration=60, date='2026-03-12')

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        # Create workouts
        Workout.objects.create(name='Pushups', description='Upper body workout', suggested_for='Marvel')
        Workout.objects.create(name='Situps', description='Core workout', suggested_for='DC')

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
