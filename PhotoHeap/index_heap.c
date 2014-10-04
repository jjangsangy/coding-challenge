#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#define MAX 10

void pq_init();
int  pq_empty();
void pq_insert(int);
int  pq_delmax();
void pq_delete(int);

typedef int Item;
static int N, pq[MAX+1], qp[MAX+1];

void exchange(int *a, int *b)
{
    int temp = qp[*a];
    qp[*a] = qp[*b];
    qp[*b] = temp;

    pq[qp[*a]] = *a;
    pq[qp[*b]] = *b;
}

void fix_down(Item a[], int k, int N)
{
    int j;
    while (2*j <= N)
    {
        j = 2*k;

        if ((j < N) && (a[j] < a[j+1]))
            j++;

        if (a[k] < a[j])
            break;

        exchange(&a[k], &a[j]);
        k = j;
    }
}

void fix_up(Item a[], int k)
{
    int parent = k/2;
    while (k > 1 && (a[parent] < a[k]))
    {
        exchange(&a[k], &a[parent]);
        k = parent;
    }
}

void pq_init()
{
    N = 0;
}

int pq_is_empty() {
    return !N;
}

void pq_insert(int k)
{
    qp[k] = ++N;
    pq[N] = k;
    fix_up(pq, N);
}

int pq_delmax()
{
    exchange(&pq[1], &pq[N]);
    fix_down(pq, 1, --N);
    return pq[N+1];
}

int main(int argc, char *argv[])
{

    pq_init();

    int i, popped;
    printf("Enqueueing\n");
    for (i=1; i<argc; i++) {
        printf("arg %i at %s\n", i, argv[i]);
        pq_insert(atoi(argv[i]));
    }

    printf("Removing\n");
    for (; N>=0; popped = pq_delmax())
        printf("pop %i is %i\n", i, popped);
    return 0;
}
