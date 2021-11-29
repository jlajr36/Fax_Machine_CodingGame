import sys, math, os

#Make current dir working directory
os.chdir(os.path.dirname(os.path.realpath(__file__)))

file = open("test5.txt","r")
lines = file.readlines()

w = int(lines[0])
h = int(lines[1])
pattern = lines[2]
patternParts = pattern.split()

mark_space = ""
firstChr = '*'
secChr = ' '
flag = True
for points in patternParts:
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