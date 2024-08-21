#hàm lambda là một hàm ẩn danh nhỏ
#Ví dụ về hàm kiểm tra số chẵn
a = int(input("Nhập số chẵn:"))
kiểm_tra_số_chẵn = lambda a : a%2==0
print(kiểm_tra_số_chẵn(a))

#Ví dụ về hàm tính tổng hai số 
tính_tổng = lambda a,b : a+b
print(tính_tổng(9,6))

#ví dụ về sử dụng lambda function bên trong function
def hàm_mũ(i):
    return lambda n : i**n

hàm_mũ2 = hàm_mũ(2)
hàm_mũ3 = hàm_mũ(3)
hàm_mũ4 = hàm_mũ(4)

print(hàm_mũ2(3))