import re

def read_input():
    # with open('day3/aoc3-1example.txt', 'r') as file:
    with open('day3/aoc3-1input.txt', 'r') as file:
        lines = file.readlines()
    return lines

def main():
    
    list1 = []
    # list2 = []
    productSum = 0
    
    # Read the input file
    data = read_input()
   
    # Print contents to verify reading
    for line in data:
        list1 = re.findall(r'mul\([\d]{1,3},[\d]{1,3}\)',line)

        print(list1)

        cleanList1 = [x.replace('mul(','').replace(')','') for x in list1]

        print(cleanList1)

        for cleanPair in cleanList1:
            x, y = cleanPair.split(',')
            x = int(x)
            y = int(y)

            productSum += x*y

            # print(productSum)

        # print(productSum)

    print(productSum)


        # list1.append(int(splitLine[0]))
        # list2.append(int(splitLine[1]))

    # print (list1)
    # print (list2)

    # list1.sort()
    # list2.sort()

    # print (list1)
    # print (list2)

    # for i in range(len(data)):
    #     gapSum += abs(list2[i] - list1[i])
    #     print(gapSum)

    # print(gapSum)


if __name__ == "__main__":
    main()