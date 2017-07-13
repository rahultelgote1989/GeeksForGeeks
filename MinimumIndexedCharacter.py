"""
Given a string str and another string patt. Find the character in patt that is present at the minimum index in str. If no character of patt is present in str then print ‘No character present’.

Input:
The first line of input contains an integer T denoting the number of test cases. Then the description of T test cases follow. Each test case contains two strings str and patt respectively.

Output:
Print the character in patt that is present at the minimum index in str.
Print "No character present" (without quotes) if no character of patt is present in str.

Constraints:
1<=T<=10^5
1<=length of string<=10^5

Example:
Input:
2
geeksforgeeks
set
adcffaet
onkl

Output:
e
No character present
"""

def main():

    testcount = input("")
    testcount = int(testcount)
    result = []
    for ind in range(testcount):
    	minchar = "No character present"
    	minindex = 9999999999999999999
    	instr1 = list(input(""))
    	instr2 = list(input(""))
    	for char in instr2:
    		for index in range(len(instr1)):
    			if char == instr1[index]:
    				if minindex > index:
    					minindex = index
    					minchar = char

    	result.append(minchar)
    for item in result:
    	print(item)			

if __name__ == "__main__":
	import time
	st = time.time()
	main()
	print("Total time: ", (time.time()-st))
