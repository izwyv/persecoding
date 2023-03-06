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


# or 

number1 = int(input())
sign = input()
number2 = int(input())
if sign == "*":
    print(number1 * number2)
elif sign == "+":
    print(number1 + number2)
