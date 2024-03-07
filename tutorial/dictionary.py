def get_sorted_keys_values(dict_obj):
    # 获取字典的键，并按字母顺序排序
    sorted_keys = sorted(dict_obj.keys())

    # 使用排好序的键来获取对应的值
    sorted_values = [dict_obj[key] for key in sorted_keys]

    # 返回由两个列表组成的列表
    return [sorted_keys, sorted_values]


# 获取用户输入转为字典
dictionary = eval(input())

# 调用函数
print(get_sorted_keys_values(dictionary))

