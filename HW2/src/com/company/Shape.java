package com.company;

public abstract class Shape implements Comparable<Shape> {

    String name;

    public Shape(String shape_name){
        name = shape_name;
    };

    public String toString(){
        return name;
    }

    public final int compareTo(Shape s) {

        return toString().compareTo(s.toString());
    }
}

class Circle extends Shape {

    public Circle(String shape_name)
    {
        super(shape_name);
    }
    @Override
    public String toString(){
        return name;
    }

}

class Square extends Shape {

    public Square(String shape_name)
    {
        super(shape_name);
    }

    @Override
    public String toString(){
        return name;
    }
}

class Triangle extends Shape {

    public Triangle(String shape_name)
    {
        super(shape_name);
    }
    @Override
    public String toString(){
        return name;
    }
}