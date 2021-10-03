def gcd(a, b):
  res = 0
  while b:
    res = a % b
    a = b
    b = res
  return a