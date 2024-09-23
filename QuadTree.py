from QuadTreeADT import QuadTreeADT
from Interval2D import Interval2D
from Point import Point
from typing import List

class Node:
  def __init__(self, x: object, y: object, value: object) -> None:
    self.x = x
    self.y = y
    self.value = value
    self.NW, self.NE, self.SE, self.SW = None, None, None, None

  def __str__(self) -> str:
    return "({}, {}) {}".format(self.x, self.y, self.value)

class QuadTree(QuadTreeADT):
  def __init__(self) -> None:
    self._root: Node = None

  def clear(self) -> None:
    self._root = None

  def is_empty(self) -> bool:
    return self._root is None

  def insert(self, x: object, y: object, value: object) -> None:
    def insert(current: Node, x: object, y: object, value: object) -> None:
      if current is None:
        return Node(x, y, value)
      elif x < current.x and y >= current.y:
        current.NW = insert(current.NW, x, y, value)
      elif x < current.x and y < current.y:
        current.SW = insert(current.SW, x, y, value)
      elif x >= current.x and y >= current.y:
        current.NE = insert(current.NE, x, y, value)
      elif x >= current.x and y < current.y:
        current.SE = insert(current.SE, x, y, value)
      return current

    self._root = insert(self._root, x, y, value)

  def query_2D(self, rect: Interval2D) -> None:
    def query_2D(current: Node, rect: Interval2D) -> None:
      if current is None:
        return
      x_min = rect.interval_x.min
      x_max = rect.interval_x.max
      y_min = rect.interval_y.min
      y_max = rect.interval_y.max
      if rect.contains(current.x, current.y):
        print(current)
      if x_min < current.x and y_max >= current.y:
        query_2D(current.NW, rect)
      if x_min < current.x and y_min < current.y:
        query_2D(current.SW, rect)
      if x_max >= current.x and y_max >= current.y:
        query_2D(current.NE, rect)
      if x_max >= current.x and y_min < current.y:
        query_2D(current.SE, rect)

    query_2D(self._root, rect)

  def search(self, point: Point) -> object:
    # TODO
    def search(current: Node, point: Point) -> object:
      print(current, point)  
      
    return search(self._root, point)

  def all_points(self) -> List[Point]:
    # TODO
    def all_points(current: Node) -> List[Point]:
      print(current)  

    return all_points(self._root)

if __name__ == "__main__":
  qt = QuadTree()
  print(qt.is_empty())

