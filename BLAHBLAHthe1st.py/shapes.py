# Supposed to be used as a module
import math
def circle(radius):
    if radius < 0 : return None
    return math.pi * radius ** 2, 2 * math.pi * radius

# return area and perimeter

def recatangle(width, height):
    if width < 0 or height < 0: return None
    return width * height, 2 * (width + height)

def shape_test():
    print(circle(3.33), circle(4.44), circle(-1.11))
    print(recatangle(3.33, 4.44), recatangle(1.2, 2.3), recatangle(-1,-2))

if __name__ == '__main__': #Will be executed only when standalone
    shape_test()
