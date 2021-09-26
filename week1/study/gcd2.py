def gcd(a, b):
  while b:
    a %= b
    a, b = b, a
  return a

