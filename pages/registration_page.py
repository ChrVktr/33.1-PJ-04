from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class RegistrationPage(WebPage):

    def __init__(self, driver, url):
        super(RegistrationPage, self).__init__(driver, url)

    key_form_enter_button = WebElement(css_selector="a.go_kab")

    standard_auth_button = WebElement(id="standard_auth_btn")

    registration_link = WebElement(id="kc-register")

    title_registration_top = WebElement(css_selector="h1.card-container__title")

    registration_data_section_1 = WebElement(xpath="//p[contains(text(),'Личные данные')]")
    registration_data_section_2 = WebElement(xpath="//p[contains(text(),'Данные для входа')]")

    input_errors_names = ManyWebElements(xpath="//span[contains(text(), 'Необходимо заполнить поле')]")

    input_field_name = WebElement(xpath="//input[@name='firstName']")
    input_field_lastname = WebElement(xpath="//input[@name='lastName']")

    input_field_email_or_phone = WebElement(id="address")
    input_field_error_email_or_phone = WebElement(css_selector="div.email-or-phone span.rt-input-container__meta")

    input_field_password = WebElement(id="password")
    input_field_password_error_message = WebElement(
        css_selector="div.new-password-container__password span.rt-input-container__meta--error"
    )

    input_field_confirm_password = WebElement(id="password-confirm")
    input_field_confirm_password_error_message = WebElement(
        css_selector="div.new-password-container__confirmed-password span.rt-input-container__meta--error"
    )

    registration_button = WebElement(xpath='//button[@name="register"]')
