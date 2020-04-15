from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MaxValueValidator
from django.utils import timezone

# Create your models here.
class Client(models.Model):
    ID = models.CharField(max_length=12, primary_key=True) # Nintendo Unique ID
    nickName = models.CharField(max_length=200) # Your nick name
    gender = models.CharField(max_length = 20) # Your gender

    def __str__(self):
        return self.nickName

class Island(models.Model):

    NORTH = 'North'
    SOUTH = 'South'

    SPHERE_CHOICES = [
        (NORTH, 'North sphere'),
        (SOUTH, 'South sphere')
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    islandName = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    sphere = models.CharField(
        max_length=5,
        choices=SPHERE_CHOICES,
        default=NORTH,
    )

    def __str__(self):
        return self.islandName

class Turnip_info(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    price = models.IntegerField(validators=[MaxValueValidator(9999)]) # Price of the turnip
    isSell = models.BooleanField(default=True)
    report_date = models.DateTimeField('date reported', default= timezone.now)

    def __str__(self):
        if self.isSell == True:
            return 'Sell price: ' + str(self.price)
        else:
            return 'Buy price: ' + str(self.price)