class PageNode:
    def __init__(self, url):
        self.url = url
        self.prev = None
        self.next = None

class BrowserHistory:
    def __init__(self):
        self.current = None

    def add_page(self, url):
        new_page = PageNode(url)
        if self.current:
            self.current.next = new_page
            new_page.prev = self.current
        self.current = new_page

    def go_back(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
            return self.current.url
        return None

    def go_forward(self):
        if self.current and self.current.next:
            self.current = self.current.next
            return self.current.url
        return None

    def current_page(self):
        return self.current.url if self.current else None



browser = BrowserHistory()
browser.add_page("google.com")
browser.add_page("youtube.com")
browser.add_page("github.com")
print("Current:", browser.current_page())
browser.go_back()
print("Back to: ", browser.current_page())
browser.go_forward()
print("Forward to: ", browser.current_page())