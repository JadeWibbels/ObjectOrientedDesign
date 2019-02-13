import java.util.*;

public class Main {

    public static void main(String[] args) {
        ShapeDatabase db = new ShapeDatabase();

        List ShapeCollection = new ArrayList(db.shapeCollection);
        Collections.sort(ShapeCollection);
        for (int i = 0; i < db.length; i++) {
            Object next = db.shapeCollection.get(i);
            //System.out.println(next);
            System.out.println(next.getClass().getName());
        }


        ShapeDisplay s = new ShapeDisplay(ShapeCollection);
        System.out.println(s.getCircles());
        System.out.println(s.getSquares());
        System.out.println(s.getTriangles());
    }
}
