def p_div():
    a=float(input("enter the first number"))
    b=float(input("enter the second number "))

    try:
        result = a/ b
        print("Result:", result)
    except ZeroDivisionError as e:
        print("Error:", e)