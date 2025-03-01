num = int(input("Enter a Number: "))
temp = num
sum = 0

while num>0:
    rem = num%10
    sum = sum+rem*rem*rem
    num = num//10

if temp == sum:
    print(temp,"is an Armstrong Number")

else:
    print(temp,"is not an Armstrong Number")