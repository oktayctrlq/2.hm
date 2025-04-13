# 📍 Coordinate Stack & Point Class Project

Hello! 👋  
This project was built as a simple and practical demonstration of how geospatial coordinates can be represented, stored, and managed using both custom Python classes and built-in data structures. The core idea was to combine concepts of **OOP (Object-Oriented Programming)** and **stack behavior** using Python lists.

I created a class called `Point` to encapsulate latitude and longitude, then wrote a unit test to validate it. I also used a `.csv` file that contains coordinate points with labels and names, and built a stack mechanism to store and remove them using Python’s native `list` object.

---

## 🧱 Project Structure

| File/Folder            | Description |
|------------------------|-------------|
| `point.py`             | Contains the `Point` class with latitude and longitude attributes |
| `tests/test_point.py`  | Unit test for verifying the behavior of the `Point` class |
| `coordinates.csv`      | CSV file containing example geographic coordinates and place names |
| `import_nodes.py`      | Contains a function to import nodes from CSV and return them as objects |
| `stack_test.py`        | Script that pushes and pops coordinate nodes using a stack (Python list) |

---

## 🗺️ Coordinates Dataset (`coordinates.csv`)

Here is a sample of the CSV file used:

| ID | Latitude  | Longitude | Name                  |
|----|-----------|-----------|-----------------------|
| A  | 39.865547 | 32.733881 | Geomatics Engineering |
| B  | 39.870883 | 32.734847 | Library               |
| C  | 39.867947 | 32.737289 | Refectory             |

Each row in the file represents a geospatial point that was pushed into and later popped from the stack.

---

## 🧪 Testing the `Point` Class

Inside the `tests/test_point.py` file, I wrote a simple unit test using Python’s built-in `unittest` module to ensure the `Point` class works correctly.

```python
import unittest
from point import Point

class TestPoint(unittest.TestCase):
    def test_creation(self):
        p = Point(40.7128, -74.0060)
        self.assertEqual(p.latitude, 40.7128)
        self.assertEqual(p.longitude, -74.0060)

if __name__ == "__main__":
    unittest.main()
