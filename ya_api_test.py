import unittest
from unittest import TestCase
import ya_api


class TestYaApi(TestCase):

    def setUp(self):
        print('method setUp')

    def test_create_folder(self):
        self.assertEqual(ya_api.create_folder('test_folder'), 201)

    def test_delete_folder(self):
        self.assertEqual(ya_api.delete_folder('test_folder'), 204)

    def test_create_folder_error(self):
        self.assertEqual(ya_api.create_folder('test_folder'), 500)

    def tearDown(self):
        print('method tearDown')


if __name__ == '__main__':
    unittest.main()

