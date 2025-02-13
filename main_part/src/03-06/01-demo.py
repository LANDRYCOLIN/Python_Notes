sName = input("What's your name? ")
iAge = input("How old are you? ")   # input函数返回的是字符串类型
print(type(iAge))    # 打印变量的类型
iAge = int(iAge)    # 将字符串类型转换为整型
print(type(iAge))    # 打印变量的类型
print("Hello, " + sName + "! You are " + iAge + " years old.")