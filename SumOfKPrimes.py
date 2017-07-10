"""
Given two numbers N and K. Find out if ‘N’ can be written as a sum of ‘K’ prime numbers.

Input:
The first line of input contains an integer T denoting the number of test cases. Each test case contains two space separated integers N and K.​

Output:
Print "1" if N can be expressed as a sum of K primes else print "0".

Constraints:
1<=T<=1000
1<=N,K<=109

Example:
Input:
2
10 2
2 2

Output:
1
0
"""

import sys
from sys import stdin, stdout, stderr

def main():
    result = []
    testcount = int(input(""))
    for test in range(testcount):
        numstr = input("")
        num1 = int(numstr.split()[0])
        num2 = int(numstr.split()[1])
        if num2 > (num1/2):
            result.append(0)
        else:
            result.append(1)
        
    for item in result:
        print(item)
        
if __name__ == "__main__":
    main()
