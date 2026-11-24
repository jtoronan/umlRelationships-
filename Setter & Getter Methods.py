class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self.__width = new_width
        else:
            print("Width must be greater than zero.")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self.__height = new_height
        else:
            print("Height must be greater than zero.")


rect = Rectangle(10, 5)
print(f"Width: {rect.width}, Height: {rect.height}")

rect.width = 20
rect.height = 15
print(f"Updated Width: {rect.width}, Updated Height: {rect.height}")

#Using @property makes code much easier to read because it lets you access and update attributes like normal variables
#(such as rect.width = 20) instead of writing clunky method calls with parentheses (like rect.set_width(20)).
#This keeps math equations and print statements clean and natural while still protecting your data behind the scenes.
