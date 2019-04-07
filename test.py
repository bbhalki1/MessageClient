from app import app
import json
import unittest 

class TestMessagesApp(unittest.TestCase): 

    def setUp(self):
        # Create a test client
        self.app = app.test_client()
        self.app.testing = True 

    def test_home(self):
        result = self.app.get('/') 
        self.assertEqual(result.status_code, 200)

    def test_post(self):
        params = '{Hello World !!}'
        result = self.app.post('/messages',
                            data=json.dumps(dict(message=params)),
                            content_type='application/json')
        self.assertIsNotNone(result.data)

    def test_get(self):
        # params = '{Hello World !!}'
        result = self.app.get('/messages/<string:digestId>',
                            data=json.dumps(dict(digestId='123')),
                            content_type='application/json')
        self.assertEqual(result.data,'{\n  "err_msg": "Message not found"\n}')


if __name__ == "__main__":
    unittest.main()