from django.db import models

# Create your models here.
class County(models.Model):
    name = models.CharField(max_length = 100)
    stateCode = models.CharField(max_length = 5)

    def __str__(self):
        return self.name


class School(models.Model):
    name = models.CharField(max_length = 100)
    type = models.CharField(max_length = 100)
    county = models.ForeignKey(County, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Pathways(models.Model):
    name = models.CharField(max_length = 100)
    department = models.CharField(max_length = 100)
    image = models.ImageField()
    type = models.CharField(max_length = 100)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    #county = models.ForeignKey(County, on_delete=models.CASCADE) POTENTIALLY#

    def __str__(self):
        return self.name