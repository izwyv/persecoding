num = []
count = 0
while len(num) < 100:
  x = int(input())
  num.append(x)
  if x > 100 :
    count += 1
  if x < 0: 
    break 

print(count)
