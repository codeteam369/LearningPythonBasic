import sympy as sp

#Để hạn chế lặp lại cú pháp ta dùng def(tạo một chương trình con)
def get_derivative(equation_str):
    # Define the variable(định nghĩa biến)
    x = sp.symbols('x')
    
    # Parse the user input string into a SymPy expression
    #Thay đổi dữ liệu người dùng thành biểu thức bằng công cụ hỗ trợ của sympy
    equation = sp.sympify(equation_str)
    
    # Compute the derivative of the equation with respect to x
    #Tính đạo hàm của phương trình theo x
    derivative = sp.diff(equation, x)
    
    return equation, derivative

# Get user input
#Kêu người dùng nhập dữ liệu có biến x vào
equation_str = input("Enter the equation in terms of x: ")

# Compute the derivative
#Gọi hàm(chương trình con)
equation, derivative = get_derivative(equation_str)

# Print the original equation and its derivative
#Khởi chạy chương trình
print(f"Original equation: {equation}")
print(f"Derivative: {derivative}")

