import unittest
from browser_history_3 import BrowserHistory

class TestBrowserHistory(unittest.TestCase):
    def setUp(self):
        self.history = BrowserHistory()
        self.history.add_page("google.com")
        self.history.add_page("youtube.com")
        self.history.add_page("github.com")

    def test_current_page(self):
        self.assertEqual(self.history.current_page(), "github.com")

    def test_go_back(self):
        self.history.go_back()
        self.assertEqual(self.history.current_page(), "youtube.com")
        self.history.go_back()
        self.assertEqual(self.history.current_page(), "google.com")
        self.assertIsNone(self.history.go_back())

    def test_go_forward(self):
        self.history.go_back()
        self.history.go_back()
        self.assertEqual(self.history.current_page(), "google.com")
        self.history.go_forward()
        self.assertEqual(self.history.current_page(), "youtube.com")