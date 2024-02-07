import pytest

from constants import Constants
from pages.authorization_page import AuthorizationPage


@pytest.mark.parametrize(
    "email",
    [
        Constants.VALID_EMAIL,
        Constants.VALID_LOGIN
    ]
)
@pytest.mark.parametrize(
    "password",
    [
        Constants.VALID_PASSWORD
    ]
)
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
def test_authorization_valid(web_browser, email, password, product):
    page = AuthorizationPage(web_browser, product)
    if product == Constants.URL_KEY_WEB:
        page.key_form_enter_button.click()

    if product != Constants.URL_ONLIME_WEB:
        page.standard_auth_button.click()

    page.username_field = email
    page.password_field = password

    page.authorization_button.click()

    if product == Constants.URL_KEY_WEB:
        assert page.slogan_key.is_presented()
        page.change_account.click(hold_seconds=2)
    else:
        assert page.personal_area.is_presented()


@pytest.mark.parametrize(
    "email",
    [
        Constants.INVALID_EMAIL,
        Constants.INVALID_LOGIN
    ]
)
@pytest.mark.parametrize(
    "password",
    [
        Constants.VALID_PASSWORD,
        Constants.INVALID_PASSWORD
    ]
)
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
def test_authorization_invalid_email(web_browser, email, password, product):
    page = AuthorizationPage(web_browser, product)
    if product == Constants.URL_KEY_WEB:
        page.key_form_enter_button.click()

    if product != Constants.URL_ONLIME_WEB:
        page.standard_auth_button.click()

    page.username_field = email
    page.password_field = password

    page.authorization_button.click()

    assert page.authorization_error_message.is_presented()

    if page.authorization_error_message.is_presented():
        page.username_field = Constants.VALID_EMAIL
        page.password_field = Constants.VALID_PASSWORD

        page.authorization_button.click()


@pytest.mark.parametrize(
    "email",
    [
        Constants.VALID_EMAIL,
        Constants.INVALID_EMAIL,
        Constants.VALID_LOGIN,
        Constants.INVALID_LOGIN
    ]
)
@pytest.mark.parametrize(
    "password",
    [
        Constants.INVALID_PASSWORD
    ]
)
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
def test_authorization_invalid_password(web_browser, email, password, product):
    page = AuthorizationPage(web_browser, product)
    if product == Constants.URL_KEY_WEB:
        page.key_form_enter_button.click()

    if product != Constants.URL_ONLIME_WEB:
        page.standard_auth_button.click()

    page.username_field = email
    page.password_field = password

    page.authorization_button.click()

    assert page.authorization_error_message.is_presented()

    if page.authorization_error_message.is_presented():
        page.username_field = Constants.VALID_EMAIL
        page.password_field = Constants.VALID_PASSWORD

        page.authorization_button.click()
