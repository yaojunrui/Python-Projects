#hello.py
#print hello world to the console

thislist = ["apple","banana","cherry"]
if "apple" in thislist:
    print("Yes,'apple' is in the list")
    
del thislist[0]
print(thislist)

str1 = "AB"
print(len(str1))


num = 34323
bin_num = bin(num)
num = str(num)
print(num[0])
print(bin_num[2:])
# int type 转化成binary后变成string
print(type(bin_num))
#int 需要先转化成str才能用subscript和split

string = "The Dog Tail"
lsit = string.split()
print(lsit)
# split() 转化后需要再赋list
