import unittest
from unittest.mock import patch
from src.url_checker import URLChecker

class TestURLChecker(unittest.TestCase):
    def setUp(self):
        self.checker = URLChecker(timeout=5)

    @patch.object(URLChecker, 'check_single_url')
    def test_single_url(self, mock_check_single):
        mock_check_single.return_value = {
            'url': 'https://httpbin.org/status/200',
            'status_code': 200,
            'response_time': 0.1,
            'error': None
        }
        result = self.checker.check_single_url('https://httpbin.org/status/200')
        self.assertEqual(result['status_code'], 200)

    @patch.object(URLChecker, 'check_single_url')
    def test_invalid_url(self, mock_check_single):
        mock_check_single.return_value = {
            'url': 'https://invalid-url-that-should-not-exist.xyz',
            'status_code': None,
            'response_time': None,
            'error': 'Name or service not known'
        }
        result = self.checker.check_single_url('https://invalid-url-that-should-not-exist.xyz')
        self.assertIsNotNone(result['error'])

    @patch.object(URLChecker, 'check_single_url')
    def test_multiple_urls(self, mock_check_single):
        mock_check_single.side_effect = [
            {'url': 'https://httpbin.org/status/200', 'status_code': 200, 'response_time': 0.1, 'error': None},
            {'url': 'https://httpbin.org/status/404', 'status_code': 404, 'response_time': 0.12, 'error': None}
        ]
        urls = [
            'https://httpbin.org/status/200',
            'https://httpbin.org/status/404'
        ]
        results = self.checker.check_urls(urls)
        self.assertEqual(len(results), 2)

if __name__ == '__main__':
    unittest.main()