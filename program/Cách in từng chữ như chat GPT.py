#Cách in từng chữ như chat GPT
from time import sleep

your_great = 'hello! My name is '
your_name = input("nhập tên của bạn: ")

for c in your_great + your_name:
    print(c, end = '', flush = True)
    sleep(0.1) #Thay đổi thời gian xuất hiện của chữ ở đây

#flush dùng để lấy dữ liệu từ bộ nhớ đệm ra ngay lập tức
