from kivy.uix.screenmanager import ScreenManager


class NavigationManager(ScreenManager):
    pages = []

    def push(self, page):
        self.pages.append(self.current)
        self.current = page

    def pop(self):
        if len(self.pages) > 0:
            back_page = self.pages[-1]
            del self.pages[-1]
            self.current = back_page
            return True
        else: quit()
