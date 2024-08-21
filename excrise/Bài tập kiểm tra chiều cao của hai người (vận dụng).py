#kiểm tra chiều cao của hai người(vận dụng)
while True: #Luôn lặp lại khi True
    
    try: #Dự đoán phần gặp lỗi
        individual_a = float(input("enter height A:"))
        individual_b = float(input("enter height B:"))

    except ValueError: #cách giải quyết khi gặp lỗi
        print("you must enter number!")

    else: #Phần thực thi khi không gặp lỗi
        if individual_a > individual_b:
            print(f"individual A is {individual_a - individual_b} taller than individual B")
        elif individual_a == individual_b:
            print(f"Both are {individual_a} tall")
        else:
            print(f"individual A is {individual_b - individual_a} shorter than individual B")
            break  #thoát vòng lặp
