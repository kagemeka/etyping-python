import dataclasses 
import re
import selenium
from \
  selenium.webdriver \
  .common.by \
import (
  By,
)
import time



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