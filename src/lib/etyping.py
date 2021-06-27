from __future__ import (
  annotations,
)
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
import enum 
import typing
from lib import (
  Login,
  AuthCfg,
  Register,
  Play,
  PlayCfg,
  LoadYml,
  LoadJson,
)
import dataclasses 




class CategoryID(
  enum.IntEnum,
):
  ROMA: int = 0
  ENGLISH: int = 2


  @classmethod
  def from_str(
    cls,
    s: str,
  ) -> CategoryID:
    return (
      cls.ROMA if s == 'roma'
      else cls.ENGLISH
    )
    

@dataclasses.dataclass
class ETypingCfg():
  base_url: str
  auth: AuthCfg
  play: PlayCfg
  category: CategoryID
  headless: bool = True


  @classmethod
  def from_files(
    cls,
    path: str,
  ) -> ETypingCfg:
    cfg = LoadYml()(path)
    auth = LoadJson()(
      '/run/secrets/auth'
    )
    return ETypingCfg(
      base_url=cfg['base_url'],
      auth=AuthCfg(
        auth['email'],
        auth['passwd'],
      ),
      play=PlayCfg(
        cfg['interval'],
      ),
      category=(
        CategoryID.from_str(
          cfg['category'],
        )
      ),
      headless=cfg['headless'],
    )



class ETyping():
  def __call__(
    self,
  ):
    self.__init_driver()
    self.__open_website()
    self.__login(self.__driver)
    self.__open_page()
    self.__start_up_game()
    self.__start_game()
    self.__play(self.__game)
    self.__register(
      self.__game,
    )
    time.sleep(1)
    self.__driver.close()
      

  def __init__(
    self,
    cfg: ETypingCfg,
  ):
    self.__cfg = cfg
    self.__play = Play(
      cfg.play,
    )
    self.__login = Login(
      cfg.auth,
    )
    self.__register = (
      Register()
    )
  

  def __init_driver(
    self,
  ):
    opts = FirefoxOptions()
    opts.headless = (
      self.__cfg.headless
    )
    self.__driver = Firefox(
      options=opts,
    )


  def __open_website(
    self,
  ):
    self.__driver.get(
      self.__cfg.base_url,
    )


  def __open_page(
    self,
  ):
    cfg = self.__cfg 
    self.__driver.get(
      f'{cfg.base_url}/'
      'member/cht.asp?tp='
      f'{cfg.category.value}',
    )


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

