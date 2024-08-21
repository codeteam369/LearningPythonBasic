#cách kiểm tra số tự nhiên trong python
def is_natural_number(n):
    if isinstance(n,int) and n > 0:
        return True
    else:
        return False

# Test the function with some examples
test_numbers = [5, -3, 0, 10, 2.5, 'seven']

for number in test_numbers:
    if is_natural_number(number):
        print(f"{number} is a natural number.")
    else:
        print(f"{number} is not a natural number.")



#hàm kiểm tra số người dùng nhập số phải số tự nhiên không
#vì kiểu dữ liệu người dùng nhập vào luôn là str(chuỗi)
def is_natural_number(input_str):
    try:
        num = int(input_str)#đưa kiểu dữ liệu người dùng về dạng int
        if num >= 1:
            return True
        else:
            return False
    except ValueError:#nếu xảy ra lỗi thì nó không phải là số tự nhiên
        return False
    
user_input = input("Nhập số tự nhiên: ")
if is_natural_number(user_input) == True:#== True không nhập cũng được
    print(user_input, "là số tự nhiên")
else:
    print(user_input, "Không phải là số tự nhiên")