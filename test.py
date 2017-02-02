from random import randint

print("Be careful not to fall off!")

i=0
for i in range(5) :
    if i==3:
        print("Now THREE!!!")
    i+=1
print(i)

for i in range(10):
    if i>7:
        print(i,randint(0,10))
    i+=1
    