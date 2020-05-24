def gcd(a, b):
    return gcd(b, a % b) if b != 0 else a
