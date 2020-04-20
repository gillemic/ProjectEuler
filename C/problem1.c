#include "stdio.h"
#include "time.h"

int main(int argc, char* argv[]) {
    clock_t start, end;
    double cpu_time_used;
    int sum;

    start = clock();

    sum = 0;

    for (int i = 1; i < 1000; i++) {
        if ((i % 3 == 0) || (i % 5 == 0)) {
            sum = sum + i;
        }
    }

    printf("%d\n", sum);

    end = clock();
    cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;

    printf("%f seconds\n", cpu_time_used);

    return 0;
}