def fibonacci_number(n):
    # 在此处编写你的代码
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib = [0, 1]
        for i in range(2, n + 1):
            next_fib = fib[i - 1] + fib[i - 2]
            fib.append(next_fib)
        return fib[n]

# 输入n的整数
n = int(input())
# 调用函数
print(fibonacci_number(n))