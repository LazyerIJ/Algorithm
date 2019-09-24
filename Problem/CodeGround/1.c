#include <stdio.h>
#include <string.h>
#include <stdlib.h>
void main(){

    int testCase=0;
    int stepCase=0;

    setbuf(stdout, NULL);
    scanf("%d",&testCase);getchar();

    for(stepCase=0; stepCase<testCase; stepCase++){

	    int testLength=0;
	    long int num=0;
	    long int result=0;
	    scanf("%d",&testLength);getchar();

	    for(int i=0; i<testLength; i++){
	        scanf("%ld", &num);getchar();
            result ^= num;
	    }

	    printf("Case#%d\n",stepCase+1);
	    printf("%ld\n",result);
    }
    
}



