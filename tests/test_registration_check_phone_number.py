import pytest

from pages.registration_page import RegistrationPage
from constants import Constants


@pytest.mark.parametrize(
    "phone_number",
    [
        "79224329109",
        "9224329167"
        "+7 (922) 432 91 09",
        "+7 922-432-91-09",
        "+79224329109",
        "8 (922) 4329109",
        "8 922 432-91-09",
    ])
@pytest.mark.parametrize(
    "product",
    [
        Constants.URL_ELK_WEB,
        Constants.URL_START_WEB,
        Constants.URL_SMARTHOME_WEB,
        Constants.URL_KEY_WEB
    ]
)
def test_registration_check_phone_number_valid(web_browser, phone_number, product):
    page = RegistrationPage(web_browser, product)
    if product == Constants.URL_KEY_WEB:
        page.key_form_enter_button.click()

    page.standard_auth_button.click()
    page.registration_link.click()

    page.input_field_email_or_phone.send_keys(phone_number)
    page.registration_button.click()

    assert not page.input_field_error_email_or_phone.is_presented()


@pytest.mark.parametrize(
    "phone_number",
    [
        "",
        "+7 4",
        "8122432910",
        "812243291092",
        "+7 123 456-78-901",
        "812243291094",
        "123 456-78-901"
    ]
)
@pytest.mark.parametrize(
    "product",
    [
        Constants.URL_ELK_WEB,
        Constants.URL_START_WEB,
        Constants.URL_SMARTHOME_WEB,
        Constants.URL_KEY_WEB
    ]
)
def test_registration_check_phone_number_invalid(web_browser, phone_number, product):
    page = RegistrationPage(web_browser, product)
    if product == Constants.URL_KEY_WEB:
        page.key_form_enter_button.click()

    page.standard_auth_button.click()
    page.registration_link.click()

    page.input_field_email_or_phone.send_keys(phone_number)
    page.registration_button.click()

    assert page.input_field_error_email_or_phone.is_presented()
