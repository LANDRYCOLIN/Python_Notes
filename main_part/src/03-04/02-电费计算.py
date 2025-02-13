# 电费计算：（期末读书 - 期初读书） * 单价

# 定义函数
def costCompute(iStart,iEnd):    #形式参数
    iConsume = iEnd - iStart
    return iConsume * 0.85

# 调用函数
fElecFee1 = costCompute(1201,1875)
fElecFee2 = costCompute(1875,2245)

# 输出结果
print("电费1：",fElecFee1)
print("电费2：",fElecFee2)