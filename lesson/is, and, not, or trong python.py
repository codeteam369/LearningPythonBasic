#giải thích về IS, AND, NOT, OR

# 1/Sự khác nhau giữa is và ==
Tèo = 17
Tí = 17
print(Tèo == Tí,'là so sánh hai giá trị với nhau (==)')
print(Tèo is Tí,'là định nghĩa tèo là tí (is)')

'''Ta có thể hiểu rằng tuy hai người có cùng một độ tuổi, chiểu cao, cân nặng,...
Nhưng ta không thể nói người này là(is) người kia mà chỉ nói người này bằng(==) người kia với một chỉ số nào đó.
Và trong python khi ta so sánh bằng lệnh is thì python sẽ lấy id của hai phần tử đó để so sánh.
Còn lệnh == thì so sánh giá trị '''

#_Ta thử in ip của tèo và tí
print(id(Tèo), 'là id của Tèo')
print(id(Tí), 'là id của Tí')
print(id("a"))
#_Qua trên ta đã thấy sự khác biệt về id

'''ID có thể hiểu là mã của một số, chuỗi, biến trong python.
Mỗi biến chỉ có duy nhất một mã và mã của mỗi biến khác nhau.
Như ID trong gane, ID thẻ học sinh, ID máy điện thoại'''

# 2/NOT, AND VÀ OR
left_value = True
right_value = False
print('use and',left_value and right_value)
print('use or',left_value or right_value)
'''
Qua ví dụ trên ta thấy khi dùng and thì cả hai giá trị là True chương trình mới trả ra True.
Còn với or thì dễ dàng hơn khi chỉ cần 1 giá trị True.
Nói chung nó giống như bản đúng sai của toán 
'''
#còn not thì sẽ chuyển từ True sang False và ngược lại
print(not right_value)

