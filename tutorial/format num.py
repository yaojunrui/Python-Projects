#千位分隔符

# 定义函数
def add_commas(number):
    # 将数字转换为字符串
    txt = '{:,}'.format(number)
    return txt

# 获取用户输入
number = int(input())
# 调用函数
print(add_commas(number))