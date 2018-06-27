#Q.1.write a program to print last n line of a file
f=open("test.txt")
content=f.readlines()
print(content)
f.close
n=int(input("enter the line number"))
while n>0:
    print(content[-n])
    n=n-1
#Q.2. write a program to read the frequency of word in a file
words=open("test.txt","r").read().split()
print(words)
print(type(words))
uniquewords=sorted(set(words))
print(uniquewords)
for word in uniquewords :
    print(words.count (word),word)

#Q.3 Write a Python program to copy the contents of a file to another file.
with open('test.txt','r') as f1:
    with open('test1.txt','w') as f2:
        for line in f1:
            f2.write(line)
            
#Q.4.write a python program to combineeach line from the list from first line with the corresponding line in second file........
with open('test.txt','r') as f1:
    with open('test1.txt','r') as f2:
        for line1,line2 in zip(f1,f2):
            print(line1+line2)
#Q.5- Write a Python program to write 10 random numbers into a file. Read the file and then sort the numbers and then store it to another file.

import random
with open('abc.txt','w') as f:
    for x in range(10):
        n = random.randint(1,9)
        f.write(str(n))
        f.write("\n")

with open('abc.txt','r') as f:
    numbers = f.readlines()

numbers.sort()

with open('test2.txt','w') as f:
    for n in numbers:
        f.write(n)
        f.write("\n")
