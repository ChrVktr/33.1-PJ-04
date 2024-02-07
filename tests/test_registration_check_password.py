import pytest

from constants import Constants
from pages.registration_page import RegistrationPage


@pytest.mark.parametrize(
    "password",
    [
        "_=o;!dia;-#Cb#",
        "$b_.A|S!-Ads=Da+,AS?"
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
def test_registration_check_password_valid(web_browser, password, product):
    page = RegistrationPage(web_browser, product)
    if product == Constants.URL_KEY_WEB:
        page.key_form_enter_button.click()

    page.standard_auth_button.click()
    page.registration_link.click()

    page.input_field_password.send_keys(password)
    page.registration_button.click()

    assert not page.input_field_password_error_message.is_presented()


@pytest.mark.parametrize(
    "password",
    [
        "",
        "-`N!#Ms",
        "$b_.A|Sad!-Ads=Da+,AS?",
        "gYsQZndd",
        "0123456789",
        "ыфщтщфттщфыв",
        "swrfkj84:",
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
def test_registration_check_password_invalid(web_browser, password, product):
    page = RegistrationPage(web_browser, product)
    if product == Constants.URL_KEY_WEB:
        page.key_form_enter_button.click()

    page.standard_auth_button.click()
    page.registration_link.click()

    page.input_field_password.send_keys(password)
    page.registration_button.click()

    assert page.input_field_password_error_message.is_presented()


@pytest.mark.parametrize(
    "password",
    [
        "_=o;!dia;-#Cb#",
        "$b_.A|S!-Ads=Da+,AS?"
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
def test_registration_confirmed_password_valid(web_browser, password, product):
    page = RegistrationPage(web_browser, product)
    if product == Constants.URL_KEY_WEB:
        page.key_form_enter_button.click()

    page.standard_auth_button.click()
    page.registration_link.click()

    page.input_field_confirm_pass.send_keys(password)
    page.registration_button.click()

    assert not page.input_field_confirm_password_error_message.is_presented()


@pytest.mark.parametrize(
    "password",
    [
        "",
        "-`N!#Ms",
        "$b_.A|Sad!-Ads=Da+,AS?",
        "gYsQZndd",
        "0123456789",
        "ыфщтщфттщфыв",
        "swrfkj84:",
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
def test_register_confirmed_password_invalid(web_browser, password, product):
    page = RegistrationPage(web_browser, product)
    if product == Constants.URL_KEY_WEB:
        page.key_form_enter_button.click()

    page.standard_auth_button.click()
    page.registration_link.click()

    page.input_field_confirm_password.send_keys(password)
    page.registration_button.click()

    assert page.input_field_confirm_password_error_message.is_presented()


@pytest.mark.parametrize(
    "password",
    [
        "_=o;!dia;-#Cb#",
        "$b_.A|S!-Ads=Da+,AS?"
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
def test_registration_both_password_same(web_browser, password, product):
    page = RegistrationPage(web_browser, product)
    if product == Constants.URL_KEY_WEB:
        page.key_form_enter_button.click()

    page.standard_auth_button.click()
    page.registration_link.click()

    page.input_field_password.send_keys(password)
    page.input_field_confirm_password.send_keys(password)
    page.registration_button.click()

    assert not page.input_field_confirm_password_error_message.is_presented()


@pytest.mark.parametrize(
    "product",
    [
        Constants.URL_ELK_WEB,
        Constants.URL_START_WEB,
        Constants.URL_SMARTHOME_WEB,
        Constants.URL_KEY_WEB
    ]
)
def test_register_both_passw_different(web_browser, product):
    page = RegistrationPage(web_browser, product)
    if product == Constants.URL_KEY_WEB:
        page.key_form_enter_button.click()

    page.standard_auth_button.click()
    page.registration_link.click()

    page.input_field_password.send_keys("_=o;!dia;-#Cb#")
    page.input_field_confirm_pass.send_keys("$b_.A|S!-Ads=Da+,AS?")
    page.register_button.click()

    assert page.confirm_passw_err_mess.is_presented()
