def divisor(a):
  return [x for x in range(1, a+1) if a % x == 0]

def normal_divisor1(a):
  arr = set()
  for i in range(1, int(a ** 0.5)+1):
    if a % i:
      continue
    arr.update((i, a//i))
  return list(arr)

def normal_divisor2(a):
  arr = set()
  for i in range(1, a):
    if a % i:
      continue
    arr.update((i, a//i))
  return list(arr)