a = 3.0
b = 7.0
c = 9.0

cos_c = (a**2 + b**2 - c**2) / (2* a * b)
cos_a = (b**2 + c**2 - a**2) / (2* b * c)
cos_b = (c**2 + a**2 - b**2) / (2* c * a)

print ("cosines a is: {}, cosines b is {}, cosines c is {}".format (cos_a , cos_b, cos_c))
