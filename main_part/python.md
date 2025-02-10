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
`=`为赋值操作符w    assignment operator  
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
# 微实践 - 地球时间
