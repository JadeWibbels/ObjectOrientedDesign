package com.company;
import java.util.Collections;
import java.util.List;

public class ShapeDisplay {
    int circles;
    int squares;
    int triangles;
    List shapes;

    public ShapeDisplay(List shapesCollection)
    {
        shapes = shapesCollection;
        circles = 0;
        squares = 0;
        triangles = 0;

        for(int i = 0; i< shapes.size(); i++){
            String shape = shapes.get(i).toString();
            switch(shape)
            {
                case "Circle":
                    circles = circles + 1;
                    break;
                case "Square":
                    squares = squares + 1;
                    break;
                case "Triangle":
                    triangles = triangles +1;
                    break;
            }
        }
    }
    public int getCircles()
    {
        return circles;
    }

    public int getSquares()
    {
        return squares;
    }

    public int getTriangles()
    {
        return triangles;
    }

    public String shapeDisplay(String shape_name, int length)
    {
        String newString = shape_name;
        for(int i = 1; i<length; i++)
        {
            newString = newString + " " + shape_name;
        }
        return newString;
    }
}
