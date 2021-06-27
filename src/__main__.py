import selenium 
from selenium.webdriver import(
  Firefox,
  FirefoxOptions,
)
from \
  selenium.webdriver \
  .common.by \
import (
  By,
)

from \
  selenium.webdriver \
  .common.keys \
import (
  Keys,
)
import time
import re
import enum 
import typing



class CategoryID(
  enum.IntEnum,
):
  ROMA: int = enum.auto()
  KANA: int = enum.auto()
  ENGLISH: int = enum.auto()



import dataclasses 
@dataclasses.dataclass
class ETypingCfg():
  base_url: str



@dataclasses.dataclass
class AuthCfg():
  email: str
  passwd: str



@dataclasses.dataclass
class PlayCfg():
  interval: float


class Play():

  def __call__(
    self,
    game: (
      selenium
      .webdriver
      .remote
      .webelement
      .WebElement
    ),
  ):
    self.__game = game
    t = self.__cfg.interval 
    while 1:
      try:
        self.__read_text()
        self.__input()
        time.sleep(t)
      except:
        break
  

  def __init__(
    self,
    cfg: PlayCfg,
  ):
    self.__cfg = cfg


  def __input(
    self,
  ):
    self.__game.send_keys(
      self.__txt,
    )


  def __read_text(
    self,
  ):
    game = self.__game
    html = game.find_element(
      by=By.ID,
      value='sentenceText',
    ).find_elements(
      by=By.TAG_NAME,
      value='span',
    )[1].get_attribute(
      'outerHTML',
    )
    self.__txt = re.sub(
      r'<[^>]+>',
      '',
      html,
    ).replace('␣', ' ')






@dataclasses.dataclass
class PlayWithLoginCfg():
  base_url: str
  auth: AuthCfg
  play: PlayCfg




@dataclasses.dataclass
class category():
  ...



@dataclasses.dataclass
class LoginFormID():
  email: str = 'mail'
  passwd: str = 'password'
  submit: str = 'login_btn'



@dataclasses.dataclass
class RegisterFormID():
  register: str = 'regist_btn'
  publish: str = 'yesBtn'
  confirm: str = 'okBtn'





class PlayWithLogin():
  def __call__(
    self,
  ):
    self.__init_driver()
    self.__open_page()
    self.__login()
    self.__start_up_game()
    self.__start_game()
    self.__play(self.__game)
    self.__register()
    time.sleep(1)
    self.__driver.close()
      

  def __init__(
    self,
    cfg: PlayWithLoginCfg,
  ):
    self.__cfg = cfg
    self.__play = Play(
      cfg.play,
    )
  

  def __init_driver(
    self,
  ):
    opts = FirefoxOptions()
    opts.headless = True
    self.__driver = Firefox(
      # options=opts,
    )


  def __login(
    self,
  ):
    auth = self.__cfg.auth
    driver = self.__driver
    ids = LoginFormID()
    driver.find_element(
      by=By.ID,
      value=ids.email,
    ).send_keys(auth.email)
    driver.find_element(
      by=By.ID,
      value=ids.passwd,
    ).send_keys(auth.passwd)
    driver.find_element(
      by=By.ID,
      value=ids.submit,
    ).click()



  def __open_page(
    self,
  ):
    self.__driver.get(
      self.__cfg.base_url,
    )
    url = (
      f'{self.__cfg.base_url}/member/cht.asp?tp=2'
    )
    self.__driver.get(url)


  def __start_up_game(
    self,
  ):
    driver = self.__driver
    id_ = 'level_check_member'
    driver.find_element(
      by=By.ID,
      value=id_,
    ).find_element(
      by=By.TAG_NAME,
      value='a',
    ).click()
    time.sleep(1)


  def __start_game(
    self,
  ):
    driver = self.__driver
    driver.switch_to.frame(
      'typing_content',
    )
    driver.find_element(
      by=By.ID,
      value='start_btn',
    ).click()
    time.sleep(1 << 1)
    game = driver.find_element(
      by=By.TAG_NAME,
      value='body',
    )
    game.send_keys(Keys.SPACE)
    time.sleep(1 << 2)
    self.__game = game


  def __register(
    self,
  ) -> typing.NoReturn:
    ids = RegisterFormID()
    game = self.__game
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


def main():

  base_url = (
    'https://www.e-typing.ne.jp/'
  )
  email = 'kagemeka1@gmail.com'
  passwd = 'ruruth12'
  auth = AuthCfg(
    email=email,
    passwd=passwd,
  )
  play = PlayCfg(
    interval=3,
  )
  cfg = PlayWithLoginCfg(
    base_url=base_url,
    auth=auth,
    play=play,
  )
  play = PlayWithLogin(cfg)
  play()
  
  

if __name__ == '__main__':
  main()