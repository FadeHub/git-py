import time
import support

support.print_func("赵书良")
print(ord('A'))
print(chr(66))

a = '''name = "zhaosan" age = "18" '''
print(a)
'''
123123
'''
#myname=input("请输入")
b = 'abcedefghijklmn'
print(b[::-1])
print(b[2:5:2])

time01 = time.time()
c = ""
for i in range(100000):
    c+="zsl"
time02 = time.time()
print("耗时为：" + str(time02-time01))


time03 = time.time()
li = []
for i in range(100000):
    li.append("zsl")
d=''.join(li)
time04 = time.time()
print("耗时为：" + str(time04-time03))

e = "我是{0}，年龄{1}"
f = e.format("赵书良",30)
print(f)
h = "我是{0}，存款为{1:*>100f}"
j = h.format("赵书良",3.234234)
print(j)

numbers = [12,23,34,42,53]
even = []
odd = []
while len(numbers) > 0:
    number = numbers.pop()
    if(number % 2 == 0):
        odd.append(number)
    else:
        even.append(number)
print(even)
print(odd)

for i in numbers:
    if (i % 2 == 0):
        odd.append(i)
    else:
        even.append(i)
print(even)
print(odd)

for i in "zhaoshuliang":
    print(i)