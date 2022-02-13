from __future__ import annotations

import dataclasses
import enum
import logging
import re
import time
import typing

import selenium.webdriver.remote.webdriver
import selenium.webdriver.remote.webelement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import etyping._constants
import etyping._site

_LOGGER = logging.getLogger(__name__)


@dataclasses.dataclass(frozen=True)
class _LoginCredentials:
    email: str
    password: str


def _login(
    credentials: _LoginCredentials,
    driver: selenium.webdriver.remote.webdriver.WebDriver,
) -> None:
    driver.find_element(by=By.ID, value="mail").send_keys(credentials.email)
    driver.find_element(by=By.ID, value="password").send_keys(
        credentials.password
    )
    driver.find_element(by=By.ID, value="login_btn").click()


class _Type(enum.IntEnum):
    ROMA: int = 0
    ENGLISH: int = 2


def _type_from_str(type: str) -> _Type:
    if type == "en":
        return _Type.ENGLISH
    elif type == "roma":
        return _Type.ROMA
    else:
        raise ValueError(f"Unknown language: {type}")


def _open(
    driver: selenium.webdirver.remote.webdriver.WebDriver,
    type: _Type,
) -> None:
    BASE_URL = f"{etyping._constants._SITE_URL}/member/cht.asp?tp="
    url = f"{BASE_URL}{type.value}"
    driver.get(url)
    _LOGGER.info(f"Opening {url}")


def _start(
    driver: selenium.webdriver.remote.webdriver.WebDriver,
) -> selenium.webdriver.remote.webelement.WebElement:
    driver.find_element(by=By.ID, value="level_check_member",).find_element(
        by=By.TAG_NAME,
        value="a",
    ).click()
    time.sleep(1)
    driver.switch_to.frame("typing_content")
    driver.find_element(by=By.ID, value="start_btn").click()
    time.sleep(2)
    game = driver.find_element(by=By.TAG_NAME, value="body")
    game.send_keys(Keys.SPACE)
    time.sleep(3)
    _LOGGER.info("Started")
    return game


def _read_text(game: selenium.webdriver.remote.webelement.WebElement) -> str:
    html = (
        game.find_element(
            by=By.ID,
            value="sentenceText",
        )
        .find_elements(
            by=By.TAG_NAME,
            value="span",
        )[1]
        .get_attribute("outerHTML")
    )
    text = re.sub(r"<[^>]+>", "", html).replace("␣", " ")
    _LOGGER.info(f"Read text: {text}")
    return typing.cast(str, text)


def _play(
    game: selenium.webdriver.remote.webelement.WebElement,
    interval_per_letter: float = 0.07,
) -> None:
    while True:
        time.sleep(0.5)
        try:
            text = _read_text(game)
            time.sleep(interval_per_letter * len(text))
            game.send_keys(text)
        except Exception as e:
            _LOGGER.debug(e)
            _LOGGER.info("Game end")
            break


def _get_score(
    game: selenium.webdriver.remote.webelement.WebElement,
) -> int:
    return int(
        game.find_element(by=By.ID, value="current")
        .find_element(by=By.CLASS_NAME, value="result_data")
        .find_element(by=By.CLASS_NAME, value="data")
        .text
    )


def _register(game: selenium.webdriver.remote.webelement.WebElement) -> None:
    game.find_element(by=By.ID, value="regist_btn").click()
    time.sleep(2)
    game.find_element(by=By.ID, value="yesBtn").click()
    time.sleep(2)
    game.find_element(by=By.ID, value="okBtn").click()
    _LOGGER.info("Registered")


def run(
    driver: selenium.webdriver.remote.webdriver.WebDriver,
    credentials: _LoginCredentials,
    game_type: _Type,
) -> None:
    etyping._site._open(driver)
    _login(credentials, driver)
    _open(driver, game_type)
    game = _start(driver)
    interval_per_letter = 0.07
    if game_type == _Type.ENGLISH:
        interval_per_letter += 0.03
    _play(game, interval_per_letter)
    score = _get_score(game)
    _LOGGER.info(f"Score: {score}")
    if score < 0:
        return
    if game_type == _Type.ROMA and score >= 800:
        return
    if game_type == _Type.ENGLISH and score >= 600:
        return
    _register(game)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
