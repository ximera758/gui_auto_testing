from pages.practice_form_page import PracticeFormPage
import time


class TestPracticeForm:

    def test_practice_form(self, driver):
        practice_form_page = PracticeFormPage(driver, 'https://demoqa.com/automation-practice-form')
        practice_form_page.open()
        input_data = practice_form_page.fill_practice_form()
        output_data = practice_form_page.check_result_form()
        assert (input_data.firstname + " " + input_data.lastname, input_data.email) == (output_data[0], output_data[1])
