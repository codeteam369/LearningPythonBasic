#In ra danh sách số từ 2000 đến 3000 chia hết cho 7 và không phải là bội số của 5(không chia hết cho 5)
list_j =[]
for i in range(2000,3000):
    if i%7 == 0 and i%5 != 0:
        list_j.append(str(i))
print("list is:")#list_j)

#Tính giai thừa của một số
factorial = int(input("Enter factorial: "))
def fact(factorial):
    if factorial == 0:
        return 1
    return factorial *fact(factorial-1)
print(fact(factorial))
