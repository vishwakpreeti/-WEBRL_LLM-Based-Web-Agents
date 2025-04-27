from playwright.sync_api import sync_playwright

class WebEnvironment:
    def __init__(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False)  # headless=False to see browser
        self.page = self.browser.new_page()

    def go_to(self, url):
        self.page.goto(url)

    def get_page_text(self):
        return self.page.content()

    def perform_action(self, action):
        if action.startswith("click"):
            _, selector = action.split(" ", 1)
            self.page.click(selector.strip())
        elif action.startswith("type"):
            _, selector, text = action.split(" ", 2)
            self.page.fill(selector.strip(), text.strip())

    def close(self):
        self.browser.close()
        self.playwright.stop()
