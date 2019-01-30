import numpy as np
import shapes


class CreateShapesDB():
    ''' this class is creating a "database" for us to reference '''

    def __init__(self):
        # total number of shapes stored in database
        self.shape_count =9
        # dummy instantiations of the shapes for database function to reference
        self.circle = shapes.Circle()
        self.square = shapes.Square()
        self.triangle = shapes.Triangle()
        self.shapesList = [self.circle, self.square, self.triangle]
        self.data = self.fill_db()

    def fill_db(self):
        ''' fills the database with shapes. '''
        data = []
        for index in range(self.shape_count):
            shape_object = np.random.choice(self.shapesList)
            data.append(shape_object)
        return data

