age = str(input())
if len(age) <= 3:
  char_symbol = input()
  c = len(char_symbol) 
  while c <= len(age)+ 2: 
    print(char_symbol, end='')
    c += 1

print()
print(char_symbol, age, char_symbol, sep='')

c = len(char_symbol) 
while c <= len(age)+ 2: 
  print(char_symbol, end='')
  c += 1
