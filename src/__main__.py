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


  driver.find_element(
    by=By.TAG_NAME,
    value='body',
  ).send_keys(Keys.SPACE)
  



if __name__ == '__main__':
  main()