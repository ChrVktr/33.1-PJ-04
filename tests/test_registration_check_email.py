import pytest

from constants import Constants
from pages.registration_page import RegistrationPage


@pytest.mark.parametrize(
    "email",
    [
        "test.test@mail.com",
        "test-test@mail.com",
        "test.test@1-mail.com",
        "test_test@mail.com",
    ]
)
@pytest.mark.parametrize(
    "product",
    [
        Constants.URL_ELK_WEB,
        Constants.URL_START_WEB,
        Constants.URL_KEY_WEB
    ]
)
def test_registration_check_email_valid(web_browser, email, product):
    page = RegistrationPage(web_browser, product)
    if product == Constants.URL_KEY_WEB:
        page.key_form_enter_button.click()

    page.standard_auth_button.click()
    page.registration_link.click()

    page.input_field_email_phone.send_keys(email)
    page.register_button.click()

    assert not page.error_email_phone.is_presented()


@pytest.mark.parametrize(
    "email",
    [
        "test.mail.ru",
        "@mail.com",
        "#@%^%#$.ru",
        "test test <test@mail.ru>",
        "test@mail.ru (Test Test)",
        "test@mail@gmail.ru",
        "test@-mail.ru",
        "test@.mail.ru",
        "test@mail.....com"
    ]
)
@pytest.mark.parametrize(
    "product",
    [
        Constants.URL_ELK_WEB,
        Constants.URL_START_WEB,
        Constants.URL_KEY_WEB
    ]
)
def test_registration_check_email_invalid(web_browser, email, product):
    page = RegistrationPage(web_browser, product)
    if product == Constants.URL_KEY_WEB:
        page.key_form_enter_button.click()

    page.standard_auth_button.click()
    page.registration_link.click()

    page.input_field_email_or_phone.send_keys(email)
    page.registration_button.click()

    assert page.input_field_error_email_or_phone.is_presented()
