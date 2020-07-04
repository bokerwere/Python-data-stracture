
def calculate():
    num1=float(input("enter number1:"))
    op=input("enter operator")
    num2 = float(input("enter number2:"))
    if op=="+":
        print(num1+num2)
    elif op=="-":
        print(num1-num2)
    elif op=="*":
        print(num1 *num2)

    elif op == "/":
        print(num1 / num2)
    else:
        print("invalid oparator")


calculate()