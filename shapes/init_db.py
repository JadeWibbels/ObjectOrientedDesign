import numpy as np
from shapes import shapes, circle, square, triangle

class CreateShapesDB():
    def __init__(self):
        self.shape_count =30
        self.shapes = [circle, square, triangle]
        self.data = self.fill_db()

    def fill_db(self):
        data = []
        for index in range(self.shape_count):
            shape_object = np.random.choice(self.shapes)
            shape_object.set_index(self, index)
            data.append(shape_object)
        return data

