old_number = 0
even_number = 0
number = float(input("enter number or type 0 to stop:"))
while number != 0:
    if number % 2 == 1:
        old_number += 1
    else:
        even_number += 1

    number = float(input("enter number or type 0 to stop:"))

print("even:", even_number)
print("old", old_number)
