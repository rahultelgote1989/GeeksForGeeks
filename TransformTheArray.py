"""
Given an array containing integers, zero is considered an invalid number and rest all other numbers are valid. 
If two nearest valid numbers are equal then double the value of the first one and make the second number as 0.
At last move all the valid numbers on the left.
Input:
The first line of input contains an integer T denoting the number of test cases. The first line of each test case consists of an integer n. The next line consists of n spaced integers.
Output:
Print the resultant array.
Constraints: 
1<=T<=100
1<=N<=10000
1<=A[i]<=10000
Example:
Input:
1
12
2 4 5 0 0 5 4 8 6 0 6 8
Output:
2 4 10 4 8 12 8 0 0 0 0 0
"""
import sys
from sys import stdin, stdout, stderr

def main():
    
    finallist = list()
    testcount = input("")
    testcount = int(testcount)
    if testcount < 1 or testcount > 100:
        print("Given test count is beyond constrinats")
        sys.exit(1)
    
    for testcase in range(testcount):
        lenlist = int(input(""))
        inlist = [int(item) for item in input("").split()]
        zerolist = []
        nonzerolist = []
        for item in inlist:
            if item == 0:
                zerolist.append(0)
            else:
                nonzerolist.append(item)

        templist = nonzerolist[:]
        count = 0
        for ind in range(len(nonzerolist)-1):
            if nonzerolist[ind] == nonzerolist[ind+1]:
                templist[ind-count] = 2*nonzerolist[ind]
                del templist[ind-count+1]
                templist.append(0)
                count += 1

        templist.extend(zerolist)
        outputstr = ""
        for item in templist:
            outputstr = outputstr + " " + str(item)
            
        print(outputstr)
        
if __name__ == "__main__":
    
    main()
    
    
    
