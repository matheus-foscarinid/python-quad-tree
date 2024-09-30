# Grupo 3
# Nomes: Matheus Foscarini Dias, Enzo Boadas e Mirágini Victória Silveira Malgarizi

from QuadTreeADT import QuadTreeADT
from typing import List

class Point:
  def __init__(self, x: object, y: object) -> None:
    self.x = x
    self.y = y

  def __str__(self) -> str:
    return "({}, {})".format(self.x, self.y)

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
    def search(current: Node, point: Point) -> object:
      # if there is no node, just return None
      if current is None:
        return None

      # if the current node is the point we are looking for
      if current.x == point.x and current.y == point.y:
        return current.value

      # check the quadrant where the point is located
      if point.x < current.x and point.y >= current.y:
        return search(current.NW, point)
      if point.x < current.x and point.y < current.y:
        return search(current.SW, point)
      if point.x >= current.x and point.y >= current.y:
        return search(current.NE, point)
      if point.x >= current.x and point.y < current.y:
        return search(current.SE, point)
      
    return search(self._root, point)

  def all_points(self) -> List[Point]:
    # create a list where we will store all the points
    points: List[Point] = []

    def all_points(current: Node) -> List[Point]:
      # if there is no node, just stop the recursion
      if current is None:
        return
      
      # add the current point to the list
      points.append(Point(current.x, current.y))
      # check all the points in the quadrants
      all_points(current.NW)
      all_points(current.SW)
      all_points(current.NE)
      all_points(current.SE)

    all_points(self._root)
    return points