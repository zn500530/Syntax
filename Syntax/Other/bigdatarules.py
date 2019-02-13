# -*- coding: utf-8 -*-

import random
import math
import matplotlib.pyplot as plt

TIMES = 50  # 赌博总数50次
BASE_MONEY = 100  # 本金100元


def test(p):  # p是赌资占资产的比例，在0-1之间
    money = BASE_MONEY  # 当前资产
    for i in range(1, TIMES):
        r = random.randint(1, 10)  # 在1-10中取随机数r
        val = money * p  # 计算本次赌资val
        if r > 3:  # 有70%的可能性r>3
            money += val  # 赢val元
        else:
            money -= val  # 亏val元
        if money <= 0:  # 如果输光，则提前出局
            money = 0.000001
            break
    return money / BASE_MONEY  # 此次操作的赢亏，>1为赢


for idx in range(0, 9):
    p = 0.1 * (idx + 1)  # 投资比例占总资产的比例为0.1,0.2...0.9
    plt.subplot(331 + idx)  # 设定做图位置
    array = []
    lose = 0
    for i in range(1, 100):  # 每个p值试验100次
        v = test(p)
        if v < 1:  # 亏本的次数
            lose += 1
        array.append(math.log10(v))  # 因数值跨度太大，以10底取对数
    print
    "percent ", p, ", lose ", lose
    plt.ylim(-1, 10)  # y轴坐标设定为-1到10做图
    plt.plot(array)
plt.show()