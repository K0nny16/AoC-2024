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
    def is_safe(report):
        #Logiken för vad som är en godkänd rapport från del 1.
        diffs = [report[i] - report[i-1] for i in range(1,len(report))]
        if not all(1 <= abs(diff) <= 3 for diff in diffs):
            return False
        return(
            all(report[i] > report[i-1] for i in range(1,len(report))) or
            all(report[i] < report[i-1] for i in range(1,len(report)))
        )

    safe_count = 0

    with open(filename, 'r') as file:
        for line in file:
            report = list(map(int, line.strip().split()))
            # Kontrollera om rapporten är säker som den är
            if is_safe(report):
                safe_count += 1
                continue
            
            #       Brute-Force lösing
            # Testa om rapporten kan bli säker genom att ta bort en nivå
            # Går över varje tal i listan.
            # Slicear bort ett nummer varje gång och testar igen 
            for i in range(len(report)):
                modified_report = report[:i] + report[i+1:]
                if is_safe(modified_report):
                    safe_count += 1
                    break

    return safe_count