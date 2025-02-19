import java.util.ArrayList;
import java.util.List;

class MathUtils {
    /** Greatest common divisor */
    public static int findGCD(int a, int b) {
        if  (b == 0) {
           return a;
        }
        return findGCD(b, a % b);
    }

    /** Least common multiple */
    public static int findLCM(int a, int b) {
        return (a * b) / findGCD(a, b);
    }
}

class MultiplesSummarizer {
    private final int limit;
    private final List<Integer> dividers;

    public MultiplesSummarizer(int limit) {
        this.limit = limit;
        this.dividers = new ArrayList<>();
    }

    public MultiplesSummarizer addDivider(int newDivider) {
        dividers.add(newDivider);
        return this;
    }

    public int sum() {
       if (dividers.size() == 1) {
           return sumMultiplesDivisibleBy(dividers.get(0));
       }
       else if (dividers.size() == 2) {
           int divider1 = dividers.get(0);
           int divider2 = dividers.get(1);
           return (
               sumMultiplesDivisibleBy(divider1)
               + sumMultiplesDivisibleBy(divider2)
               - sumMultiplesDivisibleBy(
                   MathUtils.findLCM(divider1, divider2)
               )
           );
       }
       else {
           return sumMultiplesDivisibleByAllDividers();
       }
    }

    private int sumMultiplesDivisibleByAllDividers() {
        int multipliersCount = 0;
        for (int multiple = 2; multiple < limit; multiple++) {
            boolean isDivisible = false;
            for (int divider : dividers) {
                if (multiple % divider == 0) {
                    isDivisible = true;
                    break;
                }
            }
            if (isDivisible) {
                multipliersCount += multiple;
            }
        }
        return multipliersCount;
    }

    private int sumMultiplesDivisibleBy(int divider) {
        int maxMultiplier = (limit-1) / divider;
        return divider * (maxMultiplier * (maxMultiplier+1) / 2);
    }
}


public class Main {
    public static void main(String[] args) {
        MultiplesSummarizer summarizer = new MultiplesSummarizer(1000);
        System.out.printf(
            "Sum of multiples [1; 1000) divided by 3 or 5 is: %d",
            summarizer
                .addDivider(3)
                .addDivider(5)
                .sum()
        );
    }
}