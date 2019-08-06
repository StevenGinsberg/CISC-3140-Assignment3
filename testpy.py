from app import app
import unittest

class testflask(unittest.TestCase):

    def test_home(self):
        test = app.test_client(self)
        response = test.get('/', content_type='html/test')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()