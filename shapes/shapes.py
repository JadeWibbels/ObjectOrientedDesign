class shapes():
    name = None
    index = 99

    def display(self):
        print(self.name)

    def get_index(self):
        return self.index

    def set_index(self, index):
        self.index = index


class circle(shapes):
    name = 'circle'

    def display():
        print("      o o      ")
        print("   o       o   ")
        print("  o         o  ")
        print("  o         o  ")
        print("   o       o   ") 
        print("      o o      ")

class triangle(shapes):
    name = 'triangle'

    def display():
        print("       ^   ")
        print("     /   \ ")
        print("    /     \ ")
        print("   /       \  ")
        print("  /         \  ")
        print("  ----------- ")

class square(shapes):
    name = 'square'

    def display():
        print("   _________")
        print("  |         |")
        print("  |         |")
        print("  |         |")
        print("  |         |")
        print("  |_________|")

 
