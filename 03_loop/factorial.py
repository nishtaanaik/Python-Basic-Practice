#Write a program to calculate the factorial of a number using forloop

num=int(input("Enter a number:"))
factorial = 1
for i in range(num,0,-1):
    factorial = factorial *i
print(factorial)