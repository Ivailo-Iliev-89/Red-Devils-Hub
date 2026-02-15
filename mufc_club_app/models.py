from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    position = models.CharField(max_length=50, verbose_name='Position')
    number = models.PositiveBigIntegerField(verbose_name='Number')
    nationality = models.CharField(max_length=50, verbose_name='Nationality')

    class Meta:
        verbose_name = 'Player'
        verbose_name_plural = 'Players'

    def __str__(self):
        return f"{self.number}. {self.name}"
