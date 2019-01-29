import numpy as np
import shapes


circle = shapes.Circle()
square = shapes.Square()
triangle = shapes.Triangle()
class CreateShapesDB():
    def __init__(self):
        self.shape_count =30
        self.shapesList = [circle, square, triangle]
        self.data = self.fill_db()

    def fill_db(self):
        data = []
        for index in range(self.shape_count):
            shape_object = np.random.choice(self.shapesList)
            #shape_object.set_index(self, index)
            data.append(shape_object)
        return data

