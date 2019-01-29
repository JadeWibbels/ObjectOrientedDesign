from init_db import CreateShapesDB
from shapes import shapes, circle, square, triangle
#create database
db = CreateShapesDB()
#sort?
#is this even really necessary?

#display shapes
for shape in db.data:
    shape.display()
