A = float(input())
B = float(input())
C = float(input())

if (A == 0) :
    if (B == 0) :
        print("goodbye")
    else :
        x1 = - C / B
        print("X1:%f"%x1)
else :
    D = B**2 - 4 * A * C
    if (D > 0) :
        x1 = (- B - D**0.5) / (2 * A)
        x2 = (- B + D**0.5) / (2 * A)
        print("X1:%f"%x1, "X2:%f"%x2)
    elif (D == 0) :
        x1 = - B / (2 * A)
        print("X1:%f"%x1)