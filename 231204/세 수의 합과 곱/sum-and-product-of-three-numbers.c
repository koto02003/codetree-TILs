#include <stdio.h>

int main() {
    int a, b, c;
    int sum1, mul1;

    scanf("%d", &a);
    scanf("%d", &b);
    scanf("%d", &c);

    sum1 = a + b + c;
    mul1 = a * b * c;
    printf("sum = %d\n", sum1);

    printf("mul = %d", mul1);
    return 0;
}