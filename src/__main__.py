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



def login(driver):
  ... 
  
  email = 'kagemeka1@gmail.com'
  passwd = 'ruruth12'
  


@dataclasses.dataclass
class AuthCfg():
  email: str
  passwd: str



def normalize():
  import string
  print(string.ascii_letters)


def main():
  driver = Firefox()
  base_url = (
    'https://www.e-typing.ne.jp/'
  )
  driver.get(base_url)

  email = 'kagemeka1@gmail.com'
  passwd = 'ruruth12'
  
  driver.find_element(
    by=By.ID,
    value='mail',
  ).send_keys(email)

  driver.find_element(
    by=By.ID,
    value='password',
  ).send_keys(passwd)
  
  driver.find_element(
    by=By.ID,
    value='login_btn',
  ).click()

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

  id_ = 'level_check_member'
  driver.find_element(
    by=By.ID,
    value=id_,
  ).find_element(
    by=By.TAG_NAME,
    value='a',
  ).click()
  time.sleep(1)


  driver.switch_to_frame(
    'typing_content',
  )

  id_ = 'start_btn'
  driver.find_element(
    by=By.ID,
    value=id_,
  ).click()

  time.sleep(1)
  game = driver.find_element(
    by=By.TAG_NAME,
    value='body',
  )
  game.send_keys(Keys.SPACE)
  normalize()
  time.sleep(1 << 2)
  for i in range(15):
    # while True:
    #   txt = driver.find_element(
    #     by=By.ID,
    #     value='sentenceText',
    #   ).find_elements(
    #     by=By.TAG_NAME,
    #     value='span',
    #   )
    #   print(txt)
    #   if not txt:
    #     break
    #   txt = txt[1].text
    #   txt = txt[:10]
    #   txt = txt.replace(
    #     '␣', ' ',
    #   )
    #   game.send_keys(txt)


    txt = driver.find_element(
      by=By.ID,
      value='sentenceText',
    ).text

    game.send_keys(txt)
    print(txt)
    time.sleep(2)



if __name__ == '__main__':
  main()