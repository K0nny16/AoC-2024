import { part1,part2 } from "../src/day1";

describe('Part 1 Day 1 AoC', () => {
    it('Kollar integreteten av funktionen', () => {
        const fp = "../input.txt"
        const result = part1(fp)
        expect(result).toBeGreaterThan(0);
        console.log(`Total distance: ${result}`)
    })
})

describe("Part 2 Day 1 AoC ",() => {
    it("Kollar integreteten av funktionen", () => {
        const fp = "../input.txt"
        const result = part2(fp)
        expect(result).toBeGreaterThan(0);
        console.log(`Similarity Score: ${result}`)
    })
})