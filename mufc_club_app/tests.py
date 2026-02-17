from django.test import TestCase
from .models import Player, FanMessage
from django.db import IntegrityError
from django.core.exceptions import ValidationError


class PlayerModelTest(TestCase):
    def setUp(self):
        self.player = Player.objects.create(
            name="Dimitar Berbatov",
            position="Forward",
            number=9,
            nationality="Bulgarian"
        )

    def test_player_number_cannot_be_negative(self):
        ''' If player number is a negative numbre'''
        player = Player(
            name="Mihaylov",
            position="GK",
            number=-1,
            nationality="Bulgarian"
        )

        with self.assertRaises(ValidationError):
            player.full_clean()

    def test_player_str_method(self):
        expected_name = f"{self.player.number}. {self.player.name}"
        self.assertEqual(str(self.player), expected_name)

    def test_player_verbose_name_plural(self):
        self.assertEqual(Player._meta.verbose_name_plural, "Players")


class FanMessageModelTest(TestCase):
    def setUp(self):
        self.message = FanMessage.objects.create(
            name="Ivailo Iliev",
            message="Michael Carrick is top manager!"
        )

    def test_fan_message_creation(self):
        self.assertTrue(isinstance(self.message, FanMessage))
        self.assertEqual(self.message.name, "Ivailo Iliev")

    def test_fan_message_str_method(self):
        date_str = self.message.created_at.strftime('%d/%m/%Y')
        expected_str = f"{self.message.name} - {date_str}"
        self.assertEqual(str(self.message), expected_str)

    def test_fan_message_timestamp(self):
        msg = FanMessage.objects.create(name="Elmira", message="I love you!")
        self.assertIsNotNone(msg.created_at)
