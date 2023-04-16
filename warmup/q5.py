total = 0
count = 0

while True:
  num = int(input())
  total += num
  count += 1
  if total == 0:
    break

print(count)
