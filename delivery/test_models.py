from django.test import TestCase, Client
# from django.urls import reverse
from deliveryfood.models import Employee, UserLevel, MenuDay, MenuEmployee
# import json

class TestModels(TestCase):

    def setUP(self):
        self.employee1 = Employee.objects.create(
            name = "cerne",            
        )

    