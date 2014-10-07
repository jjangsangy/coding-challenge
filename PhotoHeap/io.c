#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include "dbg.h"

#define MAXFEED 256

typedef struct {
    char name[MAXFEED];
    int photos;
} Customer;

int linefeed(FILE *fp)
{
    int index;
    Customer *order = malloc(sizeof(Customer));
    for (index = 0; (ch = fgetc(fp) != ','); index++)
        *(order->name + index)  = ch;
    *(order->name + index) = '\0';

    fscanf(fp, "%d\n", &order->photos);

    return *order
}

int main(int argc, char *argv[])
{
    // Input Validation
    if (argc != 2)
        exit("Argument Mismatch\n");

    // Open File
    FILE *fp = fopen(argv[1], "r");

    // Read File
    while ((feof(fp) != 1) {
        customer = linefeed(fp);

        printf("\n%s\n", customer->name);
        printf("%d\n", customer->photos);
    }

    // Close File
    fclose(fp);
    return 0;
}
