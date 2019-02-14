package com.company;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class ShapeDatabase {

    //holds length and list variables
    int length;
    List shapeCollection;

    public ShapeDatabase()
    {
        length = 7;
        shapeCollection = generate_collection(length);
    }

    protected static List generate_collection(int length)
    {
        Random random = new Random();
        //creates empty list
        List shapeCollection = new ArrayList();

        for(int i = 0; i< length; i++)
        {
            int next_shape = random.nextInt(3);
            //switch statement
            System.out.println(next_shape);
            switch(next_shape)
            {
                //case statements
                case 0:
                    shapeCollection.add(new Circle("Circle"));
                    break;

                case 1:
                    shapeCollection.add(new Square("Square"));
                    break;

                case 2:
                    shapeCollection.add(new Triangle("Triangle"));
            }

        }
        System.out.println("Shape Collection:");
        System.out.println(shapeCollection);
        return shapeCollection;
    }


}
