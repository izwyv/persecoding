#Q5
a = int(input())            
operator = input().strip()    
b = int(input())             

if operator == '+':
    result = a + b            
elif operator == '*':
    result = a * b            
else:
    print("Invalid operator")
    exit()                    

print(result)
