from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=100, verbose_name='Player name')
    position = models.CharField(max_length=50, verbose_name='Position')
    number = models.PositiveBigIntegerField(verbose_name='Number')
    nationality = models.CharField(max_length=50, verbose_name='Nationality')

    def __str__(self):
        return f"{self.number}. {self.name}"

    class Meta:
        verbose_name = 'Player'
        verbose_name_plural = 'Players'


class FanMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name='Fan name')
    message = models.TextField(verbose_name='Message')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.created_at.strftime('%d/%m/%Y')}"

    class Meta:
        verbose_name = 'Fan message'
        verbose_name_plural = 'Fans messages'
