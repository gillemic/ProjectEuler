#include "stdio.h"
#include "time.h"

int main(int argc, char* argv[]) {
    clock_t start, end;
    double cpu_time_used;
    int sum = 2, i = 2, prev = 1;

    start = clock();

    while (i < 4000001) {
        i = i + prev;
        prev = i - prev;

        if (i % 2 == 0) {
            sum = sum + i;
        }
    }

    end = clock();
    cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;

    printf("Sum: %d\nTime elapsed: %f\n", sum, cpu_time_used);

    return 0;
}