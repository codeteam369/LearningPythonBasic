'''KIỂU DỮ LIỆU BOOLEAN TRONG PYTHON'''
# 1/kiểu boolean có hai giá trị True hoặc False:
#Khi ta truyền vào hai phần tử và có toán tử so sánh ở giữa thì python sẽ tự động so sánh cho ta
a = 3
b = 1
print('a < b là',a < b)


# 2/Thứ tự ưu tiên của python khi khởi chạy chương trình
'''
1. Dấu ngoặc

2. toán tử số học
    + cộng các giá trị lại với nhau 
    - trừ các giá trị lại với nhau
    * nhân các giá trị lại với nhau
    / chia các giá trị cho nhau
    // chia làm tròn
    % chia lấy dư
    ** lũy thừa(toán tử mũ)

3. Toán tử so sánh
    == so sánh hai giá trị có bằng nhau không
    > so sánh giá trị này lớn hơn giá trị kia
    >= so sánh giá trị này lớn hơn hoặc bằng giá trị kia
    < so sánh giá trị này bé hơn giá trị kia
    <= so sánh giá trị này bé hơn hoặc bằng giá trị kia
    != so sánh giá trị này không bằng giá trị kia
'''
#ví dụ
print("example",(8 + 2) * 2 == 20)
#_Qua ví dụ trên ta thấy python đã ưu tiên dấu ngoặc trước, là tới toán tử số học, và cuối cùng là toán tử so sánh


# 3/So sánh các chuỗi với nhau
print('string giống nhau','duy' == 'duy')
print('string khác nhau', 'duy' == 'teo')

'''Khi so sánh hai chuỗi với nhau python sẽ đưa chúng về dưới dạng ASCII về số thập phân.
ASCII có thể hiểu là bảng chuyển đổi kí tự trên bàn thành ba hệ: nhị phân ,thập phân, thập lục phân.
Trong python thì lấy hàng thập phân để so sánh'''

#Ta có thể sử dụng hàm ord() để xem kí tự của mình ở bản ASCII ở dạng thập phân là ở thứ mấy
print('space là kí tụ thứ',ord(' '), 'ở hàng thập phân')
print('a là kí tự thứ', ord('a'), 'ở hàng thập phân') #

#?_Khoang đã nếu như so sách sự lớn bé của hai chuỗi thì tại sau a < A là False?
'''Như mình đã nói về phần kiểu ASCII ở trên thì python sẽ dựa theo thứ tự của bản đó ở phần thập phân mà so sánh.
Python sẽ dùng ord() của từ phần tủ để so sánh với nhau'''
#ví dụ
print('ord của a là',ord('a'))
print('ord của A là',ord('A'))
print('Suy ra ord của a < A là', 'a' < 'A')

#_Còn chuỗi có nhiều hơn hai kí tự thì sao
'''Nếu như chuỗi có nhiều hơn hai kí tự thì python sẽ so sánh từ kí tự cùng vị trí với nhau.
Ví dụ aaa với Aaa thì ở vị trí đầu tiên a > A. 
Và sau khi có sự khác biệt thì python sẽ lấy luôn kết quả của hai số đó cho cả chuỗi mà không xét tiếp các phần tử còn lại'''
#_Ví dụ
print("aaa" > 'abc')


# 4/Sự khác nhau giữa is và ==
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

# 4/NOT, AND VÀ OR
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


# 5/Các giá trị đều là boolean(Tức là đều có True hoặc False)
'''
Tất cả các giá trị đều là True trừ:
    _Số 0
    _None
    _Rỗng
'''
print('boolean 0 là',bool(0))
print('boolean None là',bool(None))
print('boolean rỗng là', bool(''), 'Bao gồm cả list, dictionary, tuple, set')

#Muốn xem bài tập thì qua file bài tập boolean cơ bản