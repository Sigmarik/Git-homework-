from useless import gcd

arr = [[2, 2, 2], [12, 18, 6], [5, 3, 1], [-12, 16, 4]]
for el in arr:
    if gcd(el[0], el[1]) != el[2]:
        _ = 12 / 0
