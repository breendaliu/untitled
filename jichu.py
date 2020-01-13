
#s 数组Number
# print(2+2)

# 字符串String
print('c:\some\name')
# \n转义符  打印结果换行展示。 再加\后为转义回来。 加r表示原生
print('c:\some\\name')
print(r'c:\some\name')
print('py' 'thon')
# 用单引号或双引号时，不管中间有没有空格，都会连接起来
x='abc'
print('c:\\some\\name\\'+x)
# f 加{}，表示引用变量,上方易于加减乘除混合，影响展示效果，所以使用f和{}
print(f'c:\\some\\name\\{x}')
# format  传参
print('c:\\some\\name\\{}\\{}'.format(x, 123))
print('c:\\some\\name\\{y}\\{x}'.format(y=x, x=123))

# 列表 lists
s=[1, 4, 9, 16, 25]
# 切片或区间
print(s[1:3])
# append追加
s.append('a')
print(s)
s.append('b')
print(s)
# pop 弹栈,弹出最后一个值
s.pop()
print(s)

# deque 队列
from collections import deque
# 弹出左侧的字符
queue=deque(s)
queue.popleft()
print(queue)
#  再次弹出左侧的字符
queue.popleft()
print(queue)
x=[x*10 for x in range(10)]
print(x)

# 集合  {}+，组成  没有固定顺序
basket = {"apple", "orange", "pear", "apple", "orange"}   # 重复信息只打印一次
print(basket)
# 添加
basket.add("a")
print(basket)
basket2= {"apple","orange", "pear", "a", "b" }
basket.union(basket2)  #合并basket 与basket2
basket.intersection(basket2)  # 打印重复数据
basket.difference(basket2)  # 与第二集合重复的数据排除，只打印1中的不同的数据

# 元组  有固定顺序，不可修改， 可嵌套（包含另一元组）
t = 1, 2, 3
t = 1, 2, 3, (5, 6, 7)

# 词典
y={"q": 23, "apple":"iphone", 10:"xxx"}
print (y["q"])
# 遍历词典
for k, v in y.items():
    print(f"{k}:{v}")
# 遍历列表
for u in s:
    print(u)

# 遍历结构 for 变量 in 名

# for循环  for  in
# if 条件判断 if elif  else
# while循环
