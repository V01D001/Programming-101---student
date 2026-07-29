'''
momxmarebels sheayvaninet ori ricxvi da matematikuri operacia shemdeg gamoutanet pasuxi (ricxvi1 +-*/(is matematikuri operacia romelsac airchevs) ricxvi2)
'''

A = int(input("Type First Number: "))
Op = str(input("Choose operation (+, -, *, /): "))
B = int(input("Type Second Number: "))

if Op not in "+-*/":
    print("Please Start Over... Make sure to use CORRECT FORM of operation (+, -, *, /)")
elif Op == "+":
    print(A + B)
elif Op == "-":
    print(A - B)
elif Op == "*":
    print(A * B)
elif A == 0 or B == 0 and Op == "/":
    print("Can't devide by zero")
elif Op == "/":
    print(A / B)