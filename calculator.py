number1 = input('Enter the num')
num1=int(number1)
sign=input('Enter the sign')
number2=input('Enter the number')
num2=int(number2)
if sign == '+':
    print('your result is ' +str(num1 +num2))
elif sign == '-':
    print('your result is' +str(num1 -num2))
elif sign == '*':
    print('your result is ' +str(num1 *num2))
elif sign == '/':
    print('your result is' +str(num1 /num2))
else:
    print('please enter +,-,*,/')
