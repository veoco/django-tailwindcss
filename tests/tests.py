from django.test import SimpleTestCase, Client


class ClientTestCase(SimpleTestCase):
    def setUp(self):
        self.client = Client()

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200, 'test project error')

        text = response.content.decode('utf-8')
        self.assertIn('style', text, 'style tag not in response')
        self.assertNotIn('bg-gray-100', text, 'bg-gray-100 in default css')

    def test_bg_gray(self):
        response = self.client.get('/bg-gray/')
        self.assertEqual(response.status_code, 200, 'test project error')

        text = response.content.decode('utf-8')
        self.assertIn('bg-gray-100', text, 'bg-gray-100 not in purge_tag css')
        self.assertNotIn('bg-gray-200', text, 'bg-gray-200 in purge_tag css')
    
    def test_bg_gray_raw(self):
        bg_gray_response = self.client.get('/bg-gray/')
        bg_gray_text = bg_gray_response.content.decode('utf-8')

        bg_gray_raw_response = self.client.get('/bg-gray-raw/')
        bg_gray_raw_text = bg_gray_raw_response.content.decode('utf-8')
        
        self.assertEqual(bg_gray_text, bg_gray_raw_text)