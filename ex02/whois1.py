num = input()
try:
    num = int(num)
    if num == 0:
        print("I'm Zero.")
    elif num % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

except:
    if len(num) == 0:
        print("Enter a number")
    elif len(num.split()) > 1:
        print("AssertionError: more than one argument are provided")
    elif num.isdigit() == False:
            print("AssertionError: argument is not an integer")
