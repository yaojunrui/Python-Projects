def find_highest_number(numbers_list):
    # 基本情况：如果列表只有一个元素，直接返回该元素
    if len(numbers_list) == 1:
        return numbers_list[0]
    
    # 递归情况：比较第一个元素和剩余元素的最大值
    max_rest = find_highest_number(numbers_list[1:])
    
    # 返回较大的值
    return numbers_list[0] if numbers_list[0] > max_rest else max_rest
# 输入数字并转为列表
numbers_list = list(map(int, input().split()))

# 调用函数打印结果
print(find_highest_number(numbers_list))