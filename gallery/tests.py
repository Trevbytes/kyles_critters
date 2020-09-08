from django.test import TestCase
from .models import GalleryEntry


class GalleryModelTest(TestCase):

    def setUp(self):
        GalleryEntry.objects.create(entry_number="123",
                                    critter_name="Test Name",
                                    critter_type="Chicken",
                                    critter_info="Test info",
                                    submitted_by="mouse",
                                    date="22/23/2000",)

    def test_string_representation_entry(self):
        gallery_entry = GalleryEntry.objects.get(entry_number="123")
        self.assertEqual(str(gallery_entry), gallery_entry.entry_number)
