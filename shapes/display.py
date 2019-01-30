from init_db import CreateShapesDB
import shapes


class PrettyPrint():
    def __init__(self):
        
        #create database
        self.db = CreateShapesDB()
        #sort by shapes
        self.sortedShapes = sorted(self.db.data, key=self.getKey)
        self.shape_counts = {'circle':0, 'square':0, 'triangle':0}
        self.shape_objects = [shapes.Circle(), shapes.Square(), shapes.Triangle()]

    def getKey(self, shape):
        return shape.name

    def print_db_info(self):
        print("Database contains ", len(self.sortedShapes), " shapes.")
        for element in self.shape_objects:
            count = sum(p.name == element.name for p in self.sortedShapes)
            print("There are ",count ,element.name, "objects")
            self.shape_counts[element.name] = count
        #display shapes
        for item in self.shape_objects:
            item.__repr__(self.shape_counts[item.name])
            
#try to print out all shapes of a sort on a single line
#so maybe like item.__repr__() * sum(p.name == 'circle' for p in self.sortedShapes) or something???
display = PrettyPrint()
display.print_db_info()
