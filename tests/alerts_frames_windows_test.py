import time

from pages.alerts_frames_windows_page import BrowserWindowsPage


class TestAlertFrameWindow:
    class TestBrowserWindows:

        def test_new_tab(self, driver):
            browser_windows_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            browser_windows_page.open()
            text_result = browser_windows_page.check_open_new_tab()
            assert text_result == 'This is a sample page'



        def test_new_window(self, driver):
            browser_windows_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            browser_windows_page.open()
            text_result = browser_windows_page.check_open_new_tab()
            assert text_result == 'This is a sample page'
