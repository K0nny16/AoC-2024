from day2 import part1

def test_part1():
    fp = "../input.txt"
    result = part1(fp)
    assert isinstance(result,int), f"Resultatet är inte ett tal! {result}"
    assert result > 0, f"Resultatet är inte större än 0: {result}"
    print(f"Antal safe reports är: {result}")