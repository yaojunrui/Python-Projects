def smallest_multiple(n): 
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    #定义最小公倍数
    def lcm(a, b):
        return a * b // gcd(a, b)
    # 初始化最小公倍数为1
    lcm_num = 1
    # 从1到n计算最小公倍数
    for i in range(1, n + 1):
        lcm_num = lcm(lcm_num, i)  # 使用最大公约数计算最小公倍数
    return lcm_num

# 输入n
n = int(input())
# 调用函数
print(smallest_multiple(n))