from django.test import TestCase
from core.models import User, Service, Transaction

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(id=0, username="Buba")
        User.objects.create(id=1, username="Kiki")

    def test_user_creation(self):
        self.assertEqual(len(User.objects.all()), 2)

class ServiceTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=0, username="Buba")
        self.service1 = Service.objects.create(name="service1", address="address1")
        self.service2 = Service.objects.create(name="service2", address="address2")

    def test_set_user_service1(self):
        self.user.service = self.service1
        self.user.save()
        self.assertEqual(self.user.service.name, self.service1.name)

    def test_set_user_service2(self):
        self.user.service = self.service2
        self.user.save()
        self.assertEqual(self.user.service.name, self.service2.name)

class TransactionTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=0, username="Buba")
        service = Service.objects.create(name="service", address="address")
        self.user.service = service
        self.user.save()

    def test_transaction_creation(self):
        transaction = Transaction.objects.create(user=self.user, service=self.user.service, input="test")
        self.assertEqual(len(Transaction.objects.all()), 1)
