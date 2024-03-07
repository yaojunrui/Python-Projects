def check_double_base_palindrome(number):
    decimal_str = str(number)  # 将数字转换为字符串形式
    binary_str = bin(number)[2:]  # 将数字转换为二进制字符串形式，并去除前缀 "0b"
 
    if decimal_str == decimal_str[::-1] and binary_str == binary_str[::-1]:
        return True
    else:
        return False


# 获取用户输入
number = int(input())

# 调用函数
print(check_double_base_palindrome(number))