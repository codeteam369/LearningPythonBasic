#Bài 1/
#tìm ước số chung lớn nhất của a và b
#ước số chung là số mà a và b chia hết được cho số đó
#Đầu tiên ta xây dựng hàm

def uscln(a,b):#ước chung lớn nhất
    while(a!=b):
        if a > b:
            a = a -b
        if b > a:
            b = b - a
    return a 
print(uscln(7,5))
#ta thấy mục đích vòng lặp là:
#Đầu tiên là xem a và b có khác nhau không
#Nếu có lấy số lớn trừ cho số bé 
#Vòng lặp tiếp tục cho đến khi hai số bằng nhau

#Bài 2/
#Đầu tiên kêu người dùng nhập số n phần tử vào list
#Tạo vòng lặp kêu người dùng nhập cho đến khi n>=1

list_number = []
n = -1
while(True): 
    n=int(input("Nhập số lượng phần tử:"))
    if(n>=1):
        break
#hàm nhập
def nhap(n, list_number):
    for i in range(n):
        list_number.append(int(input("Nhập vào phần tử thứ " + str(i+1) + " ")))

def tính_tổng(list_number):
    tong = 0
    for x in list_number:
        tong += x
    return tong

nhap(n, list_number)
print("Tổng = " + str(tính_tổng(list_number)))