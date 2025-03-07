#include <stdio.h>

int sum_numbers_devided_by_3_or_5(int limit) {
    int sum = 0;
    for (int i = 0; i < limit; i++) {
        if (i % 3 == 0 || i % 5 == 0) {
            sum += i;
        }
    }
    return sum;
}

int main() {
    int sum_of_multiples = sum_numbers_devided_by_3_or_5(1000);
    printf(
        "Sum of numbers devided by 3 or 5 below 1000: %d\n",
        sum_of_multiples
    ); 
    return 0;
}
