import sys, math

w = int(input())
h = int(input())
t = input()
tParts = t.split()

mark_space = ""
firstChr = '*'
secChr = ' '
flag = True
for points in tParts:
    for count in range(int(points)):
        if flag:
            mark_space += firstChr
        else:
            mark_space += secChr
    flag = not flag

count = 0
for y in range(h):
    formated = ""
    formated += "|"
    for x in range(w):
        formated += mark_space[count]
        count += 1
    formated += "|"
    print(formated)