import time
import allure
from pages.alerts_frames_windows_page import BrowserWindowsPage, AlertsPage, FramesPage, NestedFramesPage

@allure.suite("Alert frames windows ")
class TestAlertFrameWindow:
    @allure.feature('Check Browser windows')
    class TestBrowserWindows:

        @allure.title('Check new tab')
        def test_new_tab(self, driver):
            browser_windows_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            browser_windows_page.open()
            text_result = browser_windows_page.check_open_new_tab()
            assert text_result == 'This is a sample page'

        @allure.title('Check new window')
        def test_new_window(self, driver):
            browser_windows_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            browser_windows_page.open()
            text_result = browser_windows_page.check_open_new_tab()
            assert text_result == 'This is a sample page'

    @allure.feature('Check Alert')
    class TestAlert:

        @allure.title('Check see alert')
        def test_see_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_see_alert()
            assert alert_text == 'You clicked a button'

        @allure.title('Check alert appear 5 sec')
        def test_alert_appear_5_sec(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_alert_appear_5_sec()
            assert alert_text == 'This alert appeared after 5 seconds'

        @allure.title('Check comnfirm alert')
        def test_confirm_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_confirm_alert()
            assert alert_text == 'You selected Ok'

        @allure.title('Check prompt alert')
        def test_prompt_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            text, alert_text = alert_page.check_prompt_alert()
            assert text in alert_text, 'Alert did not show'

    @allure.feature('Check frames')
    class TestFrames:

        @allure.title('Check test frame')
        def test_frame(self, driver):
            frame_page = FramesPage(driver, 'https://demoqa.com/frames')
            frame_page.open()
            result_frame1 = frame_page.check_frame('frame1')
            result_frame2 = frame_page.check_frame('frame2')
            assert result_frame1 == ['This is a sample page', '500px', '350px']
            assert result_frame2 == ['This is a sample page', '100px', '100px']

    @allure.feature('Check nested frames')
    class TestNestedFrames:

        @allure.title('Check nested frames')
        def test_nested_frames(self, driver):
           nested_frame_page = NestedFramesPage(driver, 'https://demoqa.com/nestedframes')
           nested_frame_page.open()
           parent_text, child_text = nested_frame_page.check_nested_frames()
           assert parent_text == 'Parent frame', 'Nested frame doesnt not exist'
           assert child_text == 'Child Iframe', 'Nested frame doesnt not exist'
