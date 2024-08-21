try:
    with open(r"E:\learning python basis\product\output name.txt", "r") as file_text:
            name = file_text.readline().rstrip("\n")
            year_old = file_text.readline()
#vấn đề đã được giải quyết(do ghi sai)
# 1.chưa chuyển kiểu dữ liệu trong file output name về str được mà còn ở list
# 2.chưa chuyển year_old sang kiểu int được

    with open(r"E:\learning python basis\product\input.txt","w") as file_output:
        file_output.write(f"20 years from now, {name} age will be {int(year_old) + 20} ")


except:
    print("Invalid file format!")

#Cách truyền địa chỉ tuyệt đối trong python ta dùng chuỗi trần f""
#VD như hàng 2 và 9
#Muốn lưu nhanh file ta bấm control+s