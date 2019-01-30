from init_db import CreateShapesDB
from shapes import Shape


class PrettyPrint():
    def __init__(self):
        
        #create database
        self.db = CreateShapesDB()
        #sort by shapes
        self.sortedShapes = sorted(self.db.data, key=self.getKey)


    def getKey(self, shape):
        return shape.name

    def print_db_info(self):
        print("There are ", len(self.sortedShapes), " shapes in the database.")
        print("There are ", sum(p.name == 'circle' for p in self.sortedShapes),
              " circles  and ", sum(p.name == 'square' for p in self.sortedShapes),
              " squares in the database.")
        
        #display shapes
        for item in self.sortedShapes:
            item.__repr__()
            
#try to print out all shapes of a sort on a single line
#so maybe like item.__repr__() * sum(p.name == 'circle' for p in self.sortedShapes) or something???
display = PrettyPrint()
display.print_db_info()