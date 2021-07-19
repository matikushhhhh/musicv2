from django.test import TestCase
from app.models import *

class TestModels(TestCase):

    def setUp(self):
        self .project1 = Project.objects.create(
            name = 'Project1',
            app = 1000
        )

    def test_project_is_assigned_slug_on_creation(self):
        self.assertEqual(self.project1.slug, 'project-1')