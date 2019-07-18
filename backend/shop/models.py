from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User

class Effect(models.Model):

    Levels = (
        ('DIS','DISTORTION'),
        ('OCT','OCTAVER'),
        ('COM','COMPRESOR'),
    )
    who = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    effect_id = models.AutoField(primary_key=True)
    effect_name = models.CharField(max_length=80)
    effect_price = models.IntegerField(default=50)
    effect_description = models.CharField(max_length=400)
    effect_count = models.IntegerField(default=1)
    effect_group = models.CharField(max_length=3, choices=Levels)
    effect_photo = models.ImageField(upload_to='images', blank=True, null=True)
    slug = models.SlugField(max_length=200, db_index=True, default=1)

    def __str__(self):
        return self.effect_name

    def get_absolute_url(self):
        return reverse('product_detail',
                       args=[self.effect_id, self.slug])