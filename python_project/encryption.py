'''
This program is an encryption, it will encrypte the string

print(chr(65)) #ASCII code -> character
print(ord("a")) #character -> ASCII code

'''

original_str = input("please input the string you want to encryte: ")

encryted_list = []

for i in range(0, len(original_str)):
    temp = chr(ord(original_str[i]) + 3)  # char after encryting
    encryted_list.append(temp)

encryted_str = "".join(encryted_list)

print(encryted_str)
