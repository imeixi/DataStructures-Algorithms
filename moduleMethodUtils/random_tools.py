import random

if __name__ == '__main__':
    # 随机生成[0.0, 1.0) 闭开区间内的浮点数
    f = random.random()
    print(f)

    # 浮点小数精确到后两位
    print(round(f, 2))  # (数值, 精度)

    # 生成指定范围(闭合空间)内的浮点数
    ff = random.uniform(2.5, 10.0)
    print(ff)
    print(round(ff, 2), '\n')

    # 整数用函数
    print(random.randrange(10))     # [0, stop)
    print(random.randrange(10, 12))     # [start, stop) 闭开区间
    print(random.randrange(10, 21, 3))  # [start, stop) step 闭开区间
    print(random.randint(0, 20))    # [0, 20]
    print(random.randrange(0, 21), '\n')    # [0, 20]
    # print(random.randbytes(2))

    # 序列用函数
    print(random.choice(['A', 'B', 'C']))
    print(random.choices(['red', 'black', 'green'], [18, 18, 2], k=6))
    # dealt = random.sample(['tens', 'low cards'], counts=[16, 36], k=20)  python 3.10 增加counts参数
    # 返回从总体序列或集合中选择的唯一元素的 k 长度列表。 用于无重复的随机抽样
    dealt = random.sample(['tens', 'low cards'], k=1)
    print(dealt)


