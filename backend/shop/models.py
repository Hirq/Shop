from django.db import models

class Effect(models.Model):

    Levels = (
        ('DIS','DISTORTION'),
        ('OCT','OCTAVER'),
        ('COM','COMPRESOR'),
    )


    effect_name = models.CharField(max_length=80)
    effect_price = models.IntegerField(default=50)
    effect_description = models.CharField(max_length=400)
    effect_count = models.IntegerField(default=1)
    effect_group = models.CharField(max_length=3, choices=Levels)
    effect_photo = models.ImageField(upload_to='images', blank=True, null=True)

    def __str__(self):
        return self.effect_name