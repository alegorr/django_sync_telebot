from django.db import models

class User(models.Model):

    id = models.IntegerField(null=False, primary_key=True)
    is_bot = models.BooleanField(default=False)
    username = models.CharField(max_length=32, null=True)
    first_name = models.CharField(max_length=32, null=True)
    last_name = models.CharField(max_length=32, null=True)
    language_code = models.CharField(max_length=3, null=True)
    service = models.ForeignKey('Service', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.username)

class Service(models.Model):

    name = models.CharField(max_length=64, null=False)
    address = models.CharField(max_length=128, null=False, primary_key=True)

    def __str__(self):
        return str(self.name)

class Transaction(models.Model):

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, null=False, on_delete=models.CASCADE)
    input = models.TextField()
    output = models.TextField()
    complete = models.BooleanField(default=False)
    error = models.TextField(null=True)

    def __str__(self):
        return "User: {}, Service: {}, Input: {}, Output: {}, Complete: {}, Error: {}".format(self.user, self.service, self.input, self.output, self.complete, self.error)
