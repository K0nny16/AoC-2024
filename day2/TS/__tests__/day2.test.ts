import { part1 } from "../src/day2";

describe("Day 2 Part 1 AoC", () =>{
    it("Testar part 1", ()  =>{
        const fp = "../input.txt"
        const result = part1(fp)
        expect(result).toBeGreaterThan(0)
        console.log(`Safe reports ${result}`)
    })
})