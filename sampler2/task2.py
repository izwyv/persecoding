w = str(input())
n = int(input())

if len(w) == n:
  print("MATCH")
elif len(w) > n:
  print("MORE")
else:
  print("FEWER")
