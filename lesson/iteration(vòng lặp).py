#iteration là có nghĩa là sự lặp lại

print("Cách in từng dòng")
for i in range(3):
    print(i)

#Cách in ra danh sánh(kiểu tuple)
iteration = [x for x in range(5)]
print(iteration,"cách in theo kiểu tuple\n")

#nếu dùng ngoặc tròn cho vòng lặp thì kiểu dữ liệu là interator
#kiểu interator sẽ tạo cho ta một object được sử dụng như sau

iterator = (a for a in range(5))
print(iterator,"Sẽ in ra một chuỗi khó hiểu\n")

#Như nếu ta print(nxext(interator)) thì sẽ in ra phần tử đầu tiên
print(next(iterator),"là phần tử đầu tiên của iterator\n")

'''Và điều lưu ý là khi sử dụng iteration ta không thể gọi thẳng 
từng phần tử mà chỉ có thể gọi ra từng cái thông qua hàm next'''
#ví dụ print(iteration[1])
#khi ghi ra và khởi động chương trình sẽ bị lỗi

#Ta dùng sum để tính tổng các phần tử trong iteration
print("Tổng của iteration là",sum(iteration))
#Khi dùng hàm sum thì ta đã đưa con trỏ về cuối danh sánh vì thế ta sẽ không dùng hàm next được nữa

#Hàm max dùng để lấy ra giá trị lớn nhất trong list
print(max([9,3,8,4,7]),"là số lớn nhất của list")
#Khi ta gọi phần tử không có giá trị thì ta sẽ sài lệnh default=""
print(max([],default = "default value"))
#Hàm tìm giá trị nhỏ nhất là min cũng hoạt động như max

#Khi sắp xếp danh sách ta dùng hàm sorted()
list_a = [9,40,28,73]
print(sorted(list_a,"list_a sau khi đã được sắp xếp từ bé đến lớn"))
#Ta dùng reverse = True để đổi lại thứ tự sắp xếp
print(sorted(list_a, reverse = True),"List_a sau khi được sắp xếp từ lớn đến bé")

