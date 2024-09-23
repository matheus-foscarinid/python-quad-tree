class Point:
  def __init__(self, x: object, y: object) -> None:
    self.x = x
    self.y = y

  def __str__(self) -> str:
    return "({}, {})".format(self.x, self.y)