import fs from "fs";

export function part1(filepath: string): number{
    const data = fs.readFileSync(filepath,"utf-8");
    const lines = data.trim().split('\n')
    const left: number[] = []
    const right: number[] = []
    for (const line of lines){
        /*
         * Splittar och stannar när det inte finns whitespace mer så när den når nästa siffra.
         * Sen konverterar jag string elementen till tal med map(Number) om det skulle varit något som inte är ett nummer i filen hade det kommit tillbaka som NaN eller på raden i detta fallet.
        */
        const [leftNum,rightNum] = line.split(/\s+/).map(Number);
        left.push(leftNum)
        right.push(rightNum)
    }
    /*
    * Sort hade jämför talen som strängar och inte sorterat dom korrekt.
    * Därför så specifiserar jag hur dom ska sorteras.
    * Så om listan är [3,1,4] så jämför den först 3 och 1 sedan 1 och 4
    * och eftersom att i det fösta exmpelet så blir det 3 - 1 som blir 2 och är positivt så flyttas 1 förre 3 osv (i detta fallet.) 
    */
    const leftSorted = [...left].sort((a,b) => a - b);
    const rightSorted = [...right].sort((a,b) => a - b);

    let totalDistance = 0;
    for (let i = 0; i < leftSorted.length; i++){
        totalDistance += Math.abs(leftSorted[i] - rightSorted[i])
    }
    return totalDistance
}

export function part2(filepath: string): number{
    const data = fs.readFileSync(filepath,"utf-8");
    const lines = data.trim().split('\n');
    const left: number[] = []
    const right: number[] =  []

    for(const line of lines){
        const [leftNumb,rightNumb] = line.split(/\s+/).map(Number);
        left.push(leftNumb);
        right.push(rightNumb);
    }
    const rightCounter = countOccurrences(right)
    let simScore = 0;
    for(const num of left){
        //Hämtar det ifall det finns och inte så ger vi det värdet 0.
        const occurrances = rightCounter[num] || 0;
        simScore += num*occurrances;
    }
    return simScore;
}
/*
* Funktion för att lägga ihopa talet och frekvensen av talet iform av en hashmap. Detta är vad Counter gör åt oss i python delen men det finns inte med i TS.
* Som exempel:
* const right = [4,3,5,3,9,3]
* const rightCounter = countOccurances(right);
* console.log(rightCounter) Ger outputen: {4:1,3:3,5:1,9:1}
*/
function countOccurrences(array: number[]): Record<number,number>{
    const counts: Record<number,number> = {};
    for(const number of array){
        counts[number] = (counts[number] || 0)+1;
    }
    return counts;
}