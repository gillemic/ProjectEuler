#include "stdio.h"
#include "time.h"

long largest_prime_factor(long n) {
    long i = 2;
    while (i*i < n) {
        while(n % i == 0) {
            n = n / i;
        }
        i++;
    } 
    
    return n;
}

int main(int argc, char* argv[]) {
    clock_t start, end;
    double cpu_time_used;

    start = clock();

    long num = largest_prime_factor(600851475143);

    end = clock();
    cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;

    printf("Largest num: %ld\nTime elapsed: %f\n", num, cpu_time_used);

    return 0;
}