from pages.base import WebPage
from pages.elements import WebElement


class RecoveryPasswordPage(WebPage):

    def __init__(self, driver, url):
        super(RecoveryPasswordPage, self).__init__(driver, url)

    key_form_enter_button = WebElement(css_selector="a.go_kab")

    standard_auth_button = WebElement(id="standard_auth_btn")

    recovery_password_link = WebElement(id="forgot_password")

    title_recovery_password_top = WebElement(css_selector="h1.card-container__title")

    recovery_password_captcha_image = WebElement(css_selector='img[alt="Captcha"]')

    recovery_password_next_button = WebElement(id="reset")
