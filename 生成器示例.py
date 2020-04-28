
# coding: utf-8

# ## python高级语法——生成器
# 
# ### Fiona
# ### 1759667545

# In[ ]:


# 生成一个由1-20这20个数字的平方组成的列表
num_list=[]

for i in range(1,21): #range(1,21)=[1,2,3,...,20]
    num_list.append(i**2)
print(num_list)


# In[ ]:


num_list2=[i**2 for i in range(1,21)]
print(num_list2)


# In[ ]:


# generator  生成器
gen=(i**2 for i in range(1,21))
print(gen)


# In[ ]:


print(next(gen))


# In[ ]:


print(next(gen))


# In[ ]:


for g in gen:
    print(g)


# In[ ]:


print(next(gen))  #抛出异常


# In[ ]:


# yield
def odd():
    print('第一个奇数')
    yield 1
    print('第二个奇数')
    yield 3
    print('第三个奇数')
    yield 5
num=odd()   #生成器函数的调用返回了一个生成器对象
print(type(num))


# In[ ]:


next(num)


# In[ ]:


next(num)


# In[ ]:


next(num)


# In[ ]:


next(num)  #抛出异常


# In[ ]:


# Fibonacci，除了第一个和第二个数之外，任意一个数都可以由前两个数相加得到

def fib(n):
    a,b,i=0,1,0
    while i<n:
        print(b)
        a,b=b,a+b   # a=b, b=a+b  a=0,b=1  a=b=1,b=a+b=1,a=b=1,b=a+b=2
        i=i+1
fib(10)


# In[ ]:


def fib(n):
    a,b,i=0,1,0
    while i<n:
        yield b
        a,b=b,a+b   # a=b, b=a+b  a=0,b=1  a=b=1,b=a+b=1,a=b=1,b=a+b=2
        i=i+1


# In[ ]:


for f in fib(10):
    print(f)
#怎么!
