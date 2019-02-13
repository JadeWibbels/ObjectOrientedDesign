public abstract class Shape implements Comparable<Shape> {


    public abstract String getName();

    public final int compareTo(Shape s) {

        return getName().compareTo(s.getName());
    }
}

class Circle extends Shape {


    public String getName()
    {
        return "Circle";
    }
}

class Square extends Shape {

    public String getName() {
        return "Square";
    }
}

class Triangle extends Shape {

    public String getName(){
        return "Triangle";
    }
}