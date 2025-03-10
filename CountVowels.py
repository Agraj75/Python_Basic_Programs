k = input("Enter a String: ").lower() 
count = 0
vowels = {'a', 'e', 'i', 'o', 'u'}

for i in k:
    if i in vowels:
        count += 1

print("Vowels Count:", count)
