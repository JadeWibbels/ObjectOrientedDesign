import javafx.scene.shape.Circle;

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
        int circles = Collections.frequency(shapes,"Circle");
        int squares = Collections.frequency(shapes, "Square");
        int trianges = Collections.frequency(shapes, "Triangle");
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
}
