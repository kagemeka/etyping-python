from lib import (
  ETyping,
  ETypingCfg,
)


def set_globals():
  global cfd, root
  import os 
  cfd = os.path.dirname(
    __file__,
  )
  cfd = os.path.abspath(cfd)
  root = f'{cfd}/../'


def main():
  set_globals()
  cfg = ETypingCfg.from_files(
    f'{root}/config.yml'
  )
  print(cfg)
  ETyping(cfg)()
  

if __name__ == '__main__':
  main()