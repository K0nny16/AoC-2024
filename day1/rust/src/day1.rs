use std::fs;
use std::collections::HashMap;

pub fn part1(filepath: &str) -> i32 {
    //Läser in filen.
    let data = fs::read_to_string(filepath).expect("Kunde inte läsa filen");

    //Skapar vektorer för left och right. Använder Vector över Arc eftersom att detta ska inte delas över olika threads eller ägande.
    let mut left: Vec<i32> = Vec::new();
    let mut right: Vec<i32> = Vec::new();

    for line in data.lines() {
        let numbers: Vec<i32> = line
        .split_whitespace()
        //För varje num så konverterar vi det till ett heltal.
        .map(|num| num.parse::<i32>()
        .expect("Kunde inte parsa"))
        .collect();
        
        left.push(numbers[0]);
        right.push(numbers[1]);
    }
    left.sort_unstable();
    right.sort_unstable();

    /*
    * Itererar över den vänsta listan och slår sedan ihopa den med en iteration av högerlistan.
    * Mappar sedan över båda listorna l och r som jag kallar dom och räknar ut den absoluta skillnaden.
    * Summerar och returnerar det.
    */
    let total_distance: i32 = left
    .iter()
    .zip(right.iter())
    .map(|(l,r)|(l-r).abs())
    .sum();

    total_distance
}

pub fn part2(filepath: &str) -> i32 {
    let data = fs::read_to_string(filepath).expect("Kunde inte läsa filen!");
    let mut left: Vec<i32> = Vec::new();
    let mut right: Vec<i32> = Vec::new();

    for line in data.lines() {
        let numbers: Vec<i32> = line
        .split_whitespace()
        .map(|num| num.parse::<i32>().expect("Kunde inte parsa!"))
        .collect();
        
        left.push(numbers[0]);
        right.push(numbers[1]);
    }
    left.sort_unstable();
    right.sort_unstable();

    let mut right_counter: HashMap<i32,i32> = HashMap::new();
    
    for num in right {
        //Kollar ifall nyckel redan finns (nummert) ifall den inte gör det skapar den en nyckel med standard värdet 0 som sedan blir +1.
        *right_counter.entry(num).or_insert(0) += 1;
    }
    let mut sim_score = 0;
    for num in left {
        if let Some(count) = right_counter.get(&num){
            sim_score += num * count;
        }
    }

    sim_score

}