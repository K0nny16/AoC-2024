def part1(filename): 
    safe_count = 0

    with open(filename,'r') as file:
        for line in file:
            #Gär raden til en lista av siffror.
            report = list(map(int,line.strip().split()))
            #Räknar ut diffen på dom som är brevid varandra 
            diffs = [report[i] - report[i-1] for i in range(1,len(report))]
            #Kollar att skillnaden är mellan 1 och 3.
            #Jämför även med föregående
            if not all(1 <= abs(diff) <= 3 for diff in diffs):
                continue
            #Kontrollera att rpporten är antingen strikt stigande eller strikt fallande.
            #Strikt stigande: Varje tal är större än det föregånde
            #Strikt fallande: Varje tal är mindre än det föregånde
            if not (all(report[i] > report[i-1] for i in range (1,len(report)))or all (report[i] < report[i-1] for i in range(1,len(report)))):
                continue
            
            safe_count += 1

    return safe_count

def part2(filename):
    