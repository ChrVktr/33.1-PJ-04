from pages.base import WebPage
from pages.elements import WebElement


class AuthorizationPage(WebPage):

    def __init__(self, driver, url):
        super(AuthorizationPage, self).__init__(driver, url)

    key_form_enter_button = WebElement(css_selector="a.go_kab")

    standard_auth_button = WebElement(id="standard_auth_btn")

    title_authorization_top = WebElement(css_selector="h1.card-container__title")

    authorization_button = WebElement(id="kc-login")
    authorization_by_temp_code_button = WebElement(id="back_to_otp_btn")

    username_field = WebElement(id="username")
    password_field = WebElement(id="password")

    slogan_key = WebElement(css_selector='div.slogan--70NR0')

    change_account = WebElement(xpath="//span[contains(text(),'Сменить учётную запись')]")

    personal_area = WebElement(xpath="//div[contains(text(),'Личный кабинет')]")
    personal_area_onlime = WebElement(xpath="//a[contains(text(),'Перейти')]")
    personal_area_smarthome = WebElement(id="submit_button")

    authorization_error_message = WebElement(id="form-error-message")
