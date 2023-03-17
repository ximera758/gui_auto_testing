import os
import time

from selenium.webdriver import Keys

from generator.generator import generated_person, generated_file
from locators.practice_form_locators import PracticeFormPageLocators
from pages.base_page import BasePage


class PracticeFormPage(BasePage):
    locators = PracticeFormPageLocators

    def fill_practice_form(self):
        person = next(generated_person())
        file_name, path = generated_file()
        first_name = person.firstname
        last_name = person.lastname
        email = person.email
        mobile_number = person.mobile_number
        current_address = person.current_address
        subject = person.subject

        self.remove_footer()
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(last_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.GENDER_RADIOBUTTON).click()
        self.element_is_visible(self.locators.MOBILE_NUMBER).send_keys(mobile_number)
        self.go_to_element(self.element_is_visible(self.locators.BIRTHDAY_DATE))
        self.element_is_visible(self.locators.BIRTHDAY_DATE).click()
        self.element_is_visible(self.locators.YEAR_DROPDOWN_MENU).click()
        self.element_is_visible(self.locators.YEAR_IN_DROPDOWN_MENU).click()
        self.element_is_visible(self.locators.MONTH_DROPDOWN_MENU).click()
        self.element_is_visible(self.locators.MONTH_IN_DROPDOWN_MENU).click()
        self.element_is_visible(self.locators.INPUT_DATE).click()
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.SUBJECTS).send_keys(subject)
        self.element_is_visible(self.locators.SUBJECTS).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.HOBBIES_CHECKBOX).click()
        self.element_is_present(self.locators.CHOSE_FILE).send_keys(path)
        os.remove(path)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.go_to_element(self.element_is_visible(self.locators.SELECT_STATE_DROP_DOWN_MENU))
        self.element_is_visible(self.locators.SELECT_STATE_DROP_DOWN_MENU).click()
        self.element_is_visible(self.locators.STATE).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.SELECT_CITY_DROP_DOWN_MENU).click()
        self.element_is_visible(self.locators.CITY).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.SUBMIT).click()
        return person

    def check_result_form(self):
        output_list = self.elements_are_present(self.locators.RESULT_FORM)
        data = []
        for item in output_list:
            data.append(item.text)
        return data
