#include <stdio.h>
#include <stdlib.h>
int Answer;

int main(void)
{
	int T, test_case;
	setbuf(stdout, NULL);

	scanf("%d", &T);
    getchar();
	for(test_case = 0; test_case < T; test_case++)
	{
        int N=0;
        int J=0; 
        int n=0;
        int j=0;
        unsigned long   sum=0;
        unsigned long   *arr;
        unsigned long   temp = 1000000007;

        scanf("%d %d", &N, &J);
        getchar();
        N+=1;
        J+=1;

        arr = (unsigned long*)malloc(sizeof(unsigned long)*N);
        for(int i=0;i<N;i++){
            arr[i]=1;
        }
        sum = N*2-1;
    
        for(j=1;j<J;j++){
            for(n=j;n<N;n++){
               if(n==j){
                    arr[n] = arr[n]*2;
                    //arr[n] = (arr[n]%temp)?(arr[n]>temp):arr[n];
                    sum += arr[n];
               }
               else{
                    arr[n] = arr[n-1]+arr[n];
                    //arr[n] = (arr[n]%temp)?(arr[n]>temp):arr[n];
                    sum+=arr[n]*2;
               }
               //printf("arr[i] : %d   sum : %d\n", arr[n], sum);
               sum%=1000000007;
            }
        }

		printf("Case #%d\n", test_case+1);
        printf("%ld\n", sum);
        
	}

	return 0;//Your program should return 0 on normal termination.
}
