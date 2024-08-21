try:#dùng để dự đoán và đặt đoạn nghi xảy ra lỗi
    a = int(input("Nhập vào số nguyên a: "))
    print(str(a) + f" + {a} = ",str(a+a))

except Exception as e:#thực thi khi lỗi xảy ra
   print("Nhập dữ liệu không chính xác: ",e)

else:#thực thi khi lỗi không xảy ra
    print("Không có lỗi xảy ra!")

finally:#luôn thực thi khi có và không có lỗi
    print("chương trình kết thúc")