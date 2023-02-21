
fibonacci_series= 50
num1=0
num2=1
num3=0
while(num3<=fibonacci_series):
    num1=num2
    num2=num3
    num3=num2+num1
    if num3>fibonacci_series:
        break
    print(num3, end=",")



