import sys
from tabulate import tabulate

def operation(a, b):
    sum = a + b
    dif = a - b
    pro = a * b
    if b == 0:
        qou = "ERROR (division by zero)"
        rem = "ERROR (modulo by zero)"
    else:
        qou = a / b
        rem = a % b

    data = [["Sum:", sum],
            ["Difference:", dif],
            ["Product:", pro],
            ["Quotient:", qou],
            ["Quotient:", rem]]

    print(tabulate(data, tablefmt="plain"))


if __name__ == '__main__':
    if len(sys.argv) == 3:
        a = sys.argv[1]
        b = sys.argv[2]
        if a.isdigit() and b.isdigit():
            operation(int(a), int(b))
        else:
            print("AssertionError: only integers")

    elif len(sys.argv) > 3:
        print("AssertionError: too many arguments")
    else:
        print("AssertionError: enter 2 arguments")


