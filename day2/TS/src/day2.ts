import fs from 'fs';

export function part1(filename: string): number {
    const reports: number [][] = fs.readFileSync(filename,'utf-8')
        .trim()
        .split('\n')
        .map(line => line.split(' ').map(Number))

    let safeCount = 0

    for(const report of reports) {
        //Räknar ut skillandne mellan nivåerna brevid varandra.
        const diffs = report.slice(1).map((level,index) => level - report[index])
        //Kollar så att skillnaden är mellan 1 och 3.
        const validDiffs = diffs.every(diff => Math.abs(diff) >= 1 && Math.abs(diff) <= 3)
        // Kontrollerar om rapporten är strikt stigande eller fallande
        // level: aktuellt element i arrayen
        // index: positionen för det aktuella elementet
        // arr: hela arrayen
        // Första elementet (index === 0) är alltid "sant", så vi börjar jämföra från andra elementet
        const strictlyIncreasing = report.every((level,index,arr) => index === 0 || arr[index-1] < level);
        const strictlyDecreasing = report.every((level,index,arr) => index === 0 || arr[index-1] > level);

        if(validDiffs && (strictlyDecreasing || strictlyIncreasing)) safeCount++
    }
    return safeCount
}
