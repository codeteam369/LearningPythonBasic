#Bài tập chuyển từ số thập phân sang bát phân
decimal_number = int(input("enter decimal number: "))
octal_number = oct(decimal_number)[2:]
print(f"decimal number {decimal_number} in octal number is {octal_number}")

#Bài tập làm tròn số từ a đến b
a = float(input("enter a :"))

try:
    b = int(input("enter decimal place b :"))
except ValueError:
    print("You must enter b as a natural number because it is ordinal")
    b = int(input("enter b must natural munber:"))

c = round(a,b)
print(f"number {a} after being rounded to the decimal place {b} là",c)