"""
Cows of FooLand:    
Cows in the FooLand city are interesting animals. One of their specialties is related to producing offsprings. A cow in FooLand produces its first calve (female calf) at the age of two years and proceeds to produce 
other calves (one female calf a year). Now the farmer Harold wants to know how many animals would he have at the end of N years, 
if we assume that none of the calves die, given that initially, he has only one female calf?
Input:
The first line contains a single integer T denoting the number of test cases. Each line of the test case contains a single integer 
N as described in the problem.
Output:
For each test case print in new line the number of animals expected at the end of N years modulo 10^9 + 7.
Constraints:
1 <= T <= 10^3
1 <= N <= 10^18
Example:
Input:
2
2
4
Output:
2
5
Explanation:
At the end of 1 year, he will have only 1 cow, at the end of 2 years he will have 2 animals (one parent cow C1 and other baby 
calf B1 which is the offspring of cow C1). At the end of 3 years, he will have 3 animals (one parent cow C1 and 2 female calves
B1 and B2, C1 is the parent of B1 and B2). At the end of 4 years, he will have 5 animals (one parent cow C1, 3 offsprings of C1 
i.e. B1, B2, B3 and one offspring of B1).
"""

def main():
    testcount = input("")
    testcount = int(testcount)
    result = []
    for ind in range(testcount):
        offspring = dict()
        yearcount = int(input(""))
        offspring[1] = 1
        keycount = 1
        for year in range(yearcount):
            for key in list(offspring):
                if offspring[key] >= 2:
                    keycount += 1
                    offspring[keycount] = 1
                offspring[key] += 1  
        result.append(len(offspring))
    for item in result:
        print(item)

if __name__ == "__main__":
    main()
