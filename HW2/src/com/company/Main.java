package com.company;
import java.util.*;

public class Main {

    public static void main(String[] args) {

        // instantiates ShapeDatabase class
        ShapeDatabase db = new ShapeDatabase();
        // gets shape collection from Database object
        List ShapeCollection = new ArrayList(db.shapeCollection);
        // sorts list
        Collections.sort(ShapeCollection);
        System.out.println("Sorted Shape Collection: ");
        System.out.println(ShapeCollection);


        // instantiates ShapeDisplay class and uses class methods to display shape info.
        ShapeDisplay s = new ShapeDisplay(ShapeCollection);
        System.out.println("There are " + s.getCircles()+ " circles.");
        System.out.println(s.shapeDisplay("Circle", s.getCircles()));
        System.out.println("There are " + s.getSquares()+ " squares.");
        System.out.println(s.shapeDisplay("Square", s.getSquares()));
        System.out.println("There are " + s.getTriangles()+ " triangles.");
        System.out.println(s.shapeDisplay("Triangle", s.getTriangles()));
    }
}
