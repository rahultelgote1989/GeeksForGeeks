
def main():
    result = []
    testcount = int(input(""))
    for test in range(testcount):
        instr1 = list(input("").strip())
        instr2 = list(input("").strip())
        highstr = ""
        lowstr = ""
        if len(instr1) > len(instr2):
        	highstr = instr1
        	lowstr = instr2
        else:
        	highstr = instr2
        	lowstr = instr1

        for char in lowstr:
        	if char in highstr:
        		highstr.remove(char)

        result.append(len(highstr))

    for i in result:
    	print(i)

if __name__ == "__main__":
    main()
