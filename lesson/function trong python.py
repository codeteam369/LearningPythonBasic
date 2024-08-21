#hàm là một từ khóa mà khi gọi ra các câu lệnh bên trong sẽ thực hiện
def frofile(name):
    print("Xin chào",name)
#trong ngoặc là đối số (biến của hàm) của hàm ta có thể truyền biến vào trong
#ví dụ tra truyền 'duy' vào trong ngoặc của hàm
print(frofile('duy'))
#một hàm có thể có nhiều đối số được cách nhau bởi dấu phẩy

#khi không xác định được đối số ta có thể dùng dấu sao(*) trước đối số
def môn_học(*môn):
    print("Môn học 1: " + môn[0])
    print("Môn học 2: " + môn[1])
môn_học("toán", "anh")

#ví dụ làm về một chương trình tính tổng
print("chương trình tính tổng:")
def tính_tổng(*giá_trị):
    tổng = 0
    for i in giá_trị:
        tổng = tổng + i
    print(tổng)
tính_tổng(9, 8)

#ta cũng có thể đặt vị trí theo string(chuỗi) trong hàm
print('cách đặt vị trí của đối số theo kiểu string')
def xin_chào(**tên):
    print("xin chào "+tên['name'])
xin_chào(name='Duy',surname='Nguyễn')

#return trong hàm
def tính_tích(*đối_số):
    tích = 1
    for i in đối_số:
        tích=tích*i

    return tích

tich1 = tính_tích(2,2)
tich2 = tính_tích(3,2)
print(tich1 + tich2)
#return sẽ trả về giá trị và ghi nhớ nó