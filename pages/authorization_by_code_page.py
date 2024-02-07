from pages.base import WebPage
from pages.elements import WebElement


class AuthorizationByCodePage(WebPage):

    def __init__(self, driver, url):
        super(AuthorizationByCodePage, self).__init__(driver, url)

    key_form_enter_button = WebElement(css_selector="a.go_kab")

    title_authorization_by_code_top = WebElement(css_selector="h1.card-container__title")

    authorization_by_code_button = WebElement(id="otp_get_code")

    standard_auth_button = WebElement(id="standard_auth_btn")

    back_to_authorization_by_code_button = WebElement(xpath='//button[@name="back_to_otp_btn"]')
