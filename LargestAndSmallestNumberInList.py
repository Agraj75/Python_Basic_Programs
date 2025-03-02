l=[]
size = int(input("Enter a Size of List: "))
for j in range(size):
    num=int(input("Enter a Number: "))
    l.append(num)
large = l[0]
small = l[0]
for i in l:
    if i>large:
        large = i
    if i<small:
        small = i
print("Largest No is: ",large)
print("Smallest No is: ",small)