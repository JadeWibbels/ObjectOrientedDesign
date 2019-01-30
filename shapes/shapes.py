class Shape():
    ''' this is an abstract class which allows polymorphism for specific shape classes'''

    def __init__(self):
        raise NotImplementedError('Do not create raw Shape objects')

    def __str__(self):
        return self.name


class Circle(Shape):
    ''' this is a subclass of Shape, allows instantiation of 'circle' objects '''

    def __init__(self):
        self.name = 'circle'

    def __repr__(self, count):
        print("    Circle     " * count )
        print("      o o      " * count )
        print("   o       o   " * count )
        print("  o         o  " * count )
        print("  o         o  " * count )
        print("   o       o   " * count )
        print("      o o      " * count )


class Triangle(Shape):
    ''' this is a subclass of Shape, allows instantiation of 'triangle' objects '''

    def __init__(self):
        self.name = 'triangle'
        
    def __repr__(self, count):
        print("   Triangle   " * count )
        print("       ^      " * count )
        print("     /   \    " * count )
        print("    /     \   " * count )
        print("   /       \  " * count )
        print("  /         \ " * count ) 
        print("  ----------- " * count )


class Square(Shape):
    ''' this is a subclass of Shape, allows instantiation of 'square' objects '''

    def __init__(self):
        self.name = 'square'

    def __repr__(self, count):
        print("  Square     " * count )
        print("   _________ " * count )
        print("  |         |" * count )
        print("  |         |" * count )
        print("  |         |" * count )
        print("  |         |" * count )
        print("  |_________|" * count )

 
