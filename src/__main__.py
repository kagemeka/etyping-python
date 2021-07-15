from kgmk.etyping import (
  ETyping,
  ETypingCfg,
  Auth,
  PlayCfg,
  Category,
)
from kgmk.json import (
  Load as LoadJson,
)
from kgmk.yml import (
  Load as LoadYml,
)
import time

import selenium 
from selenium.webdriver import(
  Firefox,
  FirefoxOptions,
)


def set_globals():
  global cfd, root
  import os 
  cfd = os.path.dirname(
    __file__,
  )
  cfd = os.path.abspath(cfd)
  root = f'{cfd}/../'


def create_driver():
  opts = FirefoxOptions()
  opts.headless = False 
  return Firefox(
    options=opts,
  )


def main():
  set_globals()
  cfg = LoadYml()(
    f'{root}config.yml',
  )
  auth = LoadJson()(
    '/run/secrets/auth',
  )
  play_cfg = PlayCfg(
    interval=cfg['interval'],
  )
  cfg = ETypingCfg(
    Auth(**auth),
    play_cfg,
    Category.from_str(
      cfg['category'],
    )
  )
  driver = create_driver()
  fn = ETyping(cfg)
  fn(driver)
  time.sleep(1)
  driver.close()


if __name__ == '__main__':
  main()