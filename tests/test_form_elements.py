import pytest

from constants import Constants
from pages.authorization_by_code_page import AuthorizationByCodePage
from pages.authorization_page import AuthorizationPage
from pages.recovery_password_page import RecoveryPasswordPage
from pages.registration_page import RegistrationPage


@pytest.mark.parametrize(
    "product",
    [
        Constants.URL_ELK_WEB,
        Constants.URL_ONLIME_WEB,
        Constants.URL_START_WEB,
        Constants.URL_SMARTHOME_WEB,
        Constants.URL_KEY_WEB
    ]
)
def test_authorization_form_elements(web_browser, product):
    page = AuthorizationPage(web_browser, product)

    if product == Constants.URL_KEY_WEB:
        page.key_form_enter_button.click()

    if product != Constants.URL_ONLIME_WEB:
        page.standard_auth_button.click()

    assert page.title_authorization_top.is_presented()
    assert page.title_authorization_top.get_text() == Constants.AUTHORIZATION_FORM_TITLE_TEXT

    assert page.authorization_button.is_presented()
    assert page.authorization_button.get_text() == Constants.AUTHORIZATION_BUTTON_TEXT

    assert page.authorization_by_temp_code_button.is_presented()
    assert page.authorization_by_temp_code_button.get_text() == Constants.AUTHORIZATION_BY_TEMP_CODE_BUTTON_TEXT


@pytest.mark.parametrize(
    "product",
    [
        Constants.URL_ELK_WEB,
        Constants.URL_ONLIME_WEB,
        Constants.URL_START_WEB,
        Constants.URL_SMARTHOME_WEB,
        Constants.URL_KEY_WEB
    ]
)
def test_authorization_by_code_form_elements(web_browser, product):
    page = AuthorizationByCodePage(web_browser, product)

    if product == Constants.URL_KEY_WEB:
        page.key_form_enter_button.click()

    if product == Constants.URL_ONLIME_WEB:
        page.back_to_authorization_by_code_button.click()

    assert page.title_authorization_by_code_top.is_presented()
    assert page.title_authorization_by_code_top.get_text() == Constants.AUTHORIZATION_BY_CODE_FORM_TITLE_TEXT

    assert page.authorization_by_code_button.is_presented()
    assert page.authorization_by_code_button.get_text() == Constants.AUTHORIZATION_BY_CODE_BUTTON_TEXT


@pytest.mark.parametrize(
    "product",
    [
        Constants.URL_ELK_WEB,
        Constants.URL_START_WEB,
        Constants.URL_SMARTHOME_WEB,
        Constants.URL_KEY_WEB
    ]
)
def test_registration_form_elements(web_browser, product):
    page = RegistrationPage(web_browser, product)
    if product == Constants.URL_KEY_WEB:
        page.key_form_enter_button.click()

    page.standard_auth_button.click()
    page.registration_link.click()

    assert page.title_registration_top.is_presented()
    assert page.title_registration_top.get_text() == Constants.REGISTRATION_FORM_TITLE_TEXT

    assert page.registration_data_section_1.is_presented()
    assert page.registration_data_section_2.is_presented()

    assert page.registration_button.is_presented()
    assert page.registration_button.get_text() == Constants.REGISTRATION_BUTTON_TEXT


@pytest.mark.parametrize(
    "product",
    [
        Constants.URL_ELK_WEB,
        Constants.URL_ONLIME_WEB,
        Constants.URL_START_WEB,
        Constants.URL_SMARTHOME_WEB,
        Constants.URL_KEY_WEB
    ]
)
def test_recovery_form_elements(web_browser, product):
    page = RecoveryPasswordPage(web_browser, product)
    if product == Constants.URL_KEY_WEB:
        page.key_form_enter_button.click()

    if product != Constants.URL_ONLIME_WEB:
        page.standard_auth_button.click()

    page.recovery_password_link.click()

    assert page.title_recovery_password_top.is_presented()
    assert page.title_recovery_password_top.get_text() == Constants.RECOVERY_FORM_TITLE_TEXT

    assert page.recovery_password_captcha_image.is_presented()

    assert page.recovery_password_next_button.is_presented()
    assert page.recovery_password_next_button.get_text() == Constants.RECOVERY_NEXT_BUTTON_TEXT
