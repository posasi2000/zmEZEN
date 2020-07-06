import math

A = float(input("A = "))
B = float(input("B = "))
C = float(input("C = "))

D = B * B - 4 * A * C
if A == 0:
    print ("x=", -C/B)
if D == 0:
    print ("x =", -B / (2.0 * A))
elif D > 0: 
    print ("x1 =", (-B + math.sqrt(D)) / (2.0 * A))
    print ("x2 =", (-B - math.sqrt(D)) / (2.0 * A))
else:
    print ("실근이 존재하지 않음")
