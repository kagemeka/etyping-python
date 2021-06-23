import selenium 
from selenium.webdriver import(
  Firefox,
)


import dataclasses 
@dataclasses.dataclass
class ETypingCfg():
  base_url: str


def main():
  driver = Firefox()
  driver.get('https://www.e-typing.ne.jp/')
  print(driver.page_source)



if __name__ == '__main__':
  main()