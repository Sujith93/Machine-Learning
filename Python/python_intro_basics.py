######
'''
python
-an interpreted.
-object-oriented.
-high level programming language with dynamic semantics.
'''


###############Assignment 

person1="sujith"
person2="Kumar"

person1,person2,person3="Sujith","Kumar","Soppa"

var1=var2=var3="Apples"

######### Arithematic operators
num1 = 10
num2 = 20

print('num1 + num2=',num1+num2)
print('num1 + num2=',num1+num2)
print("num1 - num2=",num1-num2)
print("num1 * num2=",num1*num2)
print("num1 / num2=",num1/num2)
print('5^3=',5**3)
print('20 % 3 =',20%3) #remainder
print('22/7=',22/7) #floor division

print('3.8/2=',3.8/2)

########## Assignment operators
num3 = num1 + num2
print(num3)
num3 += num2 #short hand #when dealing with 2 vriables  #num3 = num3 + num2
print(num3)


x=5
x/=5
print(x)

x%=5
print(x)

x//=2
print(x)

x**=5
print(x)

############ comparison operators
print('Is num3 > num2 ?',num3 > num2)
print('Is num2 = num3 ?', num2 == num3)
print('Is num1 != num2 ?',num1 != num2)


############# comments
#single line with # sign
#multiple line 3 quotes '''     '''


############ logical operators
x=True
y=False

print("x and y",x and y)
print('x or y',x or y)
print('not of x',not x)

########### Bitwise operators
'''
example:
a|b :7->111
	  5->101
output:	 7->111
'''

num4 = 6 #110
num5 = 2 #010

print('Bitwise and =',num4 & num5)
print('Bitwise or =',num4 | num5)
print('Bitwise xor =',num4 ^ num5)

'''
left shift:a>>b
ex: 3 >> 2 = 0
  0011		0000

right shift: a<<b
ex: 3 << 2 = 12
  0011		1100
'''

print('num4 right shift by 2=',num4 >> 2)
print('num5 left shift by 2=',num5 << 2)

################ identity operators
x=5
x is 5
x is not 5


################ membership operators
x=[1,2,3,4,5]

3 in x
3 not in x



#################### data types ################
'''
Immutable
-number
-string
-Tuples
Mutable
-lists
-dictionary
-sets
'''

'''
Tuples are represented by ()
list are represented by []
dictionary are represented by {}
'''
#############Numbers
#Integer
4+2
2**3

#Float
2.0+5
6/3

#Complex
(3+4j)+(1+1j)
(2+2j)*2

#############strings
#single line
sample="welcome to pyton"
#or
sample='welcome to pyton'

#multiple line (3 or 6)
sample=''' this 
          is 
        sujith '''

##operations
#concatenaton
'Python'+'Tutorial'
#Repetition
'Python'*2
#sliciing
string1='python' 
string1[2:5]
string1[2:-2]
#indexing
string1='python' 
string1[-1]+string1[1]

string="It's a nice day"
string='It\'s a nice day' 	#excape sequance

# multiple line code
if "sujith_kumar" \
 == \
"Sujith_kumar":
	print("HI")
else:
	print("HELLO")



##type specific methods
#find()
str='Tutorial'
str.find('torial')
#replace()
str='Tutorial'
str.replace('Tu','t')
#split()
str='T,u,t,o,r,i,a,l'
str.split(',')
#count()
str='sujiths'
str.count('s')

#upper()
str.upper()
#max()
str.max()
#min()
str.min()
#isalpha
str.isalpha()



#auto completion
#pip install rope


####################tuple
#tuples are defined by using curve braces
#tuples cant change unlike list

#operation
#concatenation
tup=('a','b','c')
tup+('d','f')

len(tup)

#repetition
tup=('a','b','c')
tup*2

#slicing
tup=('a','b','c')
tup[1:5] #it does not gives error

#indexing
tup=('a','b','c')
tup[0]

#del-deleting tuple will not work
del tup[0]


####################List

#list is a collection of number,strings ,etc
#modify
#defined using square braces



myList = ["sujith",12.3,'pyhon']

len(myList)

#sequance operators
#concatenation
['d','e','f']+['s']
#repetition
['a',12,'b']*2
#slicing
list=['a','b','c','d']
list[1:5]

#indexing
list=['a','b','c','d']
list[0]

#type specifiy methods
#append
list=['a','b','c','d']
list.append('d')   #single value

#extend
list=['a','b','c','d']
list.extend(['s','u']) #another list

#insert
list=['a','b','c','d']
list.insert(2,'x') #with index

#pop
list=['a','b','c','d']
list.pop() #last element eliminating

#del
del list[1]
  

List=["A","a","B","Z","z"]   #min uppercase A #max-lowercase z
#max 
max(List)

#min
min(List)

List=["A","a","B","Z","z",1,20,9,200]  ## numbers + uppercase letters + lowercase letters
min(List)
max(List)

List1=["a","a","b"]
List1.count("a")
List1.count("b")




################dictionary
#key and value pair
students={"sujith":14,"Kumar":12,"Raj":26}

students["sujith"] #retriving key
students["sujith"]=13 #changing value

students["sujith"]

#types:
#empty dictionary
myDict={}
#dictionary with integer keys
myDict={1:'apple',2:'ball'}
#dictionary with mixed keys
myDict={'name':'john',1:[2,4,6]}
#from sequence having each item as a pair
myDict=dict([(1,'apple'),(2,'ball')])


myDict={1:'Green',2:'Blue',3:'Red',2:'grey'}  #same key 
#the latest key value is considered


#Accessing Dictionary
myDict[3] #red
#len
len(myDict)
#key
myDict.key()
#values
myDict.values()
#items
myDict.items()
#get()
myDict.get(1)
#update()
myDict.update({4:'black'})
#pop()
myDict.pop(2)




#type specific
del students["Kumar"]
students 

students.clear()        #clear all the elements in the dict
students   

students={"sujith":14,"Kumar":12,"Raj":26}
len(students)

students.keys()  #only keys
students.values()  #only values

students2={"sujith":16,"Kumar":42,"Raj":56}
students.update(students2)   #will not update for same keys values also wnt change
students

students2={"Sujith":16,"KumaR":42,"RaJ":56}
students.update(students2)  #keys must me different
students



#sets
#unoredered collections of items
#contains only unique elements.(no duplcates)
#defined with {}

my_set={1,2,5,7,5,10,8,2,1}
my_set  #repeated values are not allowed

#operations
#union
mys1={1,2,'c'}
mys2={1,'b','c'}

mys1 | mys2
#intersection
mys1 & mys2
#difference
mys1-mys2  #elements which are not in mys1
mys2-mys1  #elements which are not in mys2




###############################flow control############################
#7 types
#if
#if else
#if elif else

#for 
#while
#break
#continue

'''
if(condition):
    statement1
else
    statement2
'''

'''
if(condition):
    statement1
elif(condition2):
    statement2
else:
    statement3

'''

#exapmle1
if 5>2:
    print("MY name is sujith")




if 2>5:
    print("MY name is sujith")
else:
    print("MY name is kumar")



marks=75
if(marks>80):
    print("Grade A")
elif(marks> 60) and (marks<=80):
    print("Grade B")
elif(marks >40) and (marks<=60):
    print("Grade c")
else:
    print("Grade D")


#and  
age=14
name="sujith"
if age>13 and name=="sujith":
    print("Elligible")

#or
age=14
name="kumar"
if age>13 or name=="sujith":
    print("Elligible")


#for - u know how many times the loop will run
#while - u dnt know how many times the loop will run

'''
while(condition is True):
        statement1
'''

counter=10
while counter<10:
	print(i)
	counter=counter+1
    
#break functions comes out of the present loop
	
counter=0
while counter<10:
	if counter==4:
		break
	print(i)
	counter=counter+1
    
counter=0
while counter<10:
	if counter==4:
		break
	else:
		pass
	print(i)
	counter=counter+1
    
    
for i in "Python":
		if i=="h":
			continue
		print(i)


#try & except:

try:
	if name>3:
		print("HI")
except:
	print("Python ran into an error.Please take a  look at ur code.")
    
    



num=int(input('Enter the value of n='))
if num<0:
    print("enter a valid number")
else:
    sum=0
    while(num>0):
        sum+=num
        num-=1
print(sum)


#for
for i in range(0,5):
    print(i)

#using list
shopingList=["Milk","Eggs","Oranges"]
for i in shopingList:
	print(i)

#using tuples
tup=(2,34,90)
for i in tup:
	print(i)

for i in range(0,101,2):
	print(i)
	
for i in range(100,0,-1):
	print(i)

for i in range(0,5):
	for j in range(0,5):
		print(j)






#str-->repr  #concate string with number

for quant in range(99,0,-1):
    if quant>1:
        print(quant,"Bottles of beer on the wall",quant,"bootle of beer")
        if quant >2:
            #suffix=str(quant)+"Bottles of beer on the wall"
            suffix=repr(quant)+"Bottles of beer on the wall"
        else:
            suffix="1 bottle of beer on the wall"
    elif quant==1:
        print("1 bottle of beer on the wall,1 bottle of beer")
        suffix="no more beer on the wall"
    print("Take one down and pass it around",suffix)
    print("----")
    


'''
(99, 'Bottles of beer on the wall', 99, 'bootle of beer')
('Take one down and pass it around', '99Bottles of beer on the wall')
----
(98, 'Bottles of beer on the wall', 98, 'bootle of beer')
('Take one down and pass it around', '98Bottles of beer on the wall')
----
(97, 'Bottles of beer on the wall', 97, 'bootle of beer')
('Take one down and pass it around', '97Bottles of beer on the wall')
----
'''


#break
count=0
while True:
    print(count)
    count+=1
    if count>10:
        break

#continue
for x in range(20):
    if x%2==0:
        continue
    print(x)

#######################function#####################
#2types
#user defined function
#built-in function

#functions
def functionName():
	for i in range(0,5):
		print(i)

		
functionName()


def addNum(first,second):
	return(first+second)

addNum(42,3)



#inbuilt fuction
abs(-4)
abs(2) 

bool(1)
bool(0)
bool(-1)
bool(45)
bool("asd")
bool(None)

tiger="I am a tiger"
dir(tiger)

help(tiger.uppper)
help(tiger.replace)


eval('print("HI")')
eval('23*8')

program='''print(HI there)
print('My name  is sujith kumar')'''

exec(program)
eval(program) #gives error


age=input("Enter your age:")
age	#by default its a string


int('23')
float('123.456')
str(14)


list1=[23,25,234,635]
sum(list1)




def add(a,b):
    result=a+b
    return result

add(2,3)


def fibo(n):
    a=0
    b=1
    for x in range(n):
        a=b
        b=a+b
        print(a)
    return b
num=int(input("enter the value of n:"))
fibo(num)





################################file handling###########
fp=open("D:/python.txt",'w+')
fp.write("pythin is Fun")
fp.seek(0)
print(fp.read())
fp.close()








###############object oriented########################
class ClassName:
    pass


instance=ClassName()


###
#ex:1
class Students:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade

student1=Students("sujith",24,"12th") #parameters must match(not more than or less than 3 parameters)
student1.name
student1.age
student1.grade




class Students:
    def __init__(self,name,age,grade):
            pass
        
        
student1= Students("sujith",24,"12th")
#student1.name   Error will occur because it is not insitated.




#ex:2
class Students:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def displayStudent(self):
        return("Student name is " + self.name + " and age is "+str(self.age))
    
stu=Students("Suj",15)
stu.displayStudent()




class Students:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        

Students1=Students("A1",17)
Students2=Students("A2",19)

hasattr(Students1,"age")
hasattr(Students1,"grade")

setattr(Students1,"grade","8th") #to add elements
hasattr(Students1,"grade")


getattr(Students1,"grade")

delattr(Students1,"grade")
hasattr(Students1,"grade")




#####
class Parent:
    counter=10
    def __init__(self):
        print("Class Initialized.")
    def parentFunc(self):
        print("ParentFunc beign called")
    def setCounter(self,num):
        Parent.counter=num
    def showCounter(self):
        print(str(Parent.counter))

class Child:
    def __init__(self):
        print("Child class being initialized")
    def childFunc(self):
        print("Child Func being called")

class Child(Parent):
    def __init__(self):
        print("child class is initialized")
    def childFunc(self):
        print("Child Func being called")

c=Child()
c.childFunc()

c.parentFunc()
c.counter
c.setCounter(20)
c.showCounter()





#over ride

class Parent:
    def func(self):
        print("This is a parent class")
        
class Child(Parent):
    def func(self):
        print("This is a child class")
        

c=Child()
c.func()







#file
file1=open("textfile.txt","r")
file1.read()
file1.read()    #second time this show empty as the cursor position is at end.

file1.seek(0,0) #reset the position to zero
file1.read()

file1.tell()

file1.seek(0,0)
file1.read(21) #21 characters
file1.read(21) #next 21 characters



ufn=input("Enter your filename:")
ufn=ufn+'.txt'
file1=open(ufn,"r")
file2=open("copiedfile.txt","r")
#file2.write(file1.read())

file2.read()



#########################random
import random
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))



#Guessing game
import random

comGuess=random.randint(0,100)

while True:
    userGues=int(input("Guess the number between 0-100:"))
    if userGues > comGuess:
        print("Guess Lower")
    elif userGues < comGuess:
        print("Guess higher")
    else:
        print("Congrates,you've guessed the number")
        break
    

import random
food=["Sujith","Kumar","Soppa","Venkata"]
print(random.choice(food))
print(random.choice(food))
print(random.choice(food))
print(random.choice(food))
print(random.choice(food))

food
random.shuffle(food)
food





#######################
import sys
inputStatement=sys.stdin.readline() #enter the line
inputStatement

inputStatement=sys.stdin.readline(10)#enter only 10 characters
inputStatement


sys.stdout.write("This statement is awesome!")

sys.version






###########################
import time


time.time()

def numbers(max):
    time1=time.time()
    for i in range(0,max):
        print(i)
    time2=time.time()
    print(str(time2-time1))


numbers(100)
numbers(1000)
numbers(10000)

time.asctime()
time.localtime()
t=time.localtime()
year=t[0]
year
day=t[2]
day
month=t[1]
month


print(str(day)+'/'+str(month)+'/'+str(year))


for i in range(0,5):
    print(i)


for i in range(0,5):
    print(i)
    time.sleep(1)




########################class#################
class Student:
    
    pass


std_1=Student()  #obj1
std_2=Student()  #obj2

#instance variables-variables which is unique for each instamce or an object 
std_1.first="sujith"
std_1.last="kumar"
std_1.email="sujith@school.com"
std_1.marks=55

std_2.first="Praveen"
std_2.last="krishna"
std_2.email="Praveen@school.com"
std_2.marks=90


print(std_1.email)
print(std_2.email)

print(std_1.first)
print(std_2.first)


######init function(or) method , instance variable=first,last,marks

class Student:
    
    def __init__(self,first,last,marks):
        self.first=first
        self.last=last
        self.marks=marks
        self.email=first+'.'+last+'@gmail.com'
        
std1=Student("sujith","kumar",60)
std2=Student("Praveen","krishna",90)

print(std1.first)
print(std2.first)

print(std1.email)
print(std2.email)

#add actions by methods

print('{} {}'.format(std1.first,std1.last))

class Student:
    
    def __init__(self,first,last,marks):
        self.first=first
        self.last=last
        self.marks=marks
        self.email=first+'.'+last+'@gmail.com'
    
    def fulname(self):
        return '{} {}'.format(self.first,self.last)
        
std1=Student("sujith","kumar",60)
std2=Student("Praveen","krishna",90)

print(std1.fulname())
print(std2.fulname())


#class variables


class Student:
    perc_rise=1.05
    
    def __init__(self,first,last,marks):
        self.first=first
        self.last=last
        self.marks=marks
        self.email=first+'.'+last+'@gmail.com'
    
    def fulname(self):
        return '{} {}'.format(self.first,self.last)
    def apply_raise(self):
        self.marks=int(self.marks*1.05)
        
        
std1=Student("sujith","kumar",60)
std2=Student("Praveen","krishna",90)


print(std1.marks)
std1.apply_raise()
print(std1.marks)


print(std2.marks)
std2.apply_raise()
print(std2.marks)


print(std2.__dict__) #give everything about std2

print(Student.__dict__) #class





############## Inheritance ##################
#Dumb class 


class Student:
    perc_rise=1.05
    
    def __init__(self,first,last,marks):
        self.first=first
        self.last=last
        self.marks=marks
        self.email=first+'.'+last+'@gmail.com'
    
    def fulname(self):
        return '{} {}'.format(self.first,self.last)
    def apply_raise(self):
        self.marks=int(self.marks*1.05)

class Dumb(Student):
    pass

std1=Dumb("sujith","kumar",60)
print(std1.email)
print(help(Dumb))

############
class Student:
    perc_rise=1.05
    
    def __init__(self,first,last,marks):
        self.first=first
        self.last=last
        self.marks=marks
        self.email=first+'.'+last+'@gmail.com'
    
    def fulname(self):
        return '{} {}'.format(self.first,self.last)
    def apply_raise(self):
        self.marks=int(self.marks*1.05)

class Dumb(Student):
   perc_rise=1.10

std1=Dumb("sujith","kumar",60)
print(std1.perc_rise)


std1=Student("sujith","kumar",60)
print(std1.perc_rise)


####################Inheritance

class Student:          #base class
    perc_rise=1.05
    
    def __init__(self,first,last,marks):
        self.first=first
        self.last=last
        self.marks=marks
        self.email=first+'.'+last+'@gmail.com'
    
    def fulname(self):
        return '{} {}'.format(self.first,self.last)
    def apply_raise(self):
        self.marks=int(self.marks*1.05)

class Dumb(Student):        #parent class
   perc_rise=1.10
   def __init__(self,first,last,marks,prog_lang):
       #super(Dumb,self).__init__(first,last,marks)
       Student.__init__(self,first,last,marks)
       self.prog_lang=prog_lang

std1=Dumb("sujith","kumar",60,"Python")
print(std1.prog_lang)


'''
#abstract class
#cant be inherited
#only used for base class
#cant create object

#to create object for abstract class
#first create inherit abstract class then create object


from abc import ABC,abstractmethod

class Employee(ABC):
    
    @abstractmethod
    def calculate_salary(self,sal):
        pass
    
class Developer(Employee):
    def calculate_salary(self,sal):
        finalsalary=sal*1.10
        return finalsalary

emp_1=Developer()
print(emp_1.calculate_salary(10000))

'''




#######################Numpy###############################
#powerful n-dmin array

import numpy as np
a=np.array([1,2,3]) #single dim

print(a)

a=np.array([(1,2,3),(4,5,6)])   #2-d array
print(a)

###numpy / list
#less memory
#fast
#convient

import numpy as np
import time 
import sys

#memory occupied by list
s=range(1000)
print(sys.getsizeof(5)*len(s))    #size occupied by 5th element multiple with length of s(array)


#memory occupied by array
D=np.arange(1000)
print(D.size*D.itemsize)


#compute time faster

SIZE = 100000
L1=range(SIZE)
L2=range(SIZE)

A1=np.arange(SIZE)
A2=np.arange(SIZE)

start=time.time()
result=[(x,y) for x,y in zip(L1,L2)]
print(time.time()-start)*1000

start=time.time()
result=A1+A2
print(time.time()-start)*1000


#numpy operations
import numpy as np

a=np.array([(1,2,3),(4,5,6)])
print(a.ndim)

a=np.array([1,2,3])
print(a.ndim)

print(a.itemsize)
print(a.dtype)

a=np.array([1,2,3,4,5,6,7])
print(a.size)
print(a.shape)

a=np.array([(1,2,3),(4,5,6)])
print(a.size)
print(a.shape)


#reshape
#slicing
a=np.array([(1,2,3,4),(3,4,5,6)])
print(a)
a=a.reshape(4,2)
print(a)



a=np.array([(1,2,3,4),(3,4,5,6)])#(1,2,3,4)->0,(3,4,5,6)->1
print(a[0,2])

print(a[0:,3])#0: everything include 0 and every 3rd elemnt in the array

a=np.array([(1,2,3,4),(3,4,5,6),(7,8,9,10)])
print(a[0:2,3])

a=np.linspace(1,3,5) #5values equally spaced btwn 1and 3
print(a)

a=np.linspace(1,3,10) #10values equally spaced btwn 1and 3
print(a)



a=np.array([1,2,3])
print(a.max())
print(a.min())
print(a.sum())

a=np.array([(1,2,3),(3,4,5)])
print(a.sum(axis=0))    #axis 0 is
print(a.sum(axis=1))    #axis 1 is 

print(np.sqrt(a))
print(np.std(a))



a=np.array([(1,2,3),(3,4,5)])
b=np.array([(1,2,3),(3,4,5)])

print(a+b)
print(a-b)
print(a/b)
print(a%b)


#vertical stacking
print(np.vstack((a,b)))

#horizontal stacking
print(np.hstack((a,b)))

#single row
print(a.ravel())


#sin and cosin functions
import matplotlib.pyplot as plt

x=np.arange(0,3*np.pi,0.1)
y=np.sin(x)
plt.plot(x,y)
plt.show


x=np.arange(0,3*np.pi,0.1)
y=np.cos(x)
plt.plot(x,y)
plt.show


x=np.arange(0,3*np.pi,0.1)
y=np.tan(x)
plt.plot(x,y)
plt.show

#log base 10 and exponential function
ar=np.array([1,2,3])
print(np.exp(ar))

ar=np.array([1,2,3])
print(np.log(ar))  #natural log

ar=np.array([1,2,3])
print(np.log10(ar))  #log base 10





#################
'''
activate root
conda
conda update conda
conda update pandas
conda update --all
'''





'''
Q & A
#
1)how to view sparse matrix in python
a)train_cat[1,:].toarray()
2)how to fetch elements from dataframe in pandas
a)df.iloc[125545]
3)Get the column names of a python numpy ndarray
a)myData.dtype.names




'''


str(1)
int('1')



# 2 variables at a time
x = [1, 2, 3]
y = [4, 5, 6]

for i, j in zip(x, y):
   print(str(i) + " / " + str(j))
   
   
   

   



##########turtle
#sqaure
import turtle
t=turtle.Pen()
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)


import turtle
t=turtle.Pen()
for i in range(0,8):
    t.forward(50)
    t.left(45)

t.reset() #for reset

import turtle
t=turtle.Pen()
for i in range(1,38):
    t.forward(100)
    t.left(175)
    
t.reset() #for reset

for i in range(1,20):
    t.forward(100)
    t.left(95)



t.up()  #pen wnt write
t.forward(100)
t.forward(40)
t.down() #pen writes starts
for i in range(1,20):
    t.forward(100)
    t.left(95)




#colors
import turtle
t=turtle.Pen()

t.color(0,0,1)#(y,g,b)
t.begin_fill()
t.forward(150)
t.left(90)
t.forward(30)
t.left(90)
t.forward(40)
t.right(90)
t.forward(40)
t.left(90)
t.forward(70)
t.left(90)
t.forward(40)
t.right(90)
t.forward(40)
t.left(90)
t.forward(30)
t.end_fill()

t.begin_fill()
t.circle(15)
t.end_fill()


#functions in turtle

import turtle
t=turtle.Pen()
def Square(side):
    t.forward(side)
    t.left(90)

Square(10)
Square(50)
Square(100)


def Circle(radius):
    t.circle(radius)
    
Circle(10)
Circle(50)
Circle(100)



#############re

import re
dir(re) #list of function can do with re
string="The night was cold and dark"
re.search("night",string)   
m=re.search("night",string)  #searching the word night
print(m)
start=m.start() #starting the word night
start
end=start+5 #end the word night
end
string[start:end] #extracting the word



string2="asffSUJITHvevlrvlrwwfwew wkjwflwf wf jwfwfj"
position=re.search("SUJITH",string2)
position.start()
position.end()
string2[position.start():position.end()]


# re with urllib
import re
import urllib.request
#import urllib

#https://www.google.com/finance?q=FB
url="https://www.google.com/finance?q="
#FB,GOOG,DATA,BABA
stock=input("Enter the Stock:")
url=url+stock #concatinating
url

data=urllib.request.urlopen(url).read() #reading the page
#data=urllib.urlopen(url).read() #reading the page
data1=data.decode("utf-8")  #convert to html page

m=re.search('meta itemprop="price"',data1)
m
print(m)
start=m.start()
start
end=start+50
newString=data1[start:end]
print(newString)

m=re.search('content="',newString)
start=m.end()
newString1=newString[start:]
m=re.search("/",newString1)
start=0
end=m.end()-3
final=newString1[0:end]
final
print("The value of " +stock+" is "+final)









import re
import urllib.request
#import urllib

#http://www.weather-forecast.com/locations/Paris/forecasts/latest
city=input("Eneter the city:")
url="http://www.weather-forecast.com/locations/"+city+"/forecasts/latest"

data=urllib.request.urlopen(url).read() #reading the page
data1=data.decode("utf-8")  #convert to html page

m=re.search('span class="phrase"',data1)
start=m.end()
end=start+200

newString=data1[start:end]

print(newString)

m=re.search("</span>",newString)
end=m.start()-1
final=newString[0:end]
print(final)





import re
import urllib.request
#import urllib

url="http://www.dictionary.com/browse/"
word=input("Enter the word:")
#Gaudy
url=url+word

data=urllib.request.urlopen(url).read() #reading the page
data1=data.decode("utf-8")  #convert to html page

data1

m=re.search('meta name="description" content="',data1)
start=m.end()
end=start+500

newString=data1[start:end]
print(newString)

m=re.search("See more.",newString)
end=m.start()-1

definition=newString[0:end]
print(definition)





import re
import urllib.request
#import urllib
try:
    url="http://www.dictionary.com/browse/"
    word=input("Enter the word:")
    #Gaudy
    url=url+word
    
    data=urllib.request.urlopen(url).read() #reading the page
    data1=data.decode("utf-8")  #convert to html page
    
    data1
    
    m=re.search('meta name="description" content="',data1)
    start=m.end()
    end=start+500
    
    newString=data1[start:end]
    #print(newString)
    
    m=re.search("See more.",newString)
    end=m.start()-1
    
    definition=newString[0:end]
    print(definition)

except:
    print("I'm sorry.you're word is not in the dictionary.")






#####################bs4
    
from bs4 import BeautifulSoup
soup=BeautifulSoup("<html> <p> qwdqdwd <stron>Hello <a> Hello </html>","html.parser")

soup.prettify()
print(soup.prettify())





html_doc="""
<html>

   <head>
      <title>Heading Example</title>
   </head>
	
   <body>
      <h1>This is heading 1</h1>
      <h2>This is heading 2</h2>
      <h3>This is heading 3</h3>
      <h4>This is heading 4</h4>
      <h5>This is heading 5</h5>
      <h6>This is heading 6</h6>
   </body>
	
</html>

"""
from bs4 import BeautifulSoup
soup=BeautifulSoup(html_doc,"html.parser")
soup
soup.prettify()
print(soup.prettify())

soup.title
soup.head
soup.body
soup.body.h1
soup.body.h2
soup.h1

soup.find_all("h1")

head_tag=soup.head
head_tag.contents
head_tag.title
head_tag.title.string
head_tag.parent


body_tag=soup.body
for i in body_tag.children:
    print(i)


for i in body_tag.descendants:
    print(i)



import re
for tag in soup.find_all(re.compile("h")):
    print(tag.name)


import re
for tag in soup.find_all(re.compile("^ht")):
    print(tag.name)


import requests
from bs4 import *

data= requests.get("https://www.accuweather.com/en/us/san-jose-ca/95110/weather-forecast/347630")
data
soup=BeautifulSoup(data.text,"html.parser")

soup.find('div',{'class':'info'})
data2=soup.find('div',{'class':'info'})
data3=data2.find('span',{'class':'large-temp'})
data3.contents
data3.contents[0]

#direct method by searching on website
a=soup.find('span',{'class':'temp'})
a.contents[0]





#synonym
#http://www.synonym.com/synonyms/cold

import requests
from bs4 import BeautifulSoup

data= requests.get("http://www.synonym.com/synonyms/pronounciation")
data
soup=BeautifulSoup(data.text,"html.parser")

data2=soup.find('ul',{'class':'synonyms'})
data2.a.contents
data2.contents

syn=data2.contents

for i in range(1,len(syn)-1):
    print(syn[i].a.contents)

data2.a.contents
data2.contents




#################
#matplotlib
#pylab

import matplotlib
import matplotlib.pyplot as pt

pt.plot([1,2,3,4],[3,8,10,25]) #line graph
pt.show() #pop up


#Adding title,xlabel,ylabel

import matplotlib.pyplot as plt
plt.plot([1,2,3,4],[3,8,10,25])

plt.title('Rain in December')
plt.xlabel('Days in December')
plt.ylabel('Inches of Rain')

plt.show()



#from file
import matplotlib.pyplot as plt
x=[]
y=[]

readFile=open("coordinates.txt",'r')
data=readFile.read().split("\n") #newline
print(data)
for i in data:
    val=i.split(",")
    print(val)
    x.append(val[0])
    y.append(val[1])

print(x)
print(y)


plt.plot(x,y)
plt.show()



#color,subplot
import matplotlib.pyplot as plt

fig=plt.figure() #creats figure
#Background
rect=fig.patch
rect.set_facecolor("green")

x=[3,7,8,12]
y=[5,13,2,8]
graph1=fig.add_subplot(1,1,1,axisbg='black')#height,weight and 1st graph,if 2,2 means 4 graphs side by side
graph1.plot(x,y,'red',linewidth=4.0)

plt.show()





import matplotlib.pyplot as plt

fig=plt.figure() #creats figure
#Background
rect=fig.patch
rect.set_facecolor("green")

x=[3,7,8,12]
y=[5,13,2,8]
graph1=fig.add_subplot(1,1,1,axisbg='black')#height,weight and 1st graph,if 2,2 means 4 graphs side by side
graph1.plot(x,y,'red',linewidth=4.0)

graph1.tick_params(axis="x",c)

plt.show()




######################################3
import matplotlib.pyplot as plt

fig=plt.figure()

rect=fig.patch
rect.set_facecolor('green')

x=[3,7,8,12]
y=[5,13,2,8]

graph1=fig.add_subplot(1,1,1,axisbg='black') #1by1=spaces 1st position fig 
graph1.plot(x,y,'red',linewidth=4.0)

#tick marks
graph1.tick_params(axis='x',color='white')
graph1.tick_params(axis='y',color='white')

#borders
graph1.spines['top'].set_color('w')
graph1.spines['left'].set_color('w')
graph1.spines['right'].set_color('w')
graph1.spines['bottom'].set_color('w')

graph1.set_title('Random Graph',color='white')
graph1.set_xlabel('This is the x axis',color='white')
graph1.set_ylabel('This is the y axis',color='white')

plt.show()





#mutiple lines
import matplotlib.pyplot as plt

fig=plt.figure()

rect=fig.patch
rect.set_facecolor('green')

x=[3,7,8,12]
y=[5,13,2,8]
x2=[0,4,7,10]
y2=[3,7,1,12]
x3=[2,4,6,12]
y3=[13,5,8,2]

graph1=fig.add_subplot(1,1,1,axisbg='black') #1by1 1st fig
graph1.plot(x,y,'red',linewidth=4.0)
graph1.plot(x2,y2,'yellow',linewidth=2.0)
graph1.plot(x3,y3,'orange',linewidth=6.0)


#tick marks
graph1.tick_params(axis='x',color='white')
graph1.tick_params(axis='y',color='white')

#borders
graph1.spines['top'].set_color('w')
graph1.spines['left'].set_color('w')
graph1.spines['right'].set_color('w')
graph1.spines['bottom'].set_color('w')

graph1.set_title('Random Graph',color='white')
graph1.set_xlabel('This is the x axis',color='white')
graph1.set_ylabel('This is the y axis',color='white')

plt.show()






###multiple graphs
#1
import matplotlib.pyplot as plt

fig=plt.figure()

rect=fig.patch
rect.set_facecolor('green')

x=[3,7,8,12]
y=[5,13,2,8]
x2=[0,4,7,10]
y2=[3,7,1,12]
x3=[2,4,6,12]
y3=[13,5,8,2]

graph1=fig.add_subplot(2,1,1,axisbg='black') #2 grpahs,1,1st fig
graph1.plot(x,y,'red',linewidth=2.0)


#tick marks
graph1.tick_params(axis='x',color='white')
graph1.tick_params(axis='y',color='white')

#borders
graph1.spines['top'].set_color('w')
graph1.spines['left'].set_color('w')
graph1.spines['right'].set_color('w')
graph1.spines['bottom'].set_color('w')

graph1.set_title('Random Graph',color='white')
graph1.set_xlabel('This is the x axis',color='white')
graph1.set_ylabel('This is the y axis',color='white')


#2

graph2=fig.add_subplot(2,1,2,axisbg='black') ##2 grpahs,1,2st fig
graph2.plot(x2,y2,'yellow',linewidth=2.0)


#tick marks
graph2.tick_params(axis='x',color='white')
graph2.tick_params(axis='y',color='white')

#borders
graph2.spines['top'].set_color('w')
graph2.spines['left'].set_color('w')
graph2.spines['right'].set_color('w')
graph2.spines['bottom'].set_color('w')

graph2.set_title('Random Graph',color='white')
graph2.set_xlabel('This is the x axis',color='white')
graph2.set_ylabel('This is the y axis',color='white')

plt.show()






#####multiple graphs 3 graphs
#1
import matplotlib.pyplot as plt

fig=plt.figure()

rect=fig.patch
rect.set_facecolor('green')

x=[3,7,8,12]
y=[5,13,2,8]
x2=[0,4,7,10]
y2=[3,7,1,12]
x3=[2,4,6,12]
y3=[13,5,8,2]

graph1=fig.add_subplot(2,2,1,axisbg='black') #2 grpahs,1,1st fig
graph1.plot(x,y,'red',linewidth=2.0)


#tick marks
graph1.tick_params(axis='x',color='white')
graph1.tick_params(axis='y',color='white')

#borders
graph1.spines['top'].set_color('w')
graph1.spines['left'].set_color('w')
graph1.spines['right'].set_color('w')
graph1.spines['bottom'].set_color('w')

graph1.set_title('Random Graph',color='white')
graph1.set_xlabel('This is the x axis',color='white')
graph1.set_ylabel('This is the y axis',color='white')


#2

graph2=fig.add_subplot(2,2,2,axisbg='black') ##2 grpahs,1,2st fig
graph2.plot(x2,y2,'yellow',linewidth=2.0)


#tick marks
graph2.tick_params(axis='x',color='white')
graph2.tick_params(axis='y',color='white')

#borders
graph2.spines['top'].set_color('w')
graph2.spines['left'].set_color('w')
graph2.spines['right'].set_color('w')
graph2.spines['bottom'].set_color('w')

graph2.set_title('Random Graph',color='white')
graph2.set_xlabel('This is the x axis',color='white')
graph2.set_ylabel('This is the y axis',color='white')

#3

graph3=fig.add_subplot(2,1,2,axisbg='black') ##2 grpahs,1,2nd fig
graph3.plot(x3,y3,'orange',linewidth=2.0)


#tick marks
graph3.tick_params(axis='x',color='white')
graph3.tick_params(axis='y',color='white')

#borders
graph3.spines['top'].set_color('w')
graph3.spines['left'].set_color('w')
graph3.spines['right'].set_color('w')
graph3.spines['bottom'].set_color('w')

graph3.set_title('Random Graph',color='white')
graph3.set_xlabel('This is the x axis',color='white')
graph3.set_ylabel('This is the y axis',color='white')

plt.show()




#bar charts
#normal
import matplotlib.pyplot as plt 
import numpy as np

pos=np.arange(6)+0.5#6 bars,0.5 space

plt.barh(pos,(4,8,12,3,17,6),align='center',color='red')
plt.show()



#bar chartswith names
import matplotlib.pyplot as plt 
import numpy as np

pos=np.arange(6)+0.5#6 bars,0.5 space

names=['A','B','C','D','E','F']
plt.barh(pos,(4,8,12,3,17,6),align='center',color='red')

plt.title('Height of students in inches',color='blue')
plt.xlabel('Height in inches',color='Red')
plt.ylabel('Students',color='Red')

plt.tick_params(axis='x',color='white')
plt.tick_params(axis='y',color='white')

plt.yticks(pos,names)#assigning names

plt.subplots_adjust(left=.11,bottom=.12,right=.94) #adjustments

plt.show()




#pie charts
import matplotlib.pyplot as plt

sizes=[50,23,7,15,5]
plt.pie(sizes)
plt.show()


#modifications of pie charts
import matplotlib.pyplot as plt

sizes=[50,23,15,7,5]
labels=['Android','Apple','windows','Balckberry','Xiaomi']
colors=['yellow','orange','cyan','magenta','red']
plt.pie(sizes,colors=colors,startangle=90,labels=labels)
plt.title('Pie chart')
plt.legend(title='Legend',loc='lower left')
plt.axis('equal') #equall length x and y axies

plt.show()





#3d graph

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

fig=plt.figure()
chart=fig.add_subplot(1,1,1,projection='3d')

X,Y,Z=[1,2,3,4,5,6,7,8],[2,5,3,8,9,5,6,1],[3,6,2,7,5,4,5,6]
chart.plot_wireframe(X,Y,Z)
plt.show()



#3d scatter plot

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

fig=plt.figure()

chart=fig.add_subplot(1,1,1,projection='3d')

X,Y,Z=[1,2,3,4,5,6,7,8],[2,5,3,8,9,5,6,1],[3,6,2,7,5,4,5,6]
chart.scatter(X,Y,Z,c='red',marker='o')

chart.set_xlabel('x axis')
chart.set_ylabel('y axis')
chart.set_zlabel('z axis')
plt.show()



#multiple 3d Scatter plot

#from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

fig=plt.figure()

chart=fig.add_subplot(1,1,1,projection='3d')

X,Y,Z=[1,2,3,4,5,6,7,8],[2,5,3,8,9,5,6,1],[3,6,2,7,5,4,5,6]
xX,yY,zZ=[-1,-2,-3,-4,-5,-6,-7,-8],[-2,-5,-3,-8,9,5,6,1],[-3,-6,-2,-7,-5,-4,5,6]

chart.scatter(X,Y,Z,c='red',marker='o')
chart.scatter(xX,yY,zZ,c='blue',marker='^')

chart.set_xlabel('x axis')
chart.set_ylabel('y axis')
chart.set_zlabel('z axis')
plt.show()



#3d Barchart
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure()

chart=fig.add_subplot(1,1,1,projection='3d')

x=[1,2,3,4,5,6,7,8,9,10]
y=[2,3,4,5,1,6,2,1,7,2]
z=[0,0,0,0,0,0,0,0,0,0]#if not zero it will float

dx=np.ones(10)
#dx=np.zeros(10)
dy=np.ones(10)
dz=[1,2,3,4,5,6,7,8,9,10]#height of bars
chart.bar3d(x,y,z,dx,dy,dz,color='cyan')

chart.set_xlabel('xlabel')
chart.set_ylabel('ylabel')
chart.set_zlabel('zlabel')

plt.show()



#wireframes
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure()
chart=fig.add_subplot(1,1,1,projection='3d')

x,y,z=axes3d.get_test_data(0.05) #0.05 is the delta for fast computation
chart.plot_wireframe(x,y,z,rstride=10,cstride=10)
#rstride=cstride=no of lines(more detailed)

chart.set_xlabel('xlabel')
chart.set_ylabel('ylabel')
chart.set_zlabel('zlabel')

plt.show()




###################pandas##################
#####Series(is the 1-dimensional data structures)
import pandas as pd
s=pd.Series([20,"sujith",78,'Hello']) #with list
s
s[0]
s[1]

s=pd.Series([20,"sujith",78,'Hello'],index=['a','b','c','d']) #index
s
s['a']
s['b']


d={'cat':90,'dog':150,'rat':100}
animals=pd.Series(d)
animals
animals['cat']
animals[animals>95] #condition
animals[animals==90]

animals<200 #bool values

animals['rat']=200 #update
animals

animals[animals<160]=750
animals

print('dog' in animals)

print('buffalo' in animals)

#mathemtical
animals/10

import numpy as np
np.square(animals)#squaring

animals.isnull()#checking null 


######dataframe(is the 2-dimensional data structures)
import pandas as pd
data={'Students':['A1','A2','A3','A4','A5'],
      'Maths':[98,50,23,72,87],
      'Science':[96,45,76,54,1],
      'Sports':['Basketball','Swiming','TT','Badminton','Chess']      
      }

data
Students=pd.DataFrame(data,columns=['Students','Maths','Science','Sports'])
Students
Students=pd.DataFrame(data,columns=['Sports','Maths','Science','Students'])
Students


import pandas as pd
pd.read_csv('Testdata.csv')
pd.read_csv('Testdata.csv',names=['Pizza','cat','dog','cheese'])#both names
pd.read_csv('Testdata.csv',names=['Pizza','cat','dog','cheese'],header=None)#both names
pd.read_csv('Testdata.csv',names=['Pizza','cat','dog','cheese'],header=0)#replace names


pd.read_csv('Testdata.csv')
pd.read_csv('Testdata.csv',usecols=['Date','A'])
pd.read_csv('Testdata.csv',usecols=[0,1])
pd.read_csv('Testdata.csv',usecols=[0,2,3])

#Reading and writing
import pandas as pd
newCSV=pd.read_csv('Testdata.csv',header=0,names=['Food','Price','Quantity'],usecols=[1,2,3])
newCSV
newCSV.to_csv('Testdata2.csv')
newCSV=pd.read_csv('Testdata2.csv')


#https://grouplens.org/datasets/movielens/
#click on 100k (ml-100k.zip)
import pandas as pd
user=pd.read_csv('ml-100k/ml-100k/u.user',sep='|',names=['UserID','Age','Gender','Occupation','ZipCode'])
user
user.head()
user.head(2)
user.head(10)
user.tail()
user.tail(3)
user.tail(10)

user[10:15] #silicing
user[10:15] #from 10 to 15
user[900:] #from 900 to everything
user[:3] #starting upto 3
user[:-2] #cuts the last 2 rows


#####data Manipulation
user['Gender'] #single column
user.ZipCode
user['Gender'].head(10)

columns_i_want=['Occupation','ZipCode'] #multiple columns
user[columns_i_want].head(10)


#users age>30 
user['Age'] >30
user[user.Age >30].head()
#male gender with <40
user[(user.Gender=='M') &  (user.Age <40)].head()
#Female who are writer
user[(user.Gender=='F') &  (user.Occupation=='writer')].head()
#Male people or older tha 60
user[(user.Gender=='M') |  (user.Age >60)].head()

########indexing
import pandas as pd
user=pd.read_csv('ml-100k/ml-100k/u.user',sep='|',names=['UserID','Age','Gender','Occupation','ZipCode'])
user

user.dtypes #datatypes of the columns
user.describe()
user.head()

user.set_index('UserID').head()
user.head()
user.set_index('UserID',inplace=True) #replace the exciting data use inplace
user.head()

user[10:15]
user.ix[[1,12,32]] #selecting any row 


###Merging the data Frames
import pandas as pd
frame1=pd.DataFrame({
        'key':range(5),
        'frame1':['A',"B",'c','d','e']
        })
frame2=pd.DataFrame({
        'key':range(2,7),
        'frame2':['t','u','v','w','x']
        })

frame1
frame2

pd.merge(frame1,frame2,on='key')
pd.merge(frame1,frame2,on='key',how='right') #keep frame2 values add frame1
pd.merge(frame1,frame2,on='key',how='left')
pd.merge(frame1,frame2,on='key',how='outer')
pd.merge(frame1,frame2,on='key',how='inner')


pd.concat([frame1,frame2])
pd.concat([frame1,frame2],axis=1)#side by side




###groupby
#https://www.cityofchicago.org/city/en/depts/dhr/dataset/current_employeenamessalariesandpositiontitles.html
#menu ->downloads->csv
'''
import pandas as pd
chicago=pd.read_csv('Current_Employee_Names__Salaries__and_Position_Titles.csv')
chicago.head()
#headers=['Name','Job Titles','Department','Annual Salary'] #selected columns
chicago1=pd.read_csv('Current_Employee_Names__Salaries__and_Position_Titles.csv',names=[1,2,3,7])
chicago1.head()

dept=chicago.groupby('Department')
dept.count().head()

dept=chicago.groupby('department')
'''


user=pd.read_csv('ml-100k/ml-100k/u.user',sep='|',names=['UserID','Age','Gender','Occupation','ZipCode'])
gender=user.groupby('Gender')
gender.count().head()#not none
gender.size().head()

Occupation=user.groupby('Occupation')
Occupation.count().head()#not none
Occupation.size().head()





#movie lens data
import pandas as pd
col1=['UserID','movie_id','rating','unix_timestamp']
ratings=pd.read_csv('ml-100k/ml-100k/u.data',sep='\t',names=col1)
ratings.head()

col2=['movie_id','title','release_data','ideo_release_date','imdb_url']
movies=pd.read_csv('ml-100k/ml-100k/u.item',sep='|',names=col2,usecols=range(5),encoding='ISO-8859-1')
movies.head()

movie_rating=pd.merge(movies,ratings)
movie_rating.head()

user=pd.read_csv('ml-100k/ml-100k/u.user',sep='|',names=['UserID','Age','Gender','Occupation','ZipCode'])
user.head()

lens=pd.merge(movie_rating,user)
lens.head()


most_rated=lens.groupby('title').size().order(ascending=False)[:20]
most_rated

lens.title.value_counts()[:20]

movie_stats=lens.groupby('title').agg({'rating':[np.size,np.mean]})
movie_stats.head()
movie_stats.sort([('rating','mean')],ascending=False).head()




###graphs on data
user=pd.read_csv('ml-100k/ml-100k/u.user',sep='|',names=['UserID','Age','Gender','Occupation','ZipCode'])
user.head()
import matplotlib.pyplot as plt
user.Age.hist(bins=30)
plt.show()
plt.title('Distribution of users age')
plt.xlabel('age')
plt.ylabel('count of users')
user.Age.hist(bins=30)
plt.show()












####################
#pickle module for saving objects
import pickle
example_dic={1:'6',2:'2',3:"F"}

pickle_out=open("dict.pickle","wb") #witebytes
pickle.dump(example_dic,pickle_out)
pickle_out.close()


pickle_in=open("dict.pickle","rb") #readbytes
example_dict1=pickle.load(pickle_in)
print(example_dict1)


