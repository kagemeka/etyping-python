import selenium.webdriver.remote.webdriver

import etyping._constants


def _open(driver: selenium.webdriver.remote.webdriver.WebDriver) -> None:
    driver.get(etyping._constants._SITE_URL)
