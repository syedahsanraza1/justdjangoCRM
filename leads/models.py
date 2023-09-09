from django.db import models

# Create your models here.

class leads(models.Model):
    SOUCRCE_FROM = (
        ('Youtube','Youtube'),
        ('Google','Google'),
        ('Newsletter','Newsletter')
    )


    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)

    phoned = models.BooleanField(default=False)
    source = models.CharField(choices=SOUCRCE_FROM , max_length=100)

    profile_picture =models.ImageField(blank=True , null=True)
    special_file = models.FileField(blank=True , null=True)
