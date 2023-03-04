from pages.elements_pages import TextBoxPage
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