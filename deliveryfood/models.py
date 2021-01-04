from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=70)

    objects = models.Manager()

    def _str_(self):
        return "{}".format(self.name)


class UserLevel(models.Model):
    name = models.CharField(max_length=70)
    level = models.IntegerField()
    idEmpFK = models.ForeignKey(
        Employee, null=True, blank=True, on_delete=models.CASCADE
    )

    def _str_(self):
        return "{}".format(self.name)


class MenuDay(models.Model):
    options = models.CharField(max_length=200)
    salad = models.CharField(max_length=100)
    dateMenu = models.DateTimeField()
    UserLevelID = models.ForeignKey(
        UserLevel, null=True, blank=True, on_delete=models.CASCADE
    )

    objects = models.Manager()

    def _str_(self):
        return "{}".format(self.options)


class MenuEmployee(models.Model):
    MenuID = models.ForeignKey(MenuDay, null=True, blank=True, on_delete=models.CASCADE)
    EmpID = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.CASCADE)
    preferences = models.CharField(max_length=200)

    objects = models.Manager()
