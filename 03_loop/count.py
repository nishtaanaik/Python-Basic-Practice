#Write a program to count how many even numbers are between 1 and 20.

num = 0
for i in range(1,21):
    if i % 2 ==0:
        num = num +1
print(num)