def rGcd(a, b):
  return a if b == 0 else rGcd(b, a%b)