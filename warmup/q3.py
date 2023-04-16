a = int(input())
b = (a//8)*8
if a - b <= 4:
  print(b)
elif a - b > 4:
  print(b + 8)
else: 
  print(b)
