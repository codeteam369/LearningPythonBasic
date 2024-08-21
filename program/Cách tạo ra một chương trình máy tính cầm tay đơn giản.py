#Bài tập làm một chương trình máy tính cầm tay đơn giản
import sympy as sp

def calculator():
    print("Welcome to the SymPy Calculator!")
    print("Type 'exit' to quit the calculator.")

    while True:
        expr = input("Enter your expression: ")

        if expr.lower() == 'exit':
            print("Goodbye!")
            break

        try:
            # Parse the expression using SymPy
            #phân tích biểu thức bằng sympy
            result = sp.sympify(expr)

            # Simplify the result
            simplified_result = sp.simplify(result)

            print(f"Result: {simplified_result}")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    calculator()
