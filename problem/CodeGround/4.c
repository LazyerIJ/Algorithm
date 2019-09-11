/*
You should use the statndard input/output

in order to receive a score properly.

Do not use file input and output

Please be very careful. 
*/

#include <stdio.h>
#include <math.h>

int Answer;

int main(void)
{
	int T, test_case;
	/*
	   The freopen function below opens input.txt file in read only mode, and afterward,
	   the program will read from input.txt file instead of standard(keyboard) input.
	   To test your program, you may save input data in input.txt file,
	   and use freopen function to read from the file when using scanf function.
	   You may remove the comment symbols(//) in the below statement and use it.
	   But before submission, you must remove the freopen function or rewrite comment symbols(//).
	 */
	// freopen("input.txt", "r", stdin);

	/*
	   If you remove the statement below, your program's output may not be rocorded
	   when your program is terminated after the time limit.
	   For safety, please use setbuf(stdout, NULL); statement.
	 */
	setbuf(stdout, NULL);

	scanf("%d", &T);
    getchar();

    int dot_loc[20] = {13,4,18,1,20,5,12,9,14,11,8,16,7,19,3,17,2,15,10,6};

	for(test_case = 0; test_case < T; test_case++)
	{
        
        int arr[5] = {0,0,0,0,0};
        int count=0;
        int sum=0;
        int point=0;
        int multi=0;
        int pi=3.141592;
        scanf("%d %d %d %d %d",&arr[0],&arr[1],&arr[2],&arr[3],&arr[4]);
        getchar();

        for(int i=0; i<5; i++)
            arr[i] *= arr[i];
        scanf("%d",&count);
        getchar();

        for(int i=0;i<count;i++){

           int x=0;
           int y=0;
           int dist=0;
           float angle=0.0;
           scanf("%d %d",&x,&y);
           getchar();
           dist = x*x+y*y;
           angle = acos(x+y);
            //angle -= 15.0;
           printf("angle : %f\n", angle);
/*
           printf("angle : %f\n", angle);

           for(int j=1;j<21;j++)
               if(angle<j*30){
                   point=dot_loc[j-1];
                    break;
               }
           for(int k=0;k<=4;k++)
               if(dist>=arr[k])
                   multi = k;

           if(multi==0) point=50;
           else if(multi==1) point=2*point;
           else if(multi==2) point=point;
           else if(multi==3) point=3*point;
           else if(multi==4) point=0;

           sum +=point;*/
        }

        Answer=sum;        



		
		/////////////////////////////////////////////////////////////////////////////////////////////
		/*
		   Implement your algorithm here.
		   The answer to the case will be stored in variable Answer.
		 */
		/////////////////////////////////////////////////////////////////////////////////////////////
	
        // Print the answer to standard output(screen).
        
		printf("Case #%d\n", test_case+1);
        printf("%d\n", Answer);
        
	}

	return 0;//Your program should return 0 on normal termination.
}
