#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include "dbg.h"

#define MAXFIELD 20

typedef struct {
    char name[MAXFIELD];
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
    if (argc != 2)
        exit("Argument Mismatch\n");

    FILE *fp = fopen(argv[1], "r");

    while ((feof(fp) != 1) {
        customer = linefeed(fp);

        printf("\n%s\n", customer->name);
        printf("%d\n", customer->photos);
    }

    fclose(fp);
    return 0;
}
