mod day1;
fn main() {
    let fp = "../input.txt";
    let result1 = day1::part1(fp);
    let result2 = day1::part2(fp);
    println!("Sim score: {}",result2);
    println!("Total distance: {}",result1)
}