class Rectangle:
        def define(self, width, length):
                self.width = width
                self.length = length
        def area(self):
                return self.width * self.length
        def perimeter(self):
                return (self.width + self.length) * 2
        def print_info(self):
                print("length: " + str(self.length))
                print("width: " + str(self.width))
                print("area: " + str(self.area()))
                print("perimeter: " + str(self.perimeter()))
