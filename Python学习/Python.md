# 1. 初识Python  
## 1.1 编写一个简单的程序
```Python  
print(1234)#在屏幕上打印1234
print("今天天气不错")
#在屏幕上打印今天天气不错
```  
## 1.2 在Python中，代码通过缩进来区分代码之间的层次
例如：
```Python  
for i in range(0,10):
    print("今天天气真不错")
```  
**通常四个空格或者一个`Tab`代表一个缩进**  
# 2. 变量与赋值、交换  
***开发一个Python程序，交换两个变量的值***  

**变量：** 数据的名字，存放数据的地方  
**变量命名的规则：**
1. 只能由大小写字母以及数字、下划线组成，第一个字符不得为数字  
2. 不能与Python语言本身使用的名称相同  
  
    ![Python保留字](/Python学习/Python保留字.png "Python保留字")  
  
- 变量赋值使用`=`，如`name = python`就是将`python`赋值给`name`  
- `input("")`函数可以输入值
- 交换变量的值需要使用**中间变量**存储
    - 例如
        ```python
        glass1 = input("请输入杯子1中的饮料：")
        glass2 = input("请输入杯子2中的饮料：")
        temp = ""

        print("交换前各杯子的情况")
        print(glass1)
        print(glass2)
        
        temp = glass1
        glass1 = glass2
        galss2 = temp

        print("交换后各杯子的情况")
        print(glass1)
        print(glass2)
        ```
        