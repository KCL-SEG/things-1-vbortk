from django.core.exceptions import ValidationError
from django.test import TestCase
from .models import Thing

class ThingModelTestCase(TestCase):

    def setUp(self):
        self.thing = Thing.objects.create(
            name = 'dog',
            description = "A canine, man's best friend.",
            quantity = 1
        )

    def test_valid_thing(self):
        self._assert_model_is_valid()

    #NAME
    
    def test_name_can_be_30_characters(self):
        self.thing.name = 'x' * 30
        self._assert_model_is_valid()

    def test_name_cannot_be_over_30_characters(self):
        self.thing.name = 'x' * 31
        self._assert_model_is_invalid()

    def test_name_must_be_unique(self):
        Thing.objects.create(
            name = 'cat',
            description = 'feline',
            quantity = 1
        )
        self.thing.name = 'cat'
        self._assert_model_is_invalid()
    
    def test_name_must_not_be_blank(self):
        self.thing.name = ''
        self._assert_model_is_invalid()

    #DESCRIPTION

    def test_description_need_not_be_unique(self):
        Thing.objects.create(
            name = 'cat',
            description = 'feline',
            quantity = 1
        )
        self.thing.description = 'feline'
        self._assert_model_is_valid()
    
    def test_description_may_be_blank(self):
        self.thing.description = ''
        self._assert_model_is_valid()

    def test_description_can_be_120_characters(self):
        self.thing.description = 'x' * 120
        self._assert_model_is_valid()

    def test_description_cannot_be_over_120_characters(self):
        self.thing.description = 'x' * 121
        self._assert_model_is_invalid()
    
    #QUANTITY

    def test_quantity_need_not_be_unique(self):
        Thing.objects.create(
            name = 'cat',
            description = 'feline',
            quantity = 2
        )
        self.thing.quantity = 2
        self._assert_model_is_valid()

    def test_quantity_can_be_0(self):
        self.thing.quantity = 0
        self._assert_model_is_valid()

    def test_quantity_can_be_100(self):
        self.thing.quantity = 100
        self._assert_model_is_valid()

    def test_quantity_can_be_inbetween_0_and_100(self):
        self.thing.quantity = 50
        self._assert_model_is_valid()

    def test_quantity_cannot_be_less_than_0(self):
        self.thing.quantity = -1
        self._assert_model_is_invalid()

    def test_quantity_cannot_be_more_than_100(self):
        self.thing.quantity = 101
        self._assert_model_is_invalid()


    def _assert_model_is_valid(self):
        try:
            self.thing.full_clean()
        except (ValidationError):
            self.fail('Test model should be valid')

    def _assert_model_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.thing.full_clean()

