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


def main():
  driver = Firefox()
  driver.get('https://www.e-typing.ne.jp/')
  print(driver.page_source)
  id_ = 'level_check_btn'
  driver.find_element(
    by=By.ID,
    value=id_,
  ).click()
  driver.find_element(
    by=By.ID,
    value=id_,
  ).click()
  id_ = 'start_btn'
  time.sleep(1)
  driver.switch_to_frame(
    'typing_content',
  )

  driver.find_element(
    by=By.ID,
    value=id_,
  ).click()
  # driver.close()
  # with open('tmp.html', 'w') as f:
  #   f.write(driver.page_source)


  game = driver.find_element(
    by=By.TAG_NAME,
    value='body',
  )
  game.send_keys(Keys.SPACE)

  time.sleep(1 << 2)
  for i in range(15):
    txt = driver.find_element(
      by=By.ID,
      value='sentenceText',
    ).text
    game.send_keys(txt)
    print(txt)
    time.sleep(1.5)
  



if __name__ == '__main__':
  main()