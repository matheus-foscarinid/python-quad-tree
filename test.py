from QuadTree import QuadTree, Point

if __name__ == "__main__":
  # criando uma QuadTree de exemplo :)
  qt = QuadTree()
  qt.insert(1, 1, "A")
  qt.insert(2, 2, "B")
  qt.insert(3, 3, "C")
  qt.insert(4, 4, "D")
  qt.insert(5, 5, "E")
  qt.insert(6, 6, "F")
  qt.insert(7, 7, "G")
  qt.insert(8, 8, "H")
  qt.insert(9, 9, "I")
  qt.insert(10, 10, "J")

  # testando a função de search
  print(qt.search(Point(1, 1)))
  print(qt.search(Point(3, 3)))
  print(qt.search(Point(5, 5)))
  print(qt.search(Point(7, 7)))
  print(qt.search(Point(9, 9)))
  print(qt.search(Point(3, 5)))

  # testando a função de all_points
  points = qt.all_points()
  for point in points:
    print(point)

