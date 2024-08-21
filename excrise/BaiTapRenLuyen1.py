#Bài tập rèn luyện 1
#Bài tập viết chương trình in ra tất cả số nguyên tố < 100
#Số nguyên tố là số chỉ chia hết cho 1 và chính nó
for i in range(2,100):
    isPrime = True
    for j in range(2,i):
        if i % j == 0:
            print(j)
            isPrime = False
            break
    if isPrime:
        print(i)

#Bài tập tính giai thùa của một số
#giai thừa của một số là tích của tất cả các số < nó cho đến 0
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("Nhập số cần tính giai thừa:"))
print("Giai thừa của", n, "là", factorial(n))

#Viết chương trình tính tổng các số chẵn từ 1 đến n

def tính_tổng_số_chẵn(m):
    Tổng = 0
    for i in range(2,m+1,2):
        Tổng += i
    return Tổng

m=int(input("Nhập số m:"))
print("Tất cả các số chẵn từ 1 đến m là",tính_tổng_số_chẵn(m))