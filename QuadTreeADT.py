from abc import ABC, abstractmethod
from Interval2D import Interval2D
from Point import Point
from typing import List

class QuadTreeADT(ABC):
  @abstractmethod
  def clear(self) -> None: ...
  @abstractmethod
  def is_empty(self) -> bool: ...
  @abstractmethod
  def insert(self, x: object, y: object, value: object) -> None: ...
  @abstractmethod
  def query_2D(self, rect: Interval2D) -> None: ...
  @abstractmethod
  def search(self, point: Point) -> object: ...
  @abstractmethod
  def all_points(self) -> List[Point]: ...
