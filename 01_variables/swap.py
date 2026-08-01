# to swap values  using temp value
a= 4
b=5
temp= a
a=b
b= temp
print("a:",a)
print("b: ", b)

#without temp value
a=3
b=4
a,b =b,a
print("a:",a)
print("b: ", b)