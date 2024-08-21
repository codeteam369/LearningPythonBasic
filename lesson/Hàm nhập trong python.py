#Hàm nhập trong python
#Hàm nhập luôn có kiểu giá trị là chuỗi cho dù ta nhập gì đi nữa
'''khi nhập ta nhập enter thì có nghĩa là ta đã kết thúc việc nhập dữ liệu
Và python sẽ không lấy kí hiệu enter trong input == \n'''

int_number = input("Nhập số vào:")
print(int_number,"có kiểu dữ liệu là" , type(int_number))

value = input('Enter value: ')
#hàm input có thể lưu lại giá trị bạn nhập vào 
print('first value is',value)

eval(input(prompt=None))
