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
    direction = ""
    
    # Read the input file
    data = read_input()
   
    # Print contents to verify reading
    for line in data:
        splitLine = line.split()
        splitLine = [int(x) for x in splitLine]
        # print(line.strip())
        # print (splitLine)

        if splitLine[0] > splitLine [1]:
            direction = "dec"
        else:
            direction = "inc"

        safe = True

        for i in range(len(splitLine)-1):
            if direction == "dec" and splitLine[i] <= splitLine[i+1]:
                # print("dec fail")
                safe = False
                break
            elif direction == "inc" and splitLine[i] >= splitLine[i+1]:
                # print("inc fail")
                safe = False
                break
            elif abs(splitLine[i] - splitLine[i+1]) > 3:
                # print("gap fail")
                safe = False
                break
            
        if safe == True:
            safeCount += 1

    print(safeCount)


if __name__ == "__main__":
    main()