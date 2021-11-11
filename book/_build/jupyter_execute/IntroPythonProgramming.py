#!/usr/bin/env python
# coding: utf-8

# # Intro Python Programming

# <img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png">

# Python is a high-level computer language developed by Guido van Rossum and released in 1991.  It is now used in a <a href='https://python.org/about/apps' target="_blank">large variety of applications</a>

# Python's core philosophy includes aphorisms like:
# * Beautiful is better than ugly.
# * Explicit is better than implicit.
# * Simple is better than complex.
# * Complex is better than complicated.
# * Readability counts.
# 

# "Python is an interpreted, object-oriented, high-level programming language with dynamic semantics."
# 
# * Interpreted -- you don't have to compile Python code in order to run it.
# * The simplicity and readability can increase productivity
# * It can be very easy to learn, but it's also a powerful language with many libraries that enhance its ability to efficiently tackle a wide range of computational problems.
# 
# Another interesting tidbit -- "Python" comes from Monty Python's Flying Circus, rather than the snake.

# ## Various ways to run Python code
# 
# * Interactively at a prompt
# * With a file that contains the code you want
# * Inside of an interactive development environment

# Let's switch over to the terminal for awhile to explore....

# In[ ]:


# Enter commands here:


# ## Calculating

# Simple example: compound interest calculator with annual contributions
# 
# * p = principal
# * r = annual interest rate in percent
# * y = year of the balance
# * c = annual contribution (made at the start of the year)
# 
# $$\text{Balance}(y) = p(1 + r)^y + c\left[\frac{(1 + r)^{y+1} - (1 + r)}{r} \right]$$

# In[ ]:


p1 = 1000
r1 = 0.05
y1 = 1
c1 = 100
p1*(1 + r1)**y1 + c1*( ((1 + r1)**(y1 + 1) - (1 + r1)) / r1 )


# In[ ]:


p2 = 1
r2 = 0.05
y2 = 45
c2 = 6500
p2*(1 + r2)**y2 + c2*( ((1 + r2)**(y2 + 1) - (1 + r2)) / r2 )


# ## Strings

# In[ ]:


parrotreturn = "This parrot is no more! It has ceased to be!"


# In[ ]:


type(parrotreturn)


# In[ ]:


parrotreturn


# In[ ]:


parrotreturn[1]


# In[ ]:


parrotreturn[0]


# Do note:  Python numbering starts at 0, not 1

# In[ ]:


parrotreturn[0:3]


# In[ ]:


parrotreturn[0:4]


# Slicing includes the first number but not the last

# In[ ]:


# also includes whitespace
parrotreturn[0:6]


# In[ ]:


parrotreturn.index('!')


# What exactly is ".index"? -- index is a *method* and the "." notifies Python to call the method associated with parrotreturn.

# In[ ]:


# Use parrotreturn.index('!') and slicing to print out only the first sentence of the string


# In[ ]:


print(parrotreturn)


# In[ ]:


parrotreturn = '"This parrot is no more! It has ceased to be!"'


# In[ ]:


print(parrotreturn)


# In[ ]:


parrotreturn = "\"This parrot is no more! It has ceased to be!\""


# In[ ]:


print(parrotreturn)


# In[ ]:


parrotreturn = "\"This parrot is no more!\"\n\"It has ceased to be!\""


# In[ ]:


print(parrotreturn)


# Strings can also be concatenated and expanded with math operators

# In[ ]:


"spam"


# In[ ]:


"spam"*3


# In[ ]:


'spam'*3 + ' and ham and eggs'


# In[ ]:


return3 = "It's expired and gone to meet its maker!"


# In[ ]:


parrotreturn + return3


# In[ ]:


print(parrotreturn + return3)


# In[ ]:


# clean up the quote so that the formatting is consistent


# In[ ]:


# put the entire string into one variable
# and use the bracket syntax with slicing to print only the middle sentence


# ## Lists

# In[ ]:


holyhandgrenade = [1, 2, 5]


# In[ ]:


holyhandgrenade[1]


# In[ ]:


holyhandgrenade[0]


# In[ ]:


holyhandgrenade[3]


# In[ ]:


holyhandgrenade[-1]


# In[ ]:


holyhandgrenade[-3]


# In[ ]:


holyhandgrenade[-4]


# In[ ]:


holyhandgrenade[-3:-1]


# In[ ]:


holyhandgrenade[-3:0]


# In[ ]:


holyhandgrenade[-3:]


# In[ ]:


holyhandgrenade[:]


# In[ ]:


holyhandgrenade[2]


# In[ ]:


holyhandgrenade[2] = 3


# In[ ]:


holyhandgrenade[:]


# In[ ]:


holyhandgrenade = ['one','two','five']


# In[ ]:


holyhandgrenade


# In[ ]:


holyhandgrenade.sort()


# In[ ]:


holyhandgrenade


# In[ ]:


holyhandgrenade.reverse()


# In[ ]:


holyhandgrenade


# In[ ]:


help(holyhandgrenade)


# In[ ]:


holyhandgrenade.append('three')


# In[ ]:


holyhandgrenade


# In[ ]:


print(holyhandgrenade.__doc__)


# In[ ]:


get_ipython().run_line_magic('pinfo', 'holyhandgrenade')


# In[ ]:


type(holyhandgrenade)


# In[ ]:


# make your own list with 5+ elements


# In[ ]:


# try out the "pop" method to see what it does, then try it with a value between the parentheses


# ## Tuples, sets, and dictionaries

# ### Tuples

# In[ ]:


riddleanswers = ('Lancelot', 'Holy Grail', 'blue')


# In[ ]:


riddleanswers[2]


# In[ ]:


riddleanswers[2] = 'green'


# In[ ]:


riddleanswers = ('Lancelot', 43, ['x','y','z'])


# In[ ]:


riddleanswers[2]


# ### Sets

# In[ ]:


riddleanswers = {'Lancelot', 'Holy Grail', 'blue'}


# In[ ]:


riddleanswers[2]


# In[ ]:


'blue' in riddleanswers


# In[ ]:


riddleanswers


# In[ ]:


riddleanswers.add('green')


# In[ ]:


riddleanswers


# In[ ]:


riddleanswers.add('blue')


# In[ ]:


riddleanswers


# ### Dictionary

# In[ ]:


riddleanswers = {'name':'Lancelot', 'quest':'Holy Grail', 'favorite colour':'blue'}


# In[ ]:


riddleanswers[2]


# In[ ]:


riddleanswers['favorite colour']


# In[ ]:


riddleanswers.keys()


# In[ ]:


riddleanswers.values()


# In[ ]:


# Add a new key/value pair to riddleanswers


# In[ ]:


# Do a quick search on Google and see if you can figure out how to remove "name":"Lancelot" from the dict


# ## Conditionals and Loops

# Mathematical conditions:
# * Equals: `==`
# * Does not equal: `!=`
# * Less than: `<`
# * Less than or equal to: `<=`
# * Greater than: `>`
# * Greater than or equal to: `>=`

# In[ ]:


3 == 4


# In[ ]:


3 != 4


# In[ ]:


3 < 4


# In[ ]:


3 <= 4


# In[ ]:


3 > 4


# In[ ]:


3 >= 4


# ### Executing commands based on a condition:  if, elif, and else

# In[ ]:


if 3 == 4:
    print('3 is equal to 4')


# In[ ]:


if 4 == 4:
    print('This is self-evident')


# Python uses indentation to define blocks of code
# * this is not merely a matter of style in Python
# * it is *very* important for defining blocks of code
# * it is up to you how many spaces you want to use for indentation, as long as you are consistent
# * you can not mix tabs and spaces -- here in Jupyter, the indentation is set automatically to 4 spaces

# In[ ]:


if 3 == 4:
    print('3 is equal to 4')
elif 3 > 4:
    print('3 is greater than 4')


# In[ ]:


if 3 == 4:
    print('3 is equal to 4')
elif 3 < 4:
    print('3 is less than 4')


# In[ ]:


if 3 == 4:
    print('3 is equal to 4')
elif 3 > 4:
    print('3 is greater than 4')
else:
    print('3 is not equal to or greater than 4')


# Combine conditions:
# * and
# * or
# * not

# In[ ]:


(1==1) and (2==2)


# In[ ]:


(1==2) or (2==2)


# In[ ]:


not(1==2)


# In[ ]:


claim = 5
if claim == 1 or claim == 2:
    print('do not throw the grenade yet')
elif claim == 3:
    print('throw the grenade')
elif claim == 5:
    print('Silly Arthur.  3 comes after 2.')
else:
    print('You are too late - kaboom!')


# In[ ]:


# Switch the value of claim above several times and execute
# Make sure you follow the logic of the resulting print statement.


# ### While loops

# In[ ]:


disneytrip = 0
while disneytrip < 10:
    print(disneytrip + ': Are we there yet?')
    disneytrip += 1


# In[ ]:


# disneytrip = 0
# while disneytrip == 0:
#     print('Are we there yet?')


# It can be very useful to learn how to decipher these error messages.
# 
# Though we don't often pause to reflect on it, "add" depends on context -- Adding 2 + 2 is different than adding me to your list of workshop instructors

# In[ ]:


disneytrip = 0
while disneytrip < 10:
    print(str(disneytrip) + ': Are we there yet?')
    disneytrip += 1


# ### For loops

# In[ ]:


for disneytrip in range(10):
    print(str(disneytrip) + ': Are we there yet?')


# In[ ]:


for letter in parrotreturn:
    print(letter)


# In[ ]:


for letter in parrotreturn:
    print(letter, end='')


# In[ ]:


riddleanswers


# In[ ]:


for k in riddleanswers:
    print(k)


# In[ ]:


for k in riddleanswers:
    print(riddleanswers[k])


# In[ ]:


for key, value in riddleanswers.items():
    print(key + ': ' + value)


# In[ ]:


for i in range(3):
    print(i)


# In[ ]:


for i in range(1,4):
    print(i)


# In[ ]:


# Create a for loop that prints the sequence 1, 2, 5


# ## Functions

# Back to our simple example of a compound interest calculator with annual contributions
# 
# * p = principal
# * r = annual interest rate in percent
# * y = year of the balance
# * c = annual contribution (made at the start of the year)
# 
# $$\text{Balance}(y) = p(1 + r)^y + c\left[\frac{(1 + r)^{y+1} - (1 + r)}{r} \right]$$

# Ideally we'd like to plug in a bunch of numbers and see what comes out.
# 
# Functions allow you to collect together a block of code, name it, and run it when called.
# 
# You can pass data into functions and you can get results returned from functions.

# In[ ]:


def f():
    print('Hello World!')


# In[ ]:


f()


# In[ ]:


def f2(a):
    return a*2


# In[ ]:


f2


# In[ ]:


f2(3)


# In[ ]:


f2(a=4)


# In[ ]:


def f(p,r,y,c):
    return p*(1 + r)**y + c*( ((1 + r)**(y+1) - (1 + r)) / r )


# In[ ]:


principal = 1000
rate = 5
year = 1
annual_contribution = 100
f(principal, rate, year, annual_contribution)


# In[ ]:


principal = 1000
rate = 5
year = 1
annual_contribution = 100
f(principal, rate/100, year, annual_contribution)


# In[ ]:


principal = 1000
rate = 5
year = 45
annual_contribution = 6500
f(principal, rate/100, year, annual_contribution)


# In[ ]:


def f2digit(p,r,y,c):
    r = r/100
    return '{:.2f}'.format(p*(1 + r)**y + c*( ((1 + r)**(y+1) - (1 + r)) / r ))


# In[ ]:


principal = 1000
rate = 5
year = 45
annual_contribution = 6500
f2digit(principal, rate, year, annual_contribution)


# In[ ]:


def f2digit(p,r,y,c):
    r = r/100
    amountsaved = '{:.2f}'.format(p*(1 + r)**y + c*( ((1 + r)**(y+1) - (1 + r)) / r ))
    saying = "If you save for " + str(y) + " years, then you'll have $" + amountsaved + " in your retirement."
    return saying


# In[ ]:


principal = 1000
rate = 5
year = 45
annual_contribution = 6500
f2digit(principal, rate, year, annual_contribution)


# What if you want commas in your number?
# 
# * Google is a fantastic reference for python questions
# * Many many common questions have already been asked and answered
# * A quick search may lead you right to the answer you need
# (https://stackoverflow.com/questions/5180365/python-add-comma-into-number-string)

# In[ ]:


def f2digit(p,r,y,c):
    r = r/100
    amountsaved = '{:,.2f}'.format(p*(1 + r)**y + c*( ((1 + r)**(y+1) - (1 + r)) / r ))
    saying = "If you save for " + str(y) + " years, then you'll have $" + amountsaved + " in your retirement."
    return saying


# In[ ]:


principal = 1000
rate = 5
year = 45
annual_contribution = 6500
f2digit(principal, rate, year, annual_contribution)


# To follow up on this after class, you may find it interesting to check out the documentation for Python.
# * The answers on that stackoverflow page have a link for PEP (Python Enhancement Proposal) and thereby to https://www.python.org/
# * The page also has another link for the official documentation (https://docs.python.org/3/)
# * You may not immediately appreciate all the points on the documentation site, but that is ok.
# * It's intended to be a complete reference, and therefore reading through it is like reading through a dictionary -- not necessarily fun, but comprehensive
# 

# In[ ]:


# Write your own function definition


# In[ ]:


# Call your function several times to make sure it works


# ## Modules

# A module is like a library book containing code.  You can write your own module files that include functions you want to save or variables that you want to associate with the code.  
# 
# You can fetch a module using "import", and then all of its variables and functions will be usable inside the local code you are running.  It's therefore very useful for using code that others have already written.

# In[ ]:


import mymodule


# In[ ]:


dir(mymodule)


# In[ ]:


mymodule.holyhandgrenade


# In[ ]:


for i in range(len(mymodule.holyhandgrenade)):
    print(mymodule.holyhandgrenade[i])


# In[ ]:


from mymodule import holyhandgrenade as hhg


# In[ ]:


hhg


# In[ ]:


import mymodule as mm


# In[ ]:


mm.hhg


# In[ ]:


mm.holyhandgrenade


# In[ ]:


help(mymodule.compound_calculator)


# In[ ]:


print(mymodule.compound_calculator.__doc__)


# In[ ]:


get_ipython().run_line_magic('pinfo', 'mymodule.compound_calculator')


# In[ ]:


mymodule.compound_calculator(1000,5,1,100)


# In[ ]:


mm.riddleanswers


# In[ ]:


mm.stocksDict


# In[ ]:


import numpy as np
import matplotlib.pyplot as plt


# In[ ]:


t = np.linspace(0, 2*np.pi, 1000)


# In[ ]:


t


# In[ ]:


y = np.sin(t)


# In[ ]:


y


# In[ ]:


plt.plot(t,y);


# In[ ]:


fig,ax = plt.subplots()
plt.plot(t,y)
plt.xlim(0,2*np.pi)
plt.xlabel('t',fontsize=14)
plt.ylabel('y',fontsize=14)
ax.text(7,0, 'We are plotting the equation $y(t) = \sin(t)$', fontsize=14);


# ## Various ways to run Python code
# 
# * Interactively at a prompt
# * With a file that contains the code you want
# * Inside of an interactive development environment

# ## A Few Resources to Start
# 
# * Python Org
#   * Beginner's Guide: https://wiki.python.org/moin/BeginnersGuide
#   * Documentation about Setup: https://docs.python.org/3/using/index.html
#   * Python Download: https://www.python.org/downloads/
#   * General Python Documentation: https://www.python.org/doc/  
# * Anaconda
#   * Download: https://www.anaconda.com/products/individual
#   * Documentation: https://docs.anaconda.com/
#     * *Anaconda® is a package manager, an environment manager, a Python/R data science distribution, and a collection of over 7,500+ open-source packages.*
