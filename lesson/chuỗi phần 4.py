'''Giải thích về chuỗi phần 4'''
#Cách viết in chữ đầu của chuỗi 
a = "variable"
b = a.capitalize()
print(b)

#Cách viết in toàn bộ chuỗi
print(a.upper())

#cách viết thường toàn bộ
print(a.lower())

#cách đảo ngược hoa với thường
c = "Word"
print(c.swapcase())

#Cách viết in chữ đầu của mỗi từ (title)
print(a.title()) 

#Cách canh chuỗi nằm giữa khoảng cách khoảng cách
print(a.center(30,"_"))
#30 là số khoảng trống hiểu thị
# _ là từ hiển thị hai bên biến a(chỉ được tối đa có đọ dài là 1)

#Cách canh chuỗi nằm phải
print(a.rjust(30,"_"))

#Cách canh chuỗi nằm trái
print(a.ljust(30,"_"))

#Cách cộng tuần tự chuỗi bằng join
print(c.join(["1","2","3"]))

#thay thế một chuỗi bằng chuỗi khác
print(a.replace("a","v"))
#Ta dã thay thế từ a bằng từ v

