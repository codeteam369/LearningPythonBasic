#làm chương trình giải phương trình bậc hai(vận dụng)
while True:

    try:
        a = float(input("Nhập a:"))
        b = float(input("Nhập b:"))
        c = float(input("Nhập c:"))

    except:
        print("Bạn phải nhập vào số!")
        
    else:
        delta = b**2 - 4*a*c
        if delta < 0:
            print("Phương trình vô nghiệm")
        elif delta == 0:
            print("Phương trình có nghiệm kép là:")
            print(-b/2*a)
        else:
            print("Phương trình có hai nghiệm:")
            print("x1 =",(-b + delta**1/2)/2*a) #ta có căn delta = delta mũ 1/2
            print("x2 =",(-b - delta**1/2)/2*a) #số lũy thừa là số có a mũ n
            break
