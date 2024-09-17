print("cau")

import math
#from math import pi
def obsah_kruhu(r):
    s = math.pi*r**2
    return s
#r = float(input("r = "))
#(obsah_kruhu(r))


# new
def heron(a,b,c):
    s = (a + b + c) / 2
    S = (s*(s-a)*(s-b)*(s-c))**0.5
    return S
#strana_a = float(input("Strana a = "))
#strana_b = float(input("Strana b = "))
#strana_c = float(input("Strana c = "))
#print(heron(strana_a,strana_b,strana_c))
# print(heron(2, 2, 5)) trojuholnik sa neda zostrojit


#uhol alpha:

import math
#from math import acos
#from math import degrees
def uhol_alpha(a,b,c):
    cos_alpha = (-a**2+b**2+c**2)/(2*b*c)
    alpha_r = math.acos(cos_alpha)
    alpha = math.degrees(alpha_r)
    return alpha


#uhol beta:

def uhol_beta(a,b,c):
    cos_beta = (-b**2+a**2+c**2)/(2*a*c)
    alpha_rad = math.acos(cos_beta)
    alpha_d = math.degrees(alpha_rad)
    return alpha_d


#uhol gama:

def uhol_gama(a,b,c):
    gama = (-c**2+a**2+b**2)/(2*a*b)
    gama_rad = math.acos(gama)
    gama_d = math.degrees(gama_rad)
    return gama_d

strana_a = float(input("Strana a = "))
strana_b = float(input("Strana b = "))
strana_c = float(input("Strana c = "))
print(uhol_alpha(strana_a,strana_b,strana_c))
print(uhol_beta(strana_a,strana_b,strana_c))
print(uhol_gama(strana_a,strana_b,strana_c))

def pol_opisanej_k(a, sin_a):
    rad = math.degrees(sin_a)
    sin = math.sin(rad)
    r = a/(2*sin)
    return r
strana_ak = float(input("Strana a = "))
strana_uhol_a = float(input("Uhol a = "))
print(pol_opisanej_k(strana_ak, strana_uhol_a))
