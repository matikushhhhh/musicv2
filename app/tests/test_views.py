from logging import setLogRecordFactory
from django.test import TestCase, Client
from 

class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.list_url = reverse('list')

    def test_project_list_GET(self):
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/agregar.html')


    def test_project_list_GET(self):
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/.html')

    
