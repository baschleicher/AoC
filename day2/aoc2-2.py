from collections import Counter

def read_input():
    # with open('aoc1-1example.txt', 'r') as file:
    with open('aoc1-1input.txt', 'r') as file:
        lines = file.readlines()
    return lines

def main():
        
    list1 = []
    list2 = []
    simScore = 0
    
    # Read the input file
    data = read_input()
   
    # Print contents to verify reading
    for line in data:
        splitLine = line.split()
        # print(line.strip())
        # print (splitLine)

        list1.append(int(splitLine[0]))
        list2.append(int(splitLine[1]))

    # print (list1)
    # print (list2)

    list1.sort()
    list2.sort()

    # print (list1)
    # print (list2)

    list2Counter = Counter(list2)

    for i in range(len(data)):
        # simScore += abs(list2[i] - list1[i])
        simScore += list1[i] * list2Counter[list1[i]]
        # print(simScore)

    print(simScore)


if __name__ == "__main__":
    main()