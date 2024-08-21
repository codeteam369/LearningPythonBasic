#bài tập tính tổng các dãy số nguyên tố
print("chương trình tính tổng các số nguyên tố")
user_input = input("Nhập dãy số cách nhau bởi khoảng trắng:\n")

#Đầu tiên ta lấy các giá trị cách nhau bởi dấu phẩy từ user_input ra bằng hàm split()
list_user = user_input.split()

#Sau khi lấy các giá trị ra, ta chuyển đổi giá trị thành số nguyên vì dữ liệu người dùng nhập vào mặc định là kiểu chuỗi
list_user = map(int,list_user)

#Tiếp theo ta dùng hàm sum để tính tổng các giá trị của dãy
total_list = sum(list_user)

#Cuối cùng là in ra màng hình
print("Tổng dãy số là:",total_list)