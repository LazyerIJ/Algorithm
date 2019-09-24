/*
You should use the statndard input/output

in order to receive a score properly.

Do not use file input and output

Please be very careful. 
*/

#include <stdio.h>
#include <stdlib.h>


int partition( int a[], int l, int r) {
   int pivot, i, j, t;
   pivot = a[l];
   i = l; j = r+1;

   while( 1)
   {
   	do ++i; while( a[i] <= pivot && i <= r );
   	do --j; while( a[j] > pivot );
   	if( i >= j ) break;
   	t = a[i]; a[i] = a[j]; a[j] = t;
   }
   t = a[l]; a[l] = a[j]; a[j] = t;
   return j;
}
void quickSort( int a[], int l, int r)
{
   int j;

   if( l < r )
   {
   	// divide and conquer
       j = partition( a, l, r);
       quickSort( a, l, j-1);
       quickSort( a, j+1, r);
   }

}

int Answer;
int main(void)
{
	int T, test_case;
	setbuf(stdout, NULL);

	scanf("%d", &T);
	for(test_case = 0; test_case < T; test_case++)
	{
        int num=0;
        int* arr;
        int max=0;
        Answer=0;

        scanf("%d",&num);
        getchar();
        arr = (int*)malloc(sizeof(int)*num);

        for(int i=0; i<num; i++){
            scanf("%d",&arr[i]);
            getchar();
        }

        quickSort(arr,0,num-1);

        for(int i=0;i<num;i++){
            int point = arr[i]+num-i;
            max=(point>max)?point:max;

        }

        for (int i=0; i<num; i++)
            if (arr[i]+num >= max) Answer++;
        
		printf("Case #%d\n", test_case+1);
        printf("%d\n", Answer);
        
	}

	return 0;//Your program should return 0 on normal termination.
}

