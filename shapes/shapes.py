class Shape(): #superclass
    def __init__(self):
        raise NotImplementedError('Do not create raw Shape objects')

    def __str__(self):
        return self.name

    


class Circle(Shape):
    def __init__(self):
        self.name = 'circle'

    def __repr__(self):
        print("      o o      ")
        print("   o       o   ")
        print("  o         o  ")
        print("  o         o  ")
        print("   o       o   ") 
        print("      o o      ")

class Triangle(Shape):
    def __init__(self):
        self.name = 'triangle'
        
    def __repr__(self):
        print("       ^   ")
        print("     /   \ ")
        print("    /     \ ")
        print("   /       \  ")
        print("  /         \  ")
        print("  ----------- ")

class Square(Shape):
    def __init__(self):
        self.name = 'square'

    def __repr__(self):
        print("   _________")
        print("  |         |")
        print("  |         |")
        print("  |         |")
        print("  |         |")
        print("  |_________|")

 
