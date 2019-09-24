import math

input_num1 = int(input())

def sliceLine(line1,line2,line3,center):
    line1 = line1[0:center-3] + '  *  ' + line1[center+2:]
    line2 = line2[0:center-3] + ' * * ' + line2[center+2:]
    line3 = line3[0:center-3] + '*****' + line3[center+2:]
    return line1,line2,line3

def makeStar(center):
    centers=[]
    centers.append(center+3)
    centers.append(center-3)
    return centers

def dimension(count,center,num):
    line1=line2=line3=' '*(num*2-1)
    line1,line2,line3 = sliceLine(line1,line2,line3,center)
    print(line1)
    print(line2)
    print(line3)
    count-=1
    dimension(count,center,num)

