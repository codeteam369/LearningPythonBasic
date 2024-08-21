#Hàm xuất trong python(nâng cao)
#khi ta gộp nhiều phần tử khác nhau vào trong hàm print thì python sẽ mặc định xuất các phần tử cách nhau bởi khoảng trắng
print('hello', 'Duy')

#Khi ta không muốn có khoảng trắng mà một kí tự khác thì ta dùng sep=""
print('hello', 'Duy', sep='')
print('hello', 'tay ninh', sep='+')
print(1,2,3,4,sep = '\n')

#Mỗi khi print một cái gì đó, python sẽ tự thêm \n vào vì thế khi ta print nhiều dòng kết quả sẽ tự xuống hàng
#Để loại bỏ chuyện đó ta dùng hàm end = ''
print('hoa-thanh', end='|')
print('tay-ninh')

#Cách dừng thời gian khởi chạy trong một khoảng nhất định
from time import sleep
print('bắt đầu trong 2 giây ')
print('Bắt đầu chương trình', sleep(2))

#Bộ nhớ đệm là bộ nhớ tạm thời trong python
'''Bản chất của print khi lưu dữ liệu vào bộ đệm muốn xuất dữ liệu từ bộ đệm ra thì phải có newline(dấu xuống hàng).
Nhưng nếu ta end bằng trỗng thì python chưa thấy được đấu \ để kết thúc việc xuất dữ liệu từ bộ đệm.
Vì vậy python sẽ lấy tiếp ở hàng có sleep và khi đụng lệnh sleep thì cả hai đều phải đợi(vì xuất cùng lúc)'''
#Ví dụ

print('Tây_Ninh\n','Long Trung' ,end = '')
print('Hòa Thành', sleep(3))

#Cách in thẳng dữ liệu ra file
with open(r'E:\learning python basis\product\example.txt','w') as f:
    print('how_Duy', file = f)

