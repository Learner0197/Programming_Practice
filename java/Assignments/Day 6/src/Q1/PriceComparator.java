package Q1;

import java.util.Comparator;

public class PriceComparator implements Comparator<Toys> {

    @Override
    public int compare(Toys o1, Toys o2) {
        return Double.compare(o1.getPrice(), o2.getPrice());
    }

}
