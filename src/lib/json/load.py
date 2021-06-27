import json 


class Load():

  def __call__(
    self,
    path: str,
  ) -> dict:
    with open(
      file=path,
      mode='r',
    ) as f:
      return json.load(f)
    