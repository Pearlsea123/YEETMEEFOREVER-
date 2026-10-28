#======================= Math =======================
print("======================= Math =======================")
print("Hi Lets do some maths! ")
import math
Num= float(input("Pick a decimal: "))
print("The florr and ceiling value of ", Num," is ", math.floor(Num), math.ceil(Num), "\n")
Copysign= int(input("Pick a negative number: "))
Copysign2= int(input("Pick a positve number: "))
print("Now we are going to find the copysign ofyour 2 number which is ", math.copysign(Copysign, Copysign2) )
print("Now we are going to find the positive value of your negative number and the negative value of your positive value! ", math.fabs(Copysign), math.fabs(Copysign2))
Gcd= int(input("Pick a positve number for GCD: "))
print("Now we are foing to find the GCD of both your positve numbers!", math.gcd(Copysign2,Gcd))
print("BYEEE")