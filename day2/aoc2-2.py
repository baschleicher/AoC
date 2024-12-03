def read_input():
    # with open('day2/aoc2-1example.txt', 'r') as file:
    with open('day2/aoc2-1input.txt', 'r') as file:
        lines = file.readlines()
    return lines

def main():
    
    # list1 = []
    # list2 = []
    safeCount = 0
    safe = False
    failCount = 0
    direction = ""
    
    
    # Read the input file
    data = read_input()
   
    # Print contents to verify reading
    for line in data:
        splitLine = line.split()
        splitLine = [int(x) for x in splitLine]
        # print(line.strip())
        print (splitLine)

        if splitLine[0] > splitLine [1]:
            direction = "dec"
        else:
            direction = "inc"

        safe = True
        failCount = 0
        i = 0
        j = 1

        while i < len(splitLine)-1:
            if direction == "dec" and splitLine[i] <= splitLine[j]:
                failCount += 1
                print("dec fail")
                print(failCount)

                if failCount > 1:
                    safe = False
                    break
                else:
                    j += 1
                    i = 0
                    
                # safe = False
                # break
            elif direction == "inc" and splitLine[i] >= splitLine[i+1]:
                failCount += 1
                print("inc fail")
                print(failCount)

                if failCount > 1:
                    safe = False
                    break
                else:
                    del splitLine[i+1]
                    print (splitLine)
                    i = 0

                # safe = False
                # break
            elif abs(splitLine[i] - splitLine[i+1]) > 3:
                failCount += 1
                print("gap fail")
                print(failCount)

                if failCount > 1:
                    safe = False
                    break
                else:
                    del splitLine[i+1]
                    print (splitLine)
                    i = 0
            else:
                i += 1

        if safe == True:
            safeCount += 1

    print(safeCount)


if __name__ == "__main__":
    main()