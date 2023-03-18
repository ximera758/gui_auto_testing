import time

from pages.alerts_frames_windows_page import BrowserWindowsPage, AlertsPage


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


class TestAlert:
    def test_see_alert(self, driver):
        alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
        alert_page.open()
        alert_text = alert_page.check_see_alert()
        assert alert_text == 'You clicked a button'

    def test_alert_appear_5_sec(self, driver):
        alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
        alert_page.open()
        alert_text = alert_page.check_alert_appear_5_sec()
        assert alert_text == 'This alert appeared after 5 seconds'

    def test_confirm_alert(self, driver):
        alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
        alert_page.open()
        alert_text = alert_page.check_confirm_alert()
        assert alert_text == 'You selected Ok'

    def test_prompt_alert(self, driver):
        alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
        alert_page.open()
        text, alert_text = alert_page.check_prompt_alert()
        assert text in alert_text, 'Alert did not show'
