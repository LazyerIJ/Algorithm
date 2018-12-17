'''

You should use the statndard input/output



in order to receive a score properly.



Do not use file input and output



Please be very careful. 

'''



import sys



'''

	The method below means that the program will read from input.txt, instead of standard(keyboard) input.

	To test your program, you may save input data in input.txt file,

	and call below method to read from the file when using open() method.

	You may remove the comment symbols(#) in the below statement and use it.

	But before submission, you must remove the open function or rewrite comment symbols(#).

'''



#inf = open('input.txt');

inf = sys.stdin 



T = inf.readline();



for t in range(0, int(T)):

    

    Answer=0;

	#############################################################################################

    a_point=[[0,0]]
    b_point=[[0,0]]
    min_colony = 100001
    input_year = int(inf.readline())

    for year in range(input_year):

        a,b,c,d = map(int, inf.readline().split())
        a_point.append([a,b])
        b_point.append([c,d])

        for st1 in range(year):

            spended_1 = year+1+abs(a_point[st1][0]-b_point[st1][0])+abs(a_point[year][1]-b_point[year][1])
            spended_2 = year+1 + abs(a_point[year][0]-a_point[year][0]) + abs(b_point[st1][1]-b_point[st1][1])
            if spended_1 < min_colony and spended_1 <= input_year-year:
                min_colony = spended_1
            if spended_2 < min_colony and spended_2 <= input_year-year:
                min_colony = spended_2

        Answer = min_colony
        if Answer >= 100001:
            Answer = -1


	#############################################################################################

	

	# Print the answer to standard output(screen).

    print('Case #%d' %(int(t)+1))    

    print(Answer)

inf.close()
