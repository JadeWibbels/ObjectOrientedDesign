import numpy as np

class CreateShapesDB():
    def __init__(self):
        self.shape_count =np.random.choice(30, 1)[0]
        self.shapes = ['circle', 'square', 'triangle']
        self.data = self.fill_db()

    def fill_db(self):
        data = []
        for i in range(self.shape_count):
            data.append(self.shapes[np.random.choice(len(self.shapes), 1)[0]])
        return data

