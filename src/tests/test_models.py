from django.test import TestCase


class ModelsTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self):
        pass

    def test_false_is_false(self):
        # Will be removed.
        self.assertFalse(False)
