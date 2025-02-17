> Life is short, you need Python -- Bruce Eckel  
# C1.1 开篇-学习准备  
**本笔记的内容包括：**  
- Python编程语言  
- 简单的算法以及计算思维 - 排序、递归、分治  
- 与专业结合的案例，涉及数学、美术、文学、历史、信号处理、医学、经济学、游戏、科学计算、人工智能等...  
- 贯穿课程的工业实践经验，“优美、良好”的编程风格  
  
如何寻求帮助？-- [www.codelearn.club](www.codelearn.club)  

# C2.1-3 变量及简单数据类型-变量  
## 1. 导入
```python  
print("How beautiful my life is.")
#print 函数/function  y = x + 1
#参数/parameter
#变量/variable
n = 3
fPrice = 3.6
fAmont = n * fPrice
fMoney = fMoney - fAmont
sText = "我买了"  #字符串 string
print(sText,n,"斤苹果，每斤3.6元，一共花了",fAmont,"元。","还剩下",fMoney,"元")
```
`#`为注释，解释器忽略`#`后的该行  
`=`为赋值操作符（assignment operator）  
`print()`函数可以接受多个变量，每个变量之间自动添加空格  
  
## 2. 变量命名的要求
![](/main_part/001-变量命名要求.png "变量命名要求")

`keyword`为关键字
```python
import keyword
print(keyword.kwlist)   #可以打印Python中的所有关键字
```
  
这里介绍一个笔者的命名习惯，笔者认为以下的命名是正确并且好的命名（一般类似于匈牙利命名法）：
- iCount  
- sStudentNo  
- fPrice  
  
# C2.4 简单数据类型
数据类型（datatype）
- 整数 - int/integer  
- 浮点数 - float  
- 字符串 - str/string  
- 布尔型 - bool/boolean  
## 1. 导入
```python
# datatype 数据类型
n = 3
print(n, type(n))

#variable/变量 - object/对象
#datatype/类型 - class/类
```

## 2. Python中常见的数据类型
- `int`即为整数
- `float`为浮点数，**但是为什么要称为浮点数？**
![](/main_part/002-浮点数的存储格式.png "浮点数的存储格式")  
    - **浮点数的缺点**  
    ![](/main_part/003-浮点数2.png)  
    如果此时  
    ```python  
    if n == 14:     #条件语句
        print("0.14*100 == 14")
    else:
        print("0.14*100 <> 14")
    ```  
    等于比较在浮点数时会出现意外！  
- `bool`型为真假，有两值，分别为`False`、`True`  
    ![alt text](/main_part/004-布尔型.png)  
## 3. 数据类型的运算规则  
- `int`同`int`进行`/`以外的四则运算，结果是`int`  
- `int`同`int`进行`/`运算时，结果是`float`  
- 显然，`int`同`float`运算时，结果是`float`  
## 4. 字节
```python  
比特/bit    0/1  
字节/byte   - 8 bit  
1K bytes = 1024 bytes  
1M bytes = 1024 K bytes  
1G bytea = 1024 M bytes  
```  
## 5. 布尔型与整数的转换  
```python
print(int(True))
print(int(False))

#编译器输出结果
1
0
```
那么2是不是真呢？
```python  
if 3:
    print("True")

#编译器输出结果
True
```  
也就是说明整数`2`也为真  
我们可以知道结果，在Python中，**非0即真**
# C2.5 字符串  
- 字符串的格式  
- 转义字符  
- 大小写转换  
- 去除空格  
## 1. 字符串的格式  
- ***`print()`函数中字符串用`'`以及`"`均为合法字符串***  
但是
![alt text](/main_part/005-字符串.png)  
也就是当希望在字符串中包含`'`时，一般使用`"`包含；反之同理。否则会引起解释器混淆。  
![引号混淆](/main_part/006-引号混淆.png "引号混淆")  
  
## 2. 转义字符
- **但是我如果一定要这样写呢？**  
--需要使用转义字符"\"（反斜杠）  
```python  
print("I told you, \"Python is good\",\'It is terrific\'.")
```
![转义示例](/main_part/007-转义示例.png "转义示例")
  
- **如何在一段字符串再包含一个转义字符（反斜杠“\”）呢？**  
```python
print("When you need a \\ in string, put \\\\ in your code.")
```  
- 常用的转义字符
```python
\" = "
\' = '
\\ = \
\t = Tab #制表符，大致等于4个空格
\n = 换行符 #n for new line
```
示例[7]
（注意：从这里开始，笔者某些时候将不再在正文中展示示例代码的运行结果，所有编译的结果将以`demo.ipynb`中的示例编号的形式提醒）  
## 3. 大小写转换  
![](/main_part/008-title.png)
- `sName.title()`
  sName - 变量/Variable 对象/object  
  str   - 类型/Type     类/Class    存在"属性，值，行为，方法"
`.title()`是str类型的方法-method 或者 成员函数-member function  
- 其他的成员函数  
  ![](/main_part/009-str.png)  
- 为什么调用函数的形式不同？  
```python  
sName.upper()   .upper()函数它sName的成员函数
type(n)         普通函数，不属于任何对象
```  
## 4. 去除空格  
示例[10]  
![](/main_part/010-去除空格.png)  
```python  
sText = "           How beautiful my life is!           "
print("Output ly rstrip:", sText.rstrip(),"End")    #r for right    strip
print("Output ly lstrip:", sText.lstrip(),"End")    #l for left     strip
print("Output ly strip:", sText.strip(),"End")      #stirp all
```  
# C2.6 类型转换  
- `int()`  
- `float()`  
- `str()`  
## 实际演示  
![](/main_part/011-类型转换1.png)  
详细转换要求不再赘述，请读者自行领悟  
# P2-1 微实践-鸡兔同笼
> 《孙子算经》：今有雉兔同笼，上有三十五头，下有九十四足，问雉兔各几何？  
一般的解题思路：
1. 假设全部是鸡，余下的脚的数量 = 脚的数量 - 头数 * 2  
2. 兔子的数量 = 余下的脚的数量 / 2  
3. 鸡的数量 = 头数 - 兔子数量  
4. 验算：鸡的数量 * 2 + 兔子数量 * 4 = 脚的数量  
![](/main_part/012-鸡兔同笼1.png)  
## 1. 代码详解
```python
iHeads = 35   #头的数量
iFeet = 94    #脚的数量
a = iFeet - iHeads * 2
iRabbits = a / 2   # 兔子的数量
iChickens = iHeads - iRabbits   #鸡的数量
print(iFeet == iChickens * 2 + iRabbits * 4)
print("Number of chickens = %d," % iChickens, "Number of rabbits = %d" % iRabbits)
```
- `%d`是什么？--占位符（place holder）  
  `%d`由紧接之后的`% iChickens`十进制替换；同理，下一个%d一样  
# C3.1 语法初步 - 缩进  
***第三章简介***  
- 缩进  
- 操作符/运算符  
- 数值运算机器优先级  
- 函数及函数定义  
- 模块及乌龟画图  
- 获取用户输入  
- 占位符  
- 进制  
- 注释  
- 微实践 -- 地球时间  
- 微实践 -- 哈利波特之心灵感应  

**缩进 - Indentation**  
- 找茬 - 给一段代码找茬  
- 缩进语法  
# 1. 找茬
```python
message = “One of Python’s Strengths is its diverse community”
print(mesage）
```  
1. message - mesage  
2. `(`与`）`  
3. `“”`中文引号  

对初学者而言，这些都是很常见的错误！任何微小的错误，无论大小都会导致错误！  
**因此笔者在这里强烈建议在编程的时候将输入法切换为英文输入法！**
# 2. 缩进语法
```python
a = 103
if a > 100:
    print("a is bigger than 100.")  #Tab可以实现
    print("a line means nothing.")
else:
    pass  #占位语句，不可删除（会报错）

print("a is a integer.")
```  
缩进的两种实现：
1. Tab  
2. Ctrl + [, Ctrl + ]  
# C3.2 操作符或运算符
- 复合运算符  
- 整除与求模  
- 比较与逻辑  
## 1. 复合操作符  
```python  
a = 3
a = a + 2
print("a=",a)

b = 3
b += 2
print("b=",b)

#编译器输出
a= 5
b= 5
```  
- 此处可以说明，`b += 2`完全等价于`b = b + 2`  
- `+=`为复合运算符，除此之外，还有`-=`，`*=`，`/=`  
## 2. 整除与求模  
```python
a = 10 
b = a // 3    #整除
print("b=",b,type(b))

# 编译器输出
b= 3 <class 'int'>
```  
`//`为整除运算符，对商下取整
```python  
a = 10
c = a % 3   # % 求模
print("c=",c)

# 编译器输出
c= 1
```  
`%`为求模运算符
## 3. 比较与逻辑  
```python
a = 10
print("a>5:",a > 5)
print("a<20 and a>= 10:", a<20 and a >= 10)   # and 逻辑与
print("a!=3:",a != 3)                         # !=为不等于逻辑运算符
print("a > 100 or a<20:",a >100 or a < 20)    # or  逻辑或
print("not a >= 10:", not a>= 10)             # not 逻辑非

# 编译器输出
a = 10
print("a>5:",a > 5)
print("a<20 and a>= 10:", a<20 and a >= 10)   # and 逻辑与
print("a!=3:",a != 3)                         # !=为不等于逻辑运算符
print("a > 100 or a<20:",a >100 or a < 20)    # or  逻辑或
print("not a >= 10:", not a>= 10)             # not 逻辑非
```  
- `>`，`<`，`==`，`!=`，`>=`，`<=`均为逻辑运算符  
# C3.3 数值运算及其优先级  
- 先乘除，后加减  
- 通过括号调整优先级  
- **其余的明示比暗示好，建议以括号调整优先级**，笔者在这里不在赘述，感兴趣的可以自行了解  
# P3-1 微实践 - 地球时间  
- RTC计数为格林尼治时间1970年1月1日零时起，到现在总共流逝的滴答/Tick数  
- 计算机时间由RTC计数计算而来  
**本次实践的任务是通过自1970年1月1日零时起流逝的总秒数，计算现在的小时，分钟及秒数**  
## 1. 操作思路：  
1. 秒数 & 60 - 当前秒数；  
2. 秒数 // 60 - 总分钟数；  
3. 总分钟数 % 60 -当前分钟数；  
4. 总分数 // 60 - 总小时数；  
5. 总小时数 % 24 - 当前小时数；  
## 2. 操作  
```python  
#earthtime.py
import time  #导入一个叫做time的模块

curTime = time.time()  #从1970.1.1 0:0:0 -->现在经过的总秒数
print(curTime)
totalSeconds = int(curTime)
curSecond = totalSeconds % 60  #当前秒数
totalMinutes = totalSeconds // 60  #总分钟数
curMinute = totalMinutes % 60  #当前分钟数
totalHours = totalMinutes // 60  #总小时数
curHour = totalHours % 24  #当前小时数

print("现在是格林尼治时间",curHour,"时",curMinute,"分",curSecond,"秒")
print("从1970.1.1零时起到现在，经过了",totalSeconds,"秒")
```  
注意：这里采用RTC计数只是为了练习整除求模运算，实际获取当前时间可以采用以下代码更为简洁  
```python  
import datetime
curDate = datetime.datetime.now()  #当前的系统时间
print(curDate.year,"-",curDate.month,"-",curDate.day,"\n",\
    curDate.hour,":",curDate.minute,":",curDate.second)
print(type(curDate))
```  
- 其中第三行出现的`\`为续行符，用法不再赘述，请读者自行领悟  
# C3.4 函数及函数的定义  
- 现有函数的使用  
- 定义并使用新的函数  
## 1. 现有函数的使用  
```python  
# func.py

n1 = pow(2, 8)  #power 2**8
n2 = abs(-10)   #absolute value
n3 = round(7/2) #rounding

print("2^8 = ", n1)
print("abs(-10) = ", n2)
print("round(7/2) = ", n3)

#编译器输出
2^8 =  256
abs(-10) =  10
round(7/2) =  4
```  
- 在以上三个实例中，2、8为实参（当然也会存在形参）  
- 其中`round()`为四舍五入函数，但是当结果距离两个整数的距离一致（也就是x.5）时，Python默认返回偶数值  
##  2. 定义并使用新的函数  
1. 函数定义的语法  
```python  
def <函数名>(<形参列表>):
    <函数体>
    return <返回值列表>
```  
- 形式参数可以有0个到多个  
- 返回值也可以有0个到多个，当没有返回值时，return可以省略  
2. 电费计算实例函数
[电费计算.py](/main_part/src/03-04/02-电费计算.py)
```python  
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
```  
***注意：***
- 函数定义的本身并不会引起函数执行，当函数调用时才会执行函数  
- **为什么在这个实例中我们需要去定义一个函数？似乎也存在更简单方法？**  
    - costCompute抽象成函数以后，代码阅读者一看就知道这个函数是在计算费用，程序**可读性好**  
    - 世界运行规律变化才是主题，不变永远是特例；如果有一天要实施阶梯电价或者电价变更，只需要修改costCompute函数即可完成升级  
# C3.5 模块及乌龟画图  
- math模块的导入及使用  
- 使用turtle模块画图  
## 1. math模块的导入及使用  
```python  
# module.py

import math
print(math.floor(3.14))     #浮点数向下取整
print(math.ceil(3.14))      #浮点数向上取整
print(math.sqrt(16))        #开方

from math import floor, ceil, sqrt
print(sqrt(16))            #开方
```  
我们注意到，在两个`import`中，导入的谋爱调用函数时，调用方式不尽一致。  
- 前者调用为整体模块导入，在调用时需要强调所属类  
- 后者调用为直接将模块内的特定函数归入当前开发环境，已经为“我”的一部分，不需要强调`math.`  
- **但是一般不采用后者的简略写法，作为开发者应当尽可能的描述清楚，简略写法会污染名字空间**  
    - 例如，在sympy模块中也有一个名为`sqrt()`的函数，在同时使用时就会导致编译器误判  
## 2. 乌龟画图
```python
import turtle
t = turtle.Pen()    # Pen对象
iCirclesCount = 30
for x in range(iCirclesCount):   # 循环30次
    t.circle(100)
    t.left(360/iCirclesCount)
```
演示请读者自行运行，这里略过  
# C3.6 获取用户的输入  
- input()函数的使用  
- 示例程序演示  
```python  
sName = input("What's your name? ")
iAge = input("How old are you? ")   # input函数返回的是字符串类型
print(type(iAge))    # 打印变量的类型
iAge = int(iAge)    # 将字符串类型转换为整型
print(type(iAge))    # 打印变量的类型
print("Hello, " + sName + "! You are " + iAge + " years old.")
```  
# C3.7 占位符  
- 通过%进行字符串格式化  
- %d,%.2f,%s,%.1f  

**观察下面这个实例：**  
```python  
# 占位符
sName = "Mary"
fPrice = 125.75
n = 5
sText = "%s has %d lambs, each lamb worth $%.2f. So, these lambs worth $%.1f in total." % (sName, n, fPrice, n * fPrice)
print(sText)
```  
- `%s` - 字符串  
- `%d` - 十进制数  
- `%.2f` - 小数，2个小数位  
- `%.1f` - 小数，1个小数位  
# C3.8 进制  
- 二进制 - binary  
- 十进制 - decimal  
- 十六进制 - hexadecimal  
```python  
a = 0xff    #0x 表示16进制 hexa-decimal
b = 0b111   #0b 表示2进制 binary
print(a)
print(b)

aa = hex(a) #转化为十六进制
bb = bin(b) #转化为二进制

# 编译器输出
255
7
```  
***注意：***
- `0x`用于表示十六进制数；`0b`用于表示二进制数  
- 虽然存在不同进制的表示方法，但是需要注意的时是在计算机内部均以二进制存储数据  

**进制数的占位符**
`print("%x" % (255))`中`%x`表示十六进制数的占位符，同理`%b`表示二进制占位符  
# P3-2 微实践 - 心灵感应  
> 玩法：  
6张卡片上分别列出了一些60以内的整数。  
观众心中默想一个60以内的整数，写在纸条上，不告诉任何人。  
表演者将6张卡片呈现给观众看，观众如实回答每张卡片中是否包含那个数字。  
根据观众的回答，表演者“猜”那个数，仿佛掌握了“读心术”  

这里不详细介绍，读者感兴趣可以自行搜索这个实验，其中涉及二进制数的内容。  
# C3.9 注释  
## 单行注释  
`#`+注释内容  
## 多行注释  
```python  
"""
注释内容
"""
```  
## 一键注释  
选中多行注释内容后，按住`Ctrl`+`/`  
# C4.1 列表
> 出门买菜，最好带上篮子（容器）。这个容器既可以装鸡蛋，也可以装西红柿或者啤酒。人们很希望拥有这样一种容器，它可以装不同种类的对象，而且可以更具需要自动改变体积以适应需求。Python中的列表就是这样的容器。  

***下面是列表语法的基本用法：***
```python  
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
```  
**注意：**  
Python中负序号列表计数中，倒数第一个记为`-1`  
# C4.2 列表 - 元素的访问与修改  
```python  
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

months[3] = 4
```  
将列表中的第4个元素（编号为3的元素）修改为4  
此时列表中的元素不再是同一种类型（字符串和整数），这就是我们需要的**容器**。  
# C4.3 列表元素的增加  
## 1. `.append`  
```python  
#append.py
jack = ['10000', 'Jack Ma', 47]
jack.append("CEO")  #成员函数 方法
print(jack)

#编译器输出
['10000', 'Jack Ma', 47, 'CEO']
```  
也就是说，在上述的例子中`.append`这个成员函数可以在列表的末尾添加一个元素
**注意：** 此处使用单双引号没有特殊含义，均可表示合法字符串  
## 2. `.insert`  
```python  
jack.insert(1, 'Alibaba')  #插入
print(jack)
```
`.insert(a,b)`也为成员函数，意为在位置为`a`处添加元素`b`  
# C4.4 元素的删除  
```python
jack = ['10000', 'Jack Ma', 'male', 47, 'CEO']
del jack[2]   # delete
print(jack)

sTitle = jack.pop()  # 弹出
print(jack)
print(sTitle)
```  
在这一段代码中，我们采用了两种删除方法  
## 1. `del jack[2]`  
删除序号为`2`的元素  
## 2. `sTitle = jack.pop()`
- 在这里`.pop()`成员函数为弹出末尾元素并将该元素弹出给（赋值给）前置的变量  
- 其中`()`内可以添加需要弹出的元素序号  
# C4.5 列表的嵌套  
列表中可以容纳任何类型的元素，当然也可以容纳一个类型为列表的元素。  
```python  
# nesttedlist.py
jack = ['10000', 'Jack Ma', 'male', '47', 'CEO']
mary = ['10001', 'Mary Ma', 'female', '45', 'CFO']
tom = ['10002', 'Tom Ma', 'male', '20', 'CTO']
staff = [jack, mary, tom]
print(staff)
print(staff[0])
print(staff[0][1])

# 编译器输出
[['10000', 'jack Ma', 'male', '47', 'CEO'], ['10001', 'Mary Ma', 'female', '45', 'CFO'], ['10002', 'Tom Ma', 'male', '20', 'CTO']]
['10000', 'jack Ma', 'male', '47', 'CEO']
Jack Ma
```  
- 可以看出，`staff[0]`代表这个列表中的第0个元素，这个元素也就是一个名为`jack`的列表。而`staff[0][1]`代表jack列表中的序号为1的元素，姓名`jack Ma`  
- 我们可以将列表看作C/C++或者JAVA中的聪明的数组，而上述嵌套的列表可以视作二维数组  
# C4.6 名字绑定  
```python  
# 名字绑定 name binding
person1 = ['10000', 'Jack Ma', 'male', 47, 'CEO']
person2 = person1
person2[1] = "Tom Henry"
print(person1)
print(person2)

# 编译器输出
['10000', 'Tom Henry', 'male', 47, 'CEO']
['10000', 'Tom Henry', 'male', 47, 'CEO']
```  
我们看到，本来预期是修改person2列表中的序号1元素，但是发现person1中的元素也被修改，不符合预期结果。  
- 列表是一个对象（共用同一指针），所以person2与person1其实为列表的两个表示方法，也就是杜甫与杜子美的关系，这就是名字绑定  
- Python解释器这样做的原因我们可以这样理解，当采取操作列表`person2 = person1`时，列表`person1`的内容可能很大（尽管在例子中没有体现这一点），复制操作较为占用资源，于是进行了“浅复制”  
# C4.7 元素顺序  
```python  
# sort.py

names = ['jack', 'mary', 'tom', 'dorothy', 'peter']
names.sort()    #按照字母顺序排序
print(names)

names.sort(key = len)   #名字参数 按照字符串长度排序
print(names)    #长度相同并列时，无论那个在前都是可以的

scores = [82,66,66,93,24,15,77.8]
scores.sort(reverse=True)
print(scores)   #按照从大到小排序

scores.sort(reverse=False)
print(scores)   #从小到大排序

namesSorted = sorted(names) #sorted()函数返回一个新的列表,排序后的列表，这是一个新列表
print("names:",names)
print("namesSorted:",namesSorted)

# 倒序
names.reverse()  #倒序，使列表顺序颠倒
print(names)
```  
`.sort`等函数会导致列表修改（也就是顺序修改也是修改）  
# C4.8 for循环遍历  
```python  
#forloop.py

dummy = ['jacck',5,False,3.1415926,'mary',['A',"B"]]
for x in dummy:
    print(x)
    print(type(x))
    print('-----------------')

print("End of the loop")
```  
# C4.9 range数值列表  
## 1. 例1
```python  
print("output of range(5):")
for i in range(5):
    print(i)
# 编译器输出
output of range(5):
0
1
2
3
4

print("output of range(2,5):")
for i in range(2,5):
    print(i)
# 编译器输出
output of range(2,5):
2
3
4
```  
## 2. 例2  
```python  
x = range(5)
print(x)
print(x[2])
print(type(x))

#编译器输出
range(0, 5)
2
<class 'range'>
```  
从这些例子中我们可以发现range数列，