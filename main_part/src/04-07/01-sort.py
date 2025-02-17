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