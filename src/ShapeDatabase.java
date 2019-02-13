import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class ShapeDatabase {

    //creates random length for list up to 10
    Random random;
    int length;

    List shapeCollection;

    public ShapeDatabase() {
        random = new Random();
        length = random.nextInt(10);
        //System.out.println(length);
        shapeCollection = generate_collection(length);
    }

    protected static List generate_collection(int length)
    {
        Random random = new Random();
        //creates empty list
        List shapeCollection = new ArrayList();

        for(int i = 0; i< length; i++)
        {
            int next_shape = random.nextInt(2);
            //switch statement
            System.out.println(next_shape);
            switch(next_shape)
            {
                //case statements
                case 0:
                    shapeCollection.add(new Circle());
                    break;

                case 1:
                    shapeCollection.add(new Square());
                    break;

                case 2:
                    shapeCollection.add(new Triangle());
            }

        }
        System.out.println(shapeCollection);
        return shapeCollection;
    }


}
