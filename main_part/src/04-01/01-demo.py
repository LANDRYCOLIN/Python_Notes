# 列表
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']# 12个元素 elements

print(type(months)) 
# <class 'list'> 是一种容器 container

print(len(months)) 
# length 12 用于返回列表的元素数量，也叫列表的长度

print(months[0],months[3]) 
# January,April 通过索引 index 访问列表的元素。在大多数编程语言中，索引一般都是从0开始

print(months[12])
# 超出索引范围会报错 IndexError: list index out of range

print(months[-1],months[-3])
# December,October 负数索引表示从列表的末尾开始计数