import random
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
a = 0
length = int(input("Enter the length of your password:"))
if length%2 == 0:
    num = length/2
    for i in range(int(num)):
        a = random.choice(alpha)
        print(a, end = '')
    for i in range(int(num)):
        print(random.randint(0,9), end = '')
else:
    num = length/2
    x = int(num)
    el = length-x
    for i in range(x):
        a = random.choice(alpha)
        print(a, end = '')
    for i in range(el):
        print(random.randint(0,9), end = '')