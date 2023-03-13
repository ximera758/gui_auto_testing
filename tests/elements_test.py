from pages.elements_pages import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage
import random
import time

class TestElements:
     class TestTextBox:

          def test_text_box(self,driver):
               text_box_page = TextBoxPage(driver,'https://demoqa.com/text-box')
               text_box_page.open()
               full_name, email, current_address, permanent_address=text_box_page.fill_all_fields()
               output_name, output_email,output_cur_add,output_per_add = text_box_page.check_filed_form()
               assert full_name == output_name,"the full name does not match"
               assert email == output_email,"the email does not match"
               assert current_address == output_cur_add,"the current_address does not match"
               assert permanent_address == output_per_add,"the permnent_address does not match"


     class TestCheckBox:

          def test_check_box(self,driver):
               check_box_page = CheckBoxPage(driver,'https://demoqa.com/checkbox')
               check_box_page.open()
               check_box_page.open_full_list()
               check_box_page.click_random_checkbox()
               input_checkbox = check_box_page.get_checked_checkboxes()
               output_result = check_box_page.get_output_result()
               print(input_checkbox)
               print(output_result)
               assert input_checkbox == output_result, 'checkboxes have not been selected'


     class TestRadioButton:

          def test_radio_button(self,driver):
               radio_button_page = RadioButtonPage(driver,'https://demoqa.com/radio-button')
               radio_button_page.open()
               radio_button_page.click_on_the_radio_button('yes')
               output_yes = radio_button_page.get_output_result()
               radio_button_page.click_on_the_radio_button('impressive')
               output_impressive = radio_button_page.get_output_result()
               radio_button_page.click_on_the_radio_button('no')
               output_no =radio_button_page.get_output_result()
               assert output_yes == 'Yes'
               assert output_impressive == 'Impressive'
               assert output_no == 'No'


     class TestTable:

          def test_web_table_add_person(self,driver):
               web_table_page = WebTablePage(driver,'https://demoqa.com/webtables')
               web_table_page.open()
               new_person = web_table_page.add_new_person()
               table_result = web_table_page.check_new_added_person()
               assert new_person in table_result


          def test_web_table_search_person(self,driver):
               web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
               web_table_page.open()
               key_word = web_table_page.add_new_person()[random.randint(0,5)]
               web_table_page.search_some_person(key_word)
               table_result = web_table_page.check_search_person()
               assert key_word in table_result, 'the person was not found i the table'


          def test_web_table_update_perso_info(self,driver):
               web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
               web_table_page.open()
               lastname = web_table_page.add_new_person()[1]
               web_table_page.search_some_person(lastname)
               age = web_table_page.update_person_info()
               row = web_table_page.check_search_person()
               assert age in row, 'the person card has not been changed'


          def test_web_table_delete_perso_info(self,driver):
               web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
               web_table_page.open()
               email = web_table_page.add_new_person()[3]
               web_table_page.search_some_person(email)
               web_table_page.delete_person()
               text = web_table_page.check_delete()
               assert text == "No rows found"

          def test_web_table_change_count_row(self, driver):
               web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
               web_table_page.open()
               count = web_table_page.select_up_to_some_rows()
               assert count==[5,10,20,25,50,100],'The numbers of rows in the table has not been changed incorrectly'


     class TestButtonPages:

          def test_difference_click_on_the_buttons(self,driver):
                button_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
                button_page.open()
                double = button_page.click_on_differend_button('double')
                right = button_page.click_on_differend_button('right')
                click = button_page.click_on_differend_button('click')
                assert double == "You have done a double click","The double click was not present"
                assert right == "You have done a right click","The right click was not present"
                assert click == "You have done a dynamic click","The click was not present"


