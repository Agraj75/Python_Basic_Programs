start = int(input("Enter a number: "))
end = int(input("Enter a number: "))
if end<=1:
    print("not prime number")
else: 
    for i in range(start,end):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)