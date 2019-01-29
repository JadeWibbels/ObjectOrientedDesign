from init_db import CreateShapesDB
from shapes import Shape
#create database
db = CreateShapesDB()
#sort by shapes


def getKey(shape):
    return shape.name

sortedShapes = sorted(db.data, key=getKey)


#display shapes
for item in sortedShapes:
    item.__repr__()
