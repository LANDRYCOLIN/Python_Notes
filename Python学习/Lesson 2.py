glass1 = input("请输入杯子1的内容：")
glass2 = input("请输入杯子2的内容：")
temp = ""

print("Before:")
print(glass1)
print(glass2)
        
temp = glass1
glass1 = glass2
glass2 = temp

print("After:")
print(glass1)
print(glass2)