import random

def get_Circle_Area(radius=3.0, num_points=10000):
    points_inside_circle = 0
    
    for _ in range(num_points):
        x = random.uniform(-radius, radius)
        y = random.uniform(-radius, radius)
        if x**2 + y**2 <= radius**2:
            points_inside_circle += 1
    square_area = (2 * radius) ** 2
    circle_area = (points_inside_circle / num_points) * square_area
    
    return circle_area

if __name__ == "__main__":
    radius = 3.0
    number_points = 10000  
    
    area = get_Circle_Area(radius, number_points)
    print(f"The area of a circle with radius {radius} is {area:.5f}")
    
