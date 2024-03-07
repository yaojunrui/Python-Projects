# coordinates = (4, 5)
# # tuple is immutable, once created, you can't change it

# list_of_coordinates = [(3,2), (3,6)]

# print(coordinates[1])

#判断string里的char是否都一样
def is_string_identical(text_string):
    # 此处编写代码
    text_list = list(text_string)
    for i in range(0, len(text_string)-1):
        if text_string[i] == text_string[i+1]:
            text_list[i+1] = text_list[i]
        else:
            return False
    new_text_string = ''.join(text_list)
    if new_text_string == text_string:
        return True
    else:
        return False
    
        

# 获取输入 
text_string = input()
# 调用函数 
print(is_string_identical(text_string))