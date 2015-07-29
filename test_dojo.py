import unittest


class TestDojo(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_dojo(self):
        self.assertEqual(2, 1 + 1)

if __name__ == 'main':
    unittest.main()