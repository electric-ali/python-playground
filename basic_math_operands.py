#!/usr/bin/python3

print("Operation Menu:")
print("Addition: 1")
print("Substraction: 2")
print("Multiplication: 3")
print("Divison (Float): 4")
print("Division (Integer only): 5")
print("Exponentiation: 6")

while True:
    try:
        x = int(input("Type your operation number: "))
        if x < 1 or x > 6:
            raise ValueError #this will send it to the print message and back to the input option
        break
    except ValueError:
        print("Invalid integer. The number must be in the range of 1-6.")

m = int(input("First Number: "))
n = int(input("Second Number: "))


if x == 1:
    o=m+n
if x == 2:
    o=m-n
if x == 3:
    o=m*n
if x == 4:
    o=m/n
if x == 5:
    o=m//n
if x == 6:
    o=m**n

print ("Result: " + str(o))