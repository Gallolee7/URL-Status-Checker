import unittest
from src.url_checker import URLChecker

class TestURLChecker(unittest.TestCase):
    def setUp(self):
        self.checker = URLChecker(timeout=5)
    
    def test_single_url(self):
        result = self.checker.check_single_url('https://httpbin.org/status/200')
        self.assertEqual(result['status_code'], 200)
    
    def test_invalid_url(self):
        result = self.checker.check_single_url('https://invalid-url-that-should-not-exist.xyz')
        self.assertIsNotNone(result['error'])
    
    def test_multiple_urls(self):
        urls = [
            'https://httpbin.org/status/200',
            'https://httpbin.org/status/404'
        ]
        results = self.checker.check_urls(urls)
        self.assertEqual(len(results), 2)

if __name__ == '__main__':
    unittest.main()
