def read_input():
    with open('aoc2-1example.txt', 'r') as file:
    # with open('aoc2-1input.txt', 'r') as file:
        lines = file.readlines()
    return lines

def main():
    
    # list1 = []
    # list2 = []
    safeCount = 0
    direction = ""
    
    # Read the input file
    data = read_input()
   
    # Print contents to verify reading
    for line in data:
        splitLine = line.split()
        print(line.strip())
        print (splitLine)

        # list1.append(int(splitLine[0]))
        # list2.append(int(splitLine[1]))

    # print (list1)
    # print (list2)

    # list1.sort()
    # list2.sort()

    # print (list1)
    # print (list2)

    #     for i in range(len(splitLine)):
    #         gapSum += abs(list2[i] - list1[i])
    #         print(gapSum)

    # print(gapSum)


if __name__ == "__main__":
    main()