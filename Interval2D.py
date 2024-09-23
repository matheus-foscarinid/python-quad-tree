class Interval:
  def __init__(self, min: object, max: object) -> None:
    self.min = min
    self.max = max

  def contains(self, x: object) -> bool:
    return self.min <= x <= self.max

class Interval2D:
  def __init__(self, interval_x: Interval, interval_y: Interval) -> None:
    self.interval_x = interval_x
    self.interval_y = interval_y
    
  def contains(self, x: object, y: object) -> bool:
    return self.interval_x.contains(x) and self.interval_y.contains(y)
