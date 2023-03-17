from selenium.webdriver.common.by import By
import random


class PracticeFormPageLocators:
    # input
    FIRST_NAME = (By.CSS_SELECTOR, "input[id='firstName']")
    LAST_NAME = (By.CSS_SELECTOR, "input[id='lastName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    MOBILE_NUMBER = (By.CSS_SELECTOR, "input[id='userNumber']")
    SUBJECTS = (By.CSS_SELECTOR, "input[id='subjectsInput']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    # date
    BIRTHDAY_DATE = (By.CSS_SELECTOR, "input[id='dateOfBirthInput']")
    INPUT_DATE = (By.XPATH,
                  f"//*[@id='dateOfBirth']/div[2]/div[2]/div/div/div[2]/div[2]/div[{random.randint(1, 6)}]/div[{random.randint(1, 6)}]")
    MONTH_DROPDOWN_MENU = (By.CSS_SELECTOR, "div [id='dateOfBirth'] select[class='react-datepicker__month-select']")
    MONTH_IN_DROPDOWN_MENU = (By.CSS_SELECTOR,
                              f"div [id='dateOfBirth'] select[class='react-datepicker__month-select'] option[value='{random.randint(1, 12)}']")
    YEAR_DROPDOWN_MENU = (By.CSS_SELECTOR, "div [id='dateOfBirth'] select[class='react-datepicker__year-select']")
    YEAR_IN_DROPDOWN_MENU = (
        By.XPATH,
        f"//*[@id='dateOfBirth']/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/select/option[{random.randint(1, 200)}]")
    # file
    CHOSE_FILE = (By.CSS_SELECTOR, "input[id='uploadPicture']")
    # drop_down_menu
    SELECT_STATE_DROP_DOWN_MENU = (By.CSS_SELECTOR, "div[id='state']")
    SELECT_CITY_DROP_DOWN_MENU = (By.CSS_SELECTOR, "div[id='city']")
    CITY = (By.CSS_SELECTOR, "input[id='react-select-4-input']")
    STATE = (By.CSS_SELECTOR, "input[id='react-select-3-input']")
    # button
    GENDER_RADIOBUTTON = (
        By.CSS_SELECTOR, f"div [class*='custom-control'] label[for='gender-radio-{random.randint(1, 3)}']")
    HOBBIES_CHECKBOX = (
        By.CSS_SELECTOR, f"div [class*='custom-control'] label[for='hobbies-checkbox-{random.randint(1, 3)}']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")
    # output
    RESULT_FORM = (By.XPATH, "*//div[@class='table-responsive']//td[2]")
