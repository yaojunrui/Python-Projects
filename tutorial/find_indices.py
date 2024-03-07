def find_indices(my_list, element):
    # 此处编写代码 
    tmp = []
    tag = 0
    for i in my_list:
        if i == element:
            tmp.append(tag)
        tag += 1
    return tmp

# split()函数将输入的字符串分割成一个列表
user_input = input().split()
element = input()

# 调用函数 
print(find_indices(user_input, element))