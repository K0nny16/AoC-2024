from day2 import part1,part2

def test_part1():
    fp = "../input.txt"
    result = part1(fp)
    assert isinstance(result,int), f"Resultatet är inte ett tal! {result}"
    assert result > 0, f"Resultatet är inte större än 0: {result}"
    print(f"Antal safe reports är: {result}")

def test_part2():
    fp = "../input.txt"
    result = part2(fp)
    assert isinstance(result,int), f"Resultatet är inte ett tal! {result}"
    assert result > 0 , f"Resultatet är inte sörre än 0: {result}"
    print(f"Med ett tillåtet fel är resultatet: {result}")