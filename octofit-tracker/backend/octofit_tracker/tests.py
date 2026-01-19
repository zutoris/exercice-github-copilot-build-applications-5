from django.test import TestCase
from .models import Team, User, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team', description='Test Desc')
        self.user = User.objects.create(name='Test User', email='test@example.com', team=self.team)
        self.workout = Workout.objects.create(name='Test Workout', description='Desc', suggested_for='Test Team')
        self.activity = Activity.objects.create(user=self.user, type='Course', duration=30, date='2024-01-01')
        self.leaderboard = Leaderboard.objects.create(team=self.team, points=100)

    def test_team_str(self):
        self.assertEqual(str(self.team), 'Test Team')
    def test_user_str(self):
        self.assertEqual(str(self.user), 'Test User')
    def test_workout_str(self):
        self.assertEqual(str(self.workout), 'Test Workout')
    def test_activity_str(self):
        self.assertEqual(str(self.activity), 'Test User - Course')
    def test_leaderboard_str(self):
        self.assertEqual(str(self.leaderboard), 'Test Team - 100 pts')
