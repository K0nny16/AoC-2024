from collections import Counter

def part1(file_path):
    left_list = []
    right_list = []

    with open(file_path, 'r') as file:
        for line in file:
            """
            Funktionen tar rad för rad och tarbort mellanslag för,efter och emellan siffrorna så detta:
            3  4
            2  1
            blir [3,4] och [2,1] och lägger till det första i vår "vänster" list och det andra i "höger" listan.
            """
            numbers = line.strip().split()
            left_list.append(int(numbers[0]))
            right_list.append(int(numbers[1]))
    
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)
    """
    Först delen av detta är att listorna zipas ihopa baserta på index så från exempelt ovan:
    Så är då 3 och 2 ett par och 4 och 1.
    Vi itererar sedan genom varje par i forloopen och kallar paret för left/right.
    Slutligen abs ger mig den absoluta skillnaden mellan 2 siffor(det vill säga att den bryr sig inte vilken av dom som är större)
    """
    distance = [abs(left - right) for left, right in zip (left_sorted,right_sorted)]
    return sum(distance)

def part2(file_path):
    left_list = []
    right_list = []

    with open(file_path, 'r') as file:
        for line in file:
            left_list.append(int(line.strip().split()[0]))
            right_list.append(int(line.strip().split()[1]))
        
        """
        Räknare för höger sidan. Bildar en frekvens tabell så att vi slipper loopa över hela settet och bara nummerna en gång.
        Som exempel right_list = [4,3,5,3,9,3]
        right_counter = Counter(right_list)
        print(right_counter) 
        Output: Counter({3:3,4:1,5:1,9:1})
        """
        right_counter = Counter(right_list)
        similarity_score = 0
        #
        for num in left_list:
            similarity_score += num * right_counter[num]

        return similarity_score
    