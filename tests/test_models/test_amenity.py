import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):

    def test_initialization(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertEqual(amenity.name, "")

    def test_attribute_access(self):
        amenity = Amenity()
        amenity.name = "Momma Mia"
        self.assertEqual(amenity.name, "Momma Mia")

    def test_attribute_modification(self):
        amenity = Amenity()
        amenity.name = "watermelone"
        amenity.name = "watermelon"
        self.assertEqual(amenity.name, "watermelon")

    def test_serialization(self):
        amenity = Amenity()
        amenity.name = "Flabberghast"
        serialized_amenity = amenity.to_dict()
        self.assertEqual(serialized_amenity["name"], "Flabberghast")

    def test_deserialization(self):
        amenity_data = {
            "name": "Funny Honey"
        }
        amenity = Amenity(**amenity_data)
        self.assertEqual(amenity.name, "Funny Honey")

if __name__ == '__main__':
    unittest.main()
