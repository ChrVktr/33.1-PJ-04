import os


class Constants:
    URL_ELK_WEB = "https://lk.rt.ru/"
    URL_ONLIME_WEB = "https://my.rt.ru/"
    URL_START_WEB = "https://start.rt.ru/"
    URL_SMARTHOME_WEB = "https://lk.smarthome.rt.ru/"
    URL_KEY_WEB = "https://key.rt.ru/"

    AUTHORIZATION_FORM_TITLE_TEXT = "Авторизация"
    AUTHORIZATION_BUTTON_TEXT = "Войти"
    AUTHORIZATION_BY_TEMP_CODE_BUTTON_TEXT = "Войти по временному коду"

    AUTHORIZATION_BY_CODE_FORM_TITLE_TEXT = "Авторизация по коду"
    AUTHORIZATION_BY_CODE_BUTTON_TEXT = "Получить код"

    REGISTRATION_FORM_TITLE_TEXT = "Регистрация"
    REGISTRATION_BUTTON_TEXT = "Зарегистрироваться"

    RECOVERY_FORM_TITLE_TEXT = "Восстановление пароля"
    RECOVERY_NEXT_BUTTON_TEXT = "Продолжить"

    VALID_EMAIL = os.getenv("VALID_EMAIL") or "sh.sergey.yur@yandex.ru"
    VALID_LOGIN = os.getenv("VALID_LOGIN") or "rtkid_1707271413347"
    VALID_PASSWORD = os.getenv("VALID_PASSWORD") or "Equilibrium_1253460"

    INVALID_EMAIL = "test.test@1secmail.com"
    INVALID_LOGIN = "test_31y9431y91331683"
    INVALID_PASSWORD = "HnsiBn1#!"
