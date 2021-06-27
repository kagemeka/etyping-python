import dataclasses 
import selenium
from \
  selenium.webdriver \
  .common.by \
import (
  By,
)
import time
import typing



@dataclasses.dataclass
class RegisterFormID():
  register: str = 'regist_btn'
  publish: str = 'yesBtn'
  confirm: str = 'okBtn'



class Register():
  
  def __call__(
    self,
    game: (
      selenium
      .webdriver
      .remote
      .webelement
      .WebElement
    ),
  ) -> typing.NoReturn:
    ids = RegisterFormID()
    game.find_element(
      by=By.ID,
      value=ids.register,
    ).click()
    time.sleep(1)
    game.find_element(
      by=By.ID,
      value=ids.publish,
    ).click()
    time.sleep(1)
    game.find_element(
      by=By.ID,
      value=ids.confirm,
    ).click()