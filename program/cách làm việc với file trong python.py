
#"x" là tạo file
#"w" là để ghi dữ liệu vào file(nếu file có rồi sẽ ghi đè)
#"a" ghi nối tiếp vào file(nếu file có rồi sẽ ghi tiếp)
#"r" là in từ file ra 
try:
    with open("example.txt","a") as f:
        f.write("hello the word:\n")
        f.close()
except Exception as e:
    print(e)
#lưu ý phải tắt tap mở lại mới được

try:
    with open("example.txt","r") as f:
            noidung = f.readline()
            print(noidung)
except Exception as e:
    print(e)