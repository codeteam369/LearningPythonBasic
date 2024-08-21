#Bài tập về boolean cơ bản
#kiểm tra xem số này có nằm trong khoảng (a;b) hay không
print('Chương trình kiểm tra số có nằm trong khoảng(a;b) hay không')
x = int(input("Nhập số cần xác định: "))
a = int(input("Nhập đầu mút trái: "))
b = int(input("Nhập đầu mút phải: "))

if a > b:
    print('Bạn phải nhập đầu mút trái lớn hơn đầu mút phải!')

if (x > a and x < b) == True:
    print(f'{x} nằm trong khoẳng ({a};{b})')
else:
    print(f'{x} không nằm trong khoẳng ({a};{b})')

#Nếu người dùng không biết hoặc cố tình nhập a > b thì sao?
