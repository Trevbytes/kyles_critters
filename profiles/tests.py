from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UserProfileForm


class ProfileModelTest(TestCase):

    def setUp(self):
        UserProfile.objects.create(user=(User.objects.create(
                                         username='user1')),
                                   default_phone_number='252353',
                                   default_country="test",
                                   default_postcode="324",
                                   default_town_or_city='test',
                                   default_street_address1="234",
                                   default_street_address2="wwer",
                                   default_county="erw")

    def test_string_representation_profile(self):
        profile = UserProfile.objects.get(default_phone_number="252353")
        self.assertEqual(str(profile), profile.user.username)


class ProfileFormTest(TestCase):

    def test_fields_are_explicit_in_user_form_metaclass(self):
        form = UserProfileForm()
        self.assertEqual(form.Meta.fields, ('default_phone_number',
                                            'default_street_address1',
                                            'default_street_address2',
                                            'default_town_or_city',
                                            'default_postcode',
                                            'default_county'))
