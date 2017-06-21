import sys
from sys import stdin, stdout, stderr

def genIP(ipstr):
    finalips = []
    tempip = ""
    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                for l in range(1,4):
                    if (i+j+k+l) == len(ipstr):
                        firstPart = ipstr[:i]
                        secondPart = ipstr[i:i+j]
                        thirdPart = ipstr[i+j:i+j+k]
                        fourthPart = ipstr[i+j+k:]
                        tempip = firstPart + "." \
                                 + secondPart + "." \
                                 + thirdPart + "." \
                                 + fourthPart
                        checkin = True
                        for ippart in tempip.split('.'):
                            ipp = int(ippart)
                            if (ipp < 1) or (ipp > 255):
                                checkin = False
                        if checkin:
                            finalips.append(tempip)
    return finalips    

def main():

    testcount = input("")
    testcount = int(testcount)
    if not (testcount >= 1 and testcount <= 100):
        print("Test Count out of limit!")
        sys.exit(1)
    
    for test in range(testcount):
        ipstr = input("")
        if len(ipstr) < 4 or len(ipstr) > 12:
            print("Invalid IP Address string provided!")
            sys.exit(1)
        finalips = genIP(ipstr)

    for ipadd in finalips:
        print(ipadd)


if __name__ == "__main__":
    main()
