#Bài tập về boolean cơ bản
#kiểm tra xem số này có nằm trong khoảng (a;b) hay không

# 1/Kêu người dùng nhập số vào
print('Chương trình kiểm tra số có nằm trong khoảng(a;b) hay không')
x = int(input("Nhập số cần xác định: "))
a = int(input("Nhập đầu mút trái: "))
b = int(input("Nhập đầu mút phải: "))

# 2/Xử lí ngoài lề
#Nếu người dùng không biết hoặc cố tình nhập a > b thì sao?
if a > b:
    print('Bạn phải nhập đầu mút trái lớn hơn đầu mút phải!')

# 3/khởi xử lí dữ liệu
if (x > a and x < b) == True:
    print(f'{x} nằm trong khoẳng ({a};{b})')
if (x > a and x < b) == False:
    print(f'{x} không nằm trong khoẳng ({a};{b})')

#còn phải tạo vòng lặp while khi người dùng nhập sai nữa nhưng do khác phức tạp nên mình không làm ở bài này
#có thể coi cái tạo vòng lặp ở bài tập kiểm ta chiều cao của hai người
