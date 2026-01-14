
from shapes.circle import Circle
from shapes.rectangle import Rectangle

def main():
    print("--- Testing Absolute Imports ---")
    c = Circle(5, 10, 20)
    r = Rectangle(10, 5)

    print(f"Circle Area: {c.area():.2f}")
    print(f"Circle Center: {c.center}") # Point class via relative import in circle.py
    print(f"Rectangle Area: {r.area():.2f}")

if __name__ == "__main__":
    main()