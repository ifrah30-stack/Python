a = int(input("Enter A: "))
b = int(input("Enter B: "))
c = int(input("Enter C: "))

if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)
