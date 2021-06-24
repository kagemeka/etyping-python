import selenium 
from selenium.webdriver import(
  Firefox,
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



import dataclasses 
@dataclasses.dataclass
class ETypingCfg():
  base_url: str





@dataclasses.dataclass
class AuthCfg():
  email: str
  passwd: str



@dataclasses.dataclass
class PlayWithLoginCfg():
  base_url: str
  auth: AuthCfg




@dataclasses.dataclass
class category():
  ...



@dataclasses.dataclass
class LoginFormID():
  email: str = 'mail'
  passwd: str = 'password'
  submit: str = 'login_btn'



class PlayWithLogin():
  def __call__(
    self,
  ):
    self.__init_driver()
    self.__open_website()
    self.__login()
    self.__start_up_game()
    self.__start_game()
    self.__play()
    
  

  def __init__(
    self,
    cfg: PlayWithLoginCfg,
  ):
    self.__cfg = cfg 
  

  def __init_driver(
    self,
  ):
    self.__driver = Firefox()


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



  def __open_website(
    self,
  ):
    self.__driver.get(
      self.__cfg.base_url,
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
    time.sleep(1)
    game = driver.find_element(
      by=By.TAG_NAME,
      value='body',
    )
    game.send_keys(Keys.SPACE)
    time.sleep(1 << 2)
    self.__game = game


  def __play(
    self,
  ):
    for i in range(15):
      self.__input()
      time.sleep(2)
    self.__register()


  def __input(
    self,
  ):
    game = self.__game
    s = game.find_element(
      by=By.ID,
      value='sentenceText',
    ).text
    game.send_keys(s)
    print(s)

  
  def __register(
    self,
  ):
    game = self.__game
    game.find_element(
      by=By.ID,
      value='regist_btn',
    ).click()
    time.sleep(1)
    game.find_element(
      by=By.ID,
      value='yesBtn',
    ).click()
    time.sleep(1)
    game.find_element(
      by=By.ID,
      value='okBtn',
    ).click()
    # if not ok_btn:
    #   return
    # ok_btn.click()
    



  
  


def login(driver):
  ... 
  
  email = 'kagemeka1@gmail.com'
  passwd = 'ruruth12'
  



def normalize():
  import string
  print(string.ascii_letters)


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
  cfg = PlayWithLoginCfg(
    base_url=base_url,
    auth=auth,
  )
  play = PlayWithLogin(cfg)
  play()
  
  
  # url = (
  #   f'{base_url}/member/cht.asp?tp=2'
  # )
  # driver.get(url)

  # id_ = 'level_check_btn'
  # driver.find_element(
  #   by=By.ID,
  #   value=id_,
  # ).click()
  # driver.find_element(
  #   by=By.ID,
  #   value=id_,
  # ).click()


  # for i in range(15):
  #   # while True:
  #   #   txt = driver.find_element(
  #   #     by=By.ID,
  #   #     value='sentenceText',
  #   #   ).find_elements(
  #   #     by=By.TAG_NAME,
  #   #     value='span',
  #   #   )
  #   #   print(txt)
  #   #   if not txt:
  #   #     break
  #   #   txt = txt[1].text
  #   #   txt = txt[:10]
  #   #   txt = txt.replace(
  #   #     '␣', ' ',
  #   #   )
  #   #   game.send_keys(txt)



if __name__ == '__main__':
  main()