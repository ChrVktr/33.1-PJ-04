import pytest

from constants import Constants
from pages.registration_page import RegistrationPage


@pytest.mark.parametrize(
    "lastname",
    [
        "Те",
        "Тевзщыфовыщыз",
        "Тевршыгрвашгышавгрыжсвфщоывзщф"
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
def test_registration_check_last_name_valid(web_browser, lastname, product):
    page = RegistrationPage(web_browser, product)
    if product == Constants.URL_KEY_WEB:
        page.key_form_enter_button.click()

    page.standard_auth_button.click()
    page.registration_link.click()

    page.input_field_lastname.send_keys(lastname)
    page.registration_button.click()

    assert len(page.input_errors_names.get_text()) <= 1


@pytest.mark.parametrize(
    "lastname",
    [
        "",
        "Т",
        "Тетващшыырщващфазыазыщазывщвоаф",
        " ",
        "---------",
        "Hdosankonfdo",
        "123456789_987654321"
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
def test_registration_check_last_name_invalid(web_browser, lastname, product):
    page = RegistrationPage(web_browser, product)
    if product == Constants.URL_KEY_WEB:
        page.key_form_enter_button.click()

    page.standard_auth_button.click()
    page.registration_link.click()

    page.input_field_lastname.send_keys(lastname)
    page.registration_button.click()

    assert len(page.input_errors_names.get_text()) > 0
