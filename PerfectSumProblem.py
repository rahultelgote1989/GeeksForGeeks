import sys
from sys import stdin, stdout, stderr

def main():
    testcount = int(input(""))
    if not (testcount >= 1 and testcount <= pow(10, 5)):
        print("Test Count out of limit!")
        sys.exit(1)
    
    finallist = list()
    for test in range(1, testcount+1):
        lenlist = int(input(""))
        inputlist = list(input("").split(' '))
        totalsum = int(input(""))
        inputlist = [int(item) for item in inputlist]
        inputlist.sort()
        '''
        if not (lenlist >=1 and lenlist <= pow(10,5)):
            print("Length of the given array is out of limit!")
            sys.exit(1)
        for item in inputlist:
            if not(item >= 1 and item <= pow(10,5)):
                print("Values in the given array is out of limit!")
        
        if not(totalsum >= 1 and totalsum <= pow(10,5)):
            print("Given sum for the array is out of limit!")
            sys.exit(1)
            
        if lenlist != len(inputlist):
            print("Given length of the array does not match with the actual length of the array!")
            sys.exit(1)
        '''
        lenList = len(inputlist)
        count = 0
        for i in range(lenList):
            semisum = inputlist[i]
            if semisum == totalsum:
                count += 1
                
            for k in range(i+1, lenList):
                if (semisum + inputlist[k]) == totalsum:
                    count += 1
                if (semisum + inputlist[k]) < totalsum:
                    semisum = semisum + inputlist[k]
                if (inputlist[i] + inputlist[k]) == totalsum:
                    count += 1
            
        print(count)
    
if __name__ == "__main__":
    main()
