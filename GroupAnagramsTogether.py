"""
Given an array of words, print the count of all anagrams together in sorted order (increasing order of counts).
For example, if the given array is {“cat”, “dog”, “tac”, “god”, “act”}, then grouped anagrams are “(dog, god) (cat, tac, act)”. So the output will be 2 3.

Input:
First line consists of T test case. First line of every test case consists of N, denoting the number of words in array. Second line of every test case consists of words of array.

Output:
Single line output, print the counts of anagrams in increasing order.

Constraints:
1<=T<=100
1<=N<=50

Example:
Input:
2
5
act cat tac god dog
3
act cat tac
Output:
2 3
3
"""
def main():
	testcase = int(input(""))
	for test in range(testcase):
		listlen = int(input(""))
		inputlist = input("").split()
		count = 0
		result = ""
		for item in range(listlen-1):
			if sorted(list(inputlist[item])) == sorted(list(inputlist[item +1])):
				count += 1
			else:
				if count != 0:
					result = result + str(count + 1) + " "
					count = 0
				else:
					result = result + '1' + " "

		result = result + str(count + 1)
		result = [int(item) for item in result.split()]
		outputstr = ""
		for item in sorted(result):
			outputstr += str(item) + " "
		print(outputstr)

if __name__ == "__main__":
	main()
