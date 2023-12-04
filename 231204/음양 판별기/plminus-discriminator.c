#include <stdio.h>

int main() {
    int n, i, a;
    scanf("%d", &n);

    for(i = 0; i < n; i++) {
        scanf("%d", &a);
        if(a > 0) printf("plus\n");
        else if(a < 0) printf("minus\n");
        else printf("zero\n");
    }
    return 0;
}