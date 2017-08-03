
# coding: utf-8

# In[ ]:




# # ex1

# In[1]:

print("hello world")
print("hello again")
print("i like typing this")
print("This is fun")
print("Yay! Printing")
print("I'd much rather you 'not'.")
print("I 'said' do not touch this.")


# In[ ]:

#附加题
#1
print("hello world")
print("hello again")
print("i like typing this")
print("This is fun")
print("Yay! Printing")
print("I'd much rather you 'not'.")
print("I 'said' do not touch this.")
print("Let me print one more lines")

#2
print("Let me print a line only")
#3
#是声明注释的符号，表明该符号后同一行的内容都是注释，而非需要运行的代码。
#还可以用来暂时禁用一部分代码


# # ex2

# In[2]:

#A comment, this is so you can read your program later.
#Anything after the # is ignored byv python.

print("I could have code like this.") #and the comment after is ignored

#You can also use a comment to "disable" or comment out a piece of code:
#print("This won't run")

print("This will run")


# # ex3

# In[5]:

#打印一行文字
print("I will now count my chicken:")
#打印文字和计算结果
print('Hens', 25 + 30 / 6)
#打印文字和计算结果
print("'Roosters', 100 - 25 * 3 % 4")
#打印文字
print("Now I will count the eggs:")
#打印计算结果
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)
#打印文本
print("Is it true that 3 + 2 < 5 - 7?")
#打印逻辑判断的结果
print(3 + 2 < 5 - 7)
#打印文本和逻辑判断的结果
print("What is 3 + 2?", 3 + 2)
#打印文本和逻辑判断的结果
print("What is 5 - 7?", 5 - 7)
#打印文本
print("Oh, that's why it's False.")
#打印文本
print("How about some more")
#打印文本和逻辑判断的结果
print("Is it greater?", 5 > -2)
#打印文本和逻辑判断的结果
print("Is it less or equal?", 5 <= -2)


# In[6]:

#附加题
#2 由于电脑已经装了anaconda，于是直接使用jupyter当编辑器，没有下载gedit。后续练习均是使用jupyter写完代码，然后在terminal运行
#3
my_weight = 65
print("我的体重按市斤是:",weight * 2)
#4 #5在jupyter里和终端里运行是按浮点数计算的精确结果，当前版本默认了进行浮点数的精确计算


# # ex4

# In[11]:

#将一个名为cars的变量赋值为100
cars = 100
#将一个名为space_in_a_car的变量赋值为4.0
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print('There are', cars, 'cars available.')
print('There are only',drivers, 'drivers available.')
print("There will be", cars_not_driven, "empty cars today")
print('We can transport', carpool_capacity, 'people today')
print('We have', passengers, 'to carpool todat')
print('We need to put about', average_passengers_per_car, 'in each car.')


# In[18]:

#附加题
#1 不清楚是否有无必要，在我的电脑上无论是终端还是jupyter里，4和4.0的结果都没有区别
#2 浮点数是和定点数对应的概念，它是一种实数的表达方法，通过它可以有多个形式表达一个实数，实现更灵活的表示更大范围的实数。
#6
x = 3
print( x * 3)


# # ex5

# In[ ]:

my_name = 'Zed A. Shaw'
my_age = 35 #not a lie
my_height = 74 #inches
my_weight = 180 #lbs
my_eyes = 'blue'
my_teeth = 'White'
my_hair = 'Brown'


print("Let's talk about %s." %my_name)
print("He's %d inches tall." %my_height)
print("He's %d pounds heavy." %my_weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." %(my_eyes, my_hair))
print("His teeth are usually %s depending on the coffee." %my_teeth)
# this line is tricky, try to get it exactly right
print("If I add %d, %d, and %d I get %d." %(my_age, my_height, my_weight,
                                           my_age + my_height + my_weight))


# In[ ]:

#附加题
#1 2
name = 'Zed A. Shaw'
age = 35 #not a lie
height = 74 #inches
weight = 180 #lbs
eyes = 'blue'
teeth = 'White'
hair = 'Brown'


print("Let's talk about %r." %name)
print("He's %r inches tall." %height)
print("He's %r pounds heavy." %weight)
print("Actually that's not too heavy.")
print("He's got %r eyes and %r hair." %(eyes, hair))
print("His teeth are usually %r depending on the coffee." %teeth)
# this line is tricky, try to get it exactly right
print("If I add %r, %r, and %r I get %r." %(age, height, weight,
                                           age + height + weight))
#3
get_ipython().magic('c 转换成字符（ASCII 码值，或者长度为一的字符串）')
get_ipython().magic('r 优先用repr()函数进行字符串转换')
get_ipython().magic('s 优先用str()函数进行字符串转换')
get_ipython().magic('d / %i\t转成有符号十进制数')
get_ipython().magic('u 转成无符号十进制数')
get_ipython().magic('o 转成无符号八进制数')
get_ipython().magic('x / %X\t转成无符号十六进制数（x / X 代表转换后的十六进制字符的大小写）')
get_ipython().magic('e / %E\t转成科学计数法（e / E控制输出e / E）')
get_ipython().magic('f / %F\t转成浮点数（小数部分自然截断）')
get_ipython().magic('g / %G\t%e和%f / %E和%F 的简写')
%%	输出% （格式化字符串里面包括百分号，那么必须使用%%）

#4
inch = int(input())
print(inch * 2.54)

pound = int(input())
print("convert pound to kg:"pound * 0.454)



# # ex6

# In[18]:

x = 'There are %d types of people.' %10
binary = 'binary'
do_not = "don't"
#变量赋值 字符串包含字符串
y = "Those who know %s and those who%s." %(binary, do_not)

print(x)
print(y)
#字符串包含字符串
print("I said:%r." %x)
#字符串包含字符串
print("I also said: '%s'." %y)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
#字符串包含字符串
print(joke_evaluation %hilarious)

w = "This is the left side of ..."
e = "a string with a right side."

print(w+e)


# # ex7

# In[21]:

#打印文本
print('Mary had a little lamb')
print('Its fleece was white as %s.' %'snow')
print('And everywhere that Mary went.')
print('.' * 10) #what'd that do?

#赋值
end1 = 'C'
end2 = 'h'
end3 = 'e'
end4 = 'e'
end5 = 's'
end6 = 'e'
end7 = 'B'
end8 = 'u'
end9 = 'r'
end10 = 'g'
end11 = 'e'
end12 = 'r'

#使用+拼接字符串
#watch that comma at the end. try removing it to see what happens
print(end1+end2+end3+end4+end5+end6,)
print(end7+end8+end9+end10+end11+end12)


# # ex8

# In[23]:

formatter = '%r %r %r %r'

print(formatter %(1,2,3,4))
print(formatter %('one', 'tow', 'three', 'four'))
print(formatter %(True, False, False, True))
print(formatter %(formatter, formatter, formatter, formatter))
print(formatter %('I had this thing.',
                 'That you could type up right.',
                 "But it didn't sing.",
                 'So I said goodnight.'))


# In[ ]:

#加分题2
#单引号和双引号在没有互相包含的时候，都可以正常工作。如果一段文本中有多层引号的包含，那应该先用单引号、其次双引号，最后以及多行换行的时候用三引号。


# # ex9

# In[24]:

#Here's some new strange stuff,remember type it exactly.

days = 'Mon Tue Wed Thu Fri Sat Sun'
months = 'Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug'

print('Here are the days: ', days)
print('Here are the months:', months)

print("""There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.""")


# # ex10

# In[3]:

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass'''

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)


# In[ ]:

"I am 6'2\" tall." #将字符串中的双引号转义
'I am 6\'2" tall.' #将字符串中的单引号转义


# In[12]:

#附加题
#1
#2 三个单引号和三个双引号效果一样
#3
Aug = "August"
print("This month is \n%r" %Aug)


# # ex11

# In[2]:

print("How old are you?"),
age = input()
print("How tall are you?"),
height = input()
print("How much do you weigh?")
weight = input()
print("So, you're %r old, %r tall and %r heavy." %(age, height, weight))


# In[ ]:

#附加题
#1 input的作用是，接收用户在前台的输入内容


# # ex12

# In[3]:

age = input("How old are you")
height = input("How tall are you")
weight = input("How much do you weight?")

print("So, you're %r old, %r tall and %r heavy." %(age,height, weight))


# In[ ]:

#附加题
#1 pydoc的作用是打开python命令的说明文档，可以利用它来了解函数、命令的作用、用法、实例等等


# # ex13

# In[6]:

from sys import argv

script, first, second, third = argv

print("The script is called:"), script
print("Your first variable is:"), first
print("Your second variable is:"), second
print("Your third variable is:"), third


# In[ ]:

#附加题
#1 给三个以下的参数，系统会返回错误提示ValueError: not enough values to unpack (expected 4, got 3)
#这是因为脚本必须要给够三个参数（另外再加上脚本文件路径本身），才能执行保证四个变量都被赋值，从而使print函数都能正确执行


# # ex14

# In[13]:

from sys import argv

script, user_name = argv
prompt = '> '

print("Hi %s, I'm the %s script." %(user_name, script))
print("I'd like to ask you a few questions.")
print("Do you like me %s?" %user_name)
likes = input(prompt)

print("Where do you live %s?" %user_name)
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("""
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" %(likes, lives, computer))


# # ex15

# In[17]:

from sys import argv

script, filename =argv
#将打开文件赋值给变量txt
txt = open(filename)
#打印一段提示文字，并接上变量的内容（文件名）
print("Here's your file %r:" %filename)
#打印读取到的文件内容
print(txt.read())
print("Type the filename again:")
#不明白input括号里放“> "的作用
file_again = input("> ")
#将打开文件的动作赋值给变量txt_again
txt_again = open(file_again)
#打印文件里的内容
print(txt_again.read())


# # ex16

# In[ ]:

from sys import argv
script, filename = argv

print("We're going to erase %r." %filename)
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Now I'm going to ask you for three lines.")

line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()


# In[ ]:

#附加题3
target.write(line1 \nline2 \nline3)
target.write(%r %r %r %(line1, line2, line3))


# # ex17

# In[ ]:

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copying from %s to %s" %(from_file, to_file))

#We could do these two on one line too, how?
input = open(from_file)
indata = input.read()

print("The input file is %d bytes long" %len(indata))


print("Dose the output file exist? %r" %exists(to_file))
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input("")

output = open(to_file, 'w')
output.write(indata)

print("Alright, all done.")

output.close()
input.close()


# In[ ]:

#附加题3
open(to_file, 'w').write(open(from_file).read())


# # ex18

# In[ ]:

# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print("arg1: %r, arg2: %r" %(arg1, arg2))
    
# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print("arg1: %r, arg2: %r" %(arg1, arg2))
    
# this just takes one argument
def print_one(arg1):
    print("arg1: %r" %arg1)
    
# this one takes no arguments
def print_none():
    print("I got nothin'.")
    
print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()


# # ex19

# In[ ]:

#定义一个打印四条语句的函数，其中前面两句需要用到标准化变量，而变量则来自于函数所定义需要传入的参数
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("You have %d cheeses!" %cheese_count)
    print("You have %d boxes of crackers!" %boxes_of_crackers)
    print("Man that's enough for a party")
    print("Get a blanket.\n")

#打印双引号中的文本
print("We can just give the function numbers directly:")
#向函数传入20，30两个参数，获取函数的返回结果
cheese_and_crackers(20, 30)

#打印文本，命名两个变量，将两个变量作为参数传入两个函数
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
#将两个数值的加法运算作为参数传入函数
cheese_and_crackers(10+20, 5+6)

print("And we can combine the two,variables and math:")
#将数字和变量的加法运算作为参数传入函数
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


# # ex20

# In[ ]:

from sys import argv

script, input_file = argv

#这个函数的功能是，传入文件名，将文件内容读取和打印出来
def print_all(f):
    print(f.read())
    
#定位到文件开始的位置
def rewind(f):
    f.seek(0)
    
#这个函数的作用是，传入两个参数，一个行数，一个文件名，打印出文件指定行的内容
def print_a_line(line_count, f):
    print(line_count, f.readline())

#打开输入的文件
current_file = open(input_file)

print("First let's print the whole file:\n")

#读取打印所传入文件内容
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
#定位到文件所传入文件的开始位置
rewind(current_file)

print("Let's print three lines:")
#打印出第一行的内容
current_line = 1
print_a_line(current_line, current_file)

#打印出第二行的内容
current_line = current_line + 1
print_a_line(current_line, current_file)

#打印出第三行的内容
current_line = current_line + 1
print_a_line(current_line, current_file)


# # ex21

# In[ ]:

def add(a,b):
    print("ADDING %d + %d" %(a, b))
    return a + b

def subtract(a, b):
    print("SUBTRACTING %d - %d" %(a,b))
    return a - b 

def multiply(a, b):
    print("MULTIPLYING %d * %d" %(a, b))
    return a * b

def divide(a, b):
    print("DIVIDING %d / %d" %(a, b))
    return a / b

print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print("Age: %d, Height: %d, Weight: %d, IQ: %d" %(age, height, weight, iq))

# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print("That becomes:", what, "Can you do it by hand?")


# In[ ]:



