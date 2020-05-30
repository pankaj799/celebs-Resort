from django.db import models


class UserDetails(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.IntegerField()
    no_of_child = models.IntegerField()
    no_of_adult = models.IntegerField()
    check_in = models.CharField(max_length=255)
    check_out = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Query(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.IntegerField()
    email = models.EmailField()
    suggestions = models.TextField()

    def __str__(self):
        return self.first_name
